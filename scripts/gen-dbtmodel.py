#!/usr/bin/env python3
"""
Generate a dbt sources YAML file from a LinkML schema.

IMPORTANT: this script generates dbt sources that describe the *relational*
(SQL) form of the schema, not the raw LinkML class/slot structure. LinkML's
SQL DDL generator (`gen-sqltables` / `SQLTableGenerator`) does not map
classes to tables directly -- it first runs the schema through
`linkml.transformers.relmodel_transformer.RelationalModelTransformer`, which:

  - extracts every multivalued slot (whether its range is a literal type,
    an enum, or a class) into its own linking table, e.g. a 0..* slot
    `external_id` on class `Study` becomes a table `study_external_id`
    with a backref FK column `study_study_id` and a value column
    `external_id`
  - adds backref/foreign-key columns for single-valued class-range slots
  - marks generated PK/FK/backref columns with `primary_key`,
    `foreign_key`, and `backref` annotations

This script runs that same transformer before generating dbt sources, so
the tables/columns it describes -- and the tests it infers -- match what
the SQL DDL generator will actually produce, including linking tables you
did not write by hand in the LinkML schema itself.

Requires the full `linkml` package (not just `linkml_runtime`), since that's
where RelationalModelTransformer lives. If your project already uses LinkML's
SQL generator, you already have this dependency.

Inferred dbt tests, per column:
  - `not_null`         for slots marked `required: true`, and any column
                        that's part of a table's primary key (including
                        composite keys on generated linking tables)
  - `unique`            for a single-column (non-composite) primary key
  - `accepted_values`   for slots whose range is a LinkML enum
  - `relationships`     for any column the transformer marked with a
                        `foreign_key` annotation (covers both ordinary FK
                        slots and the backref columns on linking tables)
  - `uri_or_curie_format` / `valid_uri_format`
                        for slots whose range resolves (following the
                        LinkML type's `typeof` chain, so custom subtypes
                        count too) to the built-in `uriorcurie` or `uri`
                        types. These are custom generic tests -- see the
                        companion `uri_curie_tests.sql` macro file, which
                        must be added to your dbt project's macros/
                        directory (e.g. tests/generic/) for these tests
                        to resolve.

And per table:
  - a `dbt_utils.unique_combination_of_columns` test for composite primary
    keys (e.g. on linking tables) and for any LinkML `unique_keys` spanning
    more than one slot. This requires the `dbt_utils` package in your dbt
    project; pass --no-composite-key-tests to omit these if you don't have
    it installed.

Intended to be run as part of a LinkML project's GitHub release action, e.g.:

    python gen-dbt.py \\
        --schema src/mymodel/schema/mymodel.yaml \\
        --output project/dbt/src_dev_include_access.yml

If --schema is omitted, the script falls back to auto-detecting
src/*/schema/*.yaml, matching the original script's behavior.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from linkml.transformers.relmodel_transformer import RelationalModelTransformer
from linkml_runtime.linkml_model.meta import ClassDefinition, SlotDefinition
from linkml_runtime.utils.schemaview import SchemaView

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def to_snake_case(name: str) -> str:
    """Converts PascalCase / CamelCase string to snake_case.

    Only used for *table* names: the database lower-cases/snake-cases
    class names when they become table names, but column/slot names --
    including the class-name prefixes on generated linking-table backref
    columns -- are left exactly as LinkML/the relational transformer
    produced them, so this must not be applied to column names.
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def annotation_value(slot: SlotDefinition, tag: str) -> str | None:
    """Safely fetch a slot annotation value by tag, or None if absent.

    linkml_runtime's Annotations container doesn't always support a plain
    dict-style .items()/.get() across versions, but `in` and `[]` are
    reliable, so we use those instead.
    """
    if not slot.annotations or tag not in slot.annotations:
        return None
    return slot.annotations[tag].value


def is_primary_key_slot(slot: SlotDefinition) -> bool:
    """A slot is a PK column if LinkML marks it identifier/key, or if the
    relational transformer auto-generated it as part of a linking table's
    primary key (marked via the `primary_key` annotation)."""
    if slot.identifier or slot.key:
        return True
    return str(annotation_value(slot, "primary_key")).lower() == "true"


def resolve_type_root(range_name: str | None, view: SchemaView) -> str | None:
    """Walk a LinkML type's `typeof` chain up to its ultimate base type.

    Schemas often define custom types like `IdentifierType: typeof:
    uriorcurie` rather than using the bare `uriorcurie`/`uri` type names
    directly, so a plain string comparison against `slot.range` isn't
    enough -- we need to follow the chain to see what the type ultimately
    derives from. Returns None if `range_name` isn't a type at all (e.g.
    it's a class or enum reference).
    """
    all_types = view.all_types()
    current = range_name
    visited: set[str] = set()
    while current in all_types and current not in visited:
        visited.add(current)
        typeof = all_types[current].typeof
        if not typeof:
            break
        current = str(typeof)
    return current if current in visited else None


def build_column_tests(
    slot: SlotDefinition,
    pk_names: list[str],
    view: SchemaView,
    class_to_table: dict[str, str],
    source_name: str,
) -> list[Any]:
    """Infer a list of dbt column tests for a single transformed-schema attribute."""
    tests: list[Any] = []
    is_pk = slot.name in pk_names
    is_composite_pk = len(pk_names) > 1

    if slot.required or is_pk:
        tests.append("not_null")

    if is_pk and not is_composite_pk and not slot.multivalued:
        tests.append("unique")

    # Multivalued attributes shouldn't normally survive the relational
    # transform (they get extracted into their own linking tables), but
    # guard anyway in case a future transformer version leaves one inlined.
    if slot.multivalued:
        return tests

    # uriorcurie / uri: LinkML's URI-ish types don't map to a SQL
    # constraint on their own, so add a custom generic test (see
    # `uri_or_curie_format` / `valid_uri_format` in the companion
    # macros this script emits) that checks the value's lexical form
    # against the URI/CURIE grammar. Resolve through the type's `typeof`
    # chain so custom subtypes (e.g. `IdentifierType: typeof: uriorcurie`)
    # are caught too, not just the bare `uriorcurie`/`uri` type names.
    type_root = resolve_type_root(str(slot.range) if slot.range else None, view)
    if type_root == "uriorcurie":
        tests.append("uri_or_curie_format")
    elif type_root == "uri":
        tests.append("valid_uri_format")

    # relationships (foreign key): prefer the transformer's own
    # `foreign_key` annotation, which it sets on every FK/backref column
    # it generates (both ordinary FK slots and linking-table backrefs).
    fk_target = annotation_value(slot, "foreign_key")
    if fk_target and "." in fk_target:
        target_class, target_slot_name = fk_target.split(".", 1)
        target_table = class_to_table.get(target_class)
        if target_table:
            tests.append(
                {
                    "relationships": {
                        "arguments": {
                            "to": f"source('{source_name}', '{target_table}')",
                            "field": f'"{target_slot_name}"',
                            "column_name": f'"{slot.name}"',
                        }
                    }
                }
            )
    elif slot.range and slot.range in view.all_classes():
        # Fallback for schemas/LinkML versions where the annotation isn't
        # present but the range is still clearly a class reference.
        target_id_slot = view.get_identifier_slot(slot.range)
        target_table = class_to_table.get(slot.range)
        if target_id_slot and target_table:
            tests.append(
                {
                    "relationships": {
                        "arguments": {
                            "to": f"source('{source_name}', '{target_table}')",
                            "field": f'"{target_id_slot.name}"',
                            "column_name": f'"{slot.name}"',
                        }
                    }
                }
            )
    elif slot.range and slot.range in view.all_enums():
        # accepted_values: range is an enum with a fixed permissible_values set
        enum_def = view.get_enum(slot.range)
        values = list(enum_def.permissible_values.keys())
        if values:
            tests.append({"accepted_values": {"arguments": {"values": values}}})

    return tests


def build_table_tests(
    class_def: ClassDefinition,
    pk_names: list[str],
    composite_key_tests: bool,
) -> list[Any]:
    """Table-level tests: composite PK uniqueness, and any multi-slot
    LinkML unique_keys not already covered by the PK."""
    if not composite_key_tests:
        return []

    table_tests: list[Any] = []

    if len(pk_names) > 1:
        table_tests.append(
            {
                "dbt_utils.unique_combination_of_columns": {
                    "arguments": {
                        "combination_of_columns": [f'"{x}"' for x in pk_names]
                    }
                }
            }
        )

    for uk in (class_def.unique_keys or {}).values():
        uk_slots = list(uk.unique_key_slots)
        if set(uk_slots) == set(pk_names):
            continue  # already covered by the PK test above
        if len(uk_slots) > 1:
            table_tests.append(
                {
                    "dbt_utils.unique_combination_of_columns": {
                        "arguments": {
                            "combination_of_columns": [str(s) for s in uk_slots]
                        }
                    }
                }
            )

    return table_tests


def apply_single_slot_unique_keys(
    class_def: ClassDefinition, pk_names: list[str], columns: list[dict[str, Any]]
) -> int:
    """LinkML unique_keys spanning exactly one slot map to a plain column-level
    `unique` test rather than a table-level combination test. Returns the
    number of tests added."""
    added = 0
    columns_by_name = {c["name"]: c for c in columns}
    for uk in (class_def.unique_keys or {}).values():
        uk_slots = list(uk.unique_key_slots)
        if set(uk_slots) == set(pk_names):
            continue  # already unique via the PK
        if len(uk_slots) == 1:
            col = columns_by_name.get(uk_slots[0])
            if col is not None and "unique" not in col.get("tests", []):
                col.setdefault("tests", []).append("unique")
                added += 1
    return added


def generate_dbt_sources(
    linkml_schema_path: str,
    source_name: str = "dev_include_access",
    source_description: str = "Database schema containing access policy data.",
    include_abstract: bool = False,
    composite_key_tests: bool = True,
) -> dict[str, Any]:
    # 1. Load the LinkML schema and run it through the same relational
    #    transform LinkML's SQL DDL generator uses, so what we describe
    #    here matches the actual tables the database will have -- including
    #    linking tables for multivalued slots that don't exist as classes
    #    anywhere in the LinkML schema itself.
    original_view = SchemaView(linkml_schema_path)
    tr_result = RelationalModelTransformer(original_view).transform()
    rel_schema = tr_result.schema
    view = SchemaView(rel_schema)

    all_classes: dict[str, ClassDefinition] = rel_schema.classes

    concrete_classes = {
        cname: cdef
        for cname, cdef in all_classes.items()
        if include_abstract or not (cdef.mixin or cdef.abstract)
    }
    class_to_table = {cname: to_snake_case(cname) for cname in concrete_classes}

    # 2. Structure the core dbt source wrapper
    dbt_config: dict[str, Any] = {
        "version": 2,
        "sources": [
            {
                "name": source_name,
                "description": source_description,
                "tables": [],
            }
        ],
    }

    table_count = 0
    column_count = 0
    test_count = 0

    # 3. Pull tables/columns from the transformed relational schema
    for class_name, class_def in concrete_classes.items():
        table_name = class_to_table[class_name]
        attrs: dict[str, SlotDefinition] = class_def.attributes

        pk_names = [str(sn) for sn, s in attrs.items() if is_primary_key_slot(s)]

        description = str(class_def.description) if class_def.description else None
        if description is None:
            backref = next(
                (s for s in attrs.values() if annotation_value(s, "backref") == "true"),
                None,
            )
            if backref is not None:
                description = (
                    f"Linking table generated for a multivalued slot on "
                    f"{backref.range}."
                )
            else:
                description = f"Table for {class_name}"

        table_info: dict[str, Any] = {
            "name": table_name,
            "description": description,
            "columns": [],
        }

        for slot_name, slot in attrs.items():
            column_info: dict[str, Any] = {
                "name": f'"{slot_name!s}"',
                "description": str(slot.description) if slot.description else "",
            }

            tests = build_column_tests(
                slot, pk_names, view, class_to_table, source_name
            )
            if tests:
                column_info["tests"] = tests
                test_count += len(tests)

            table_info["columns"].append(column_info)
            column_count += 1

        test_count += apply_single_slot_unique_keys(
            class_def, pk_names, table_info["columns"]
        )

        table_tests = build_table_tests(class_def, pk_names, composite_key_tests)
        if table_tests:
            table_info["tests"] = table_tests
            test_count += len(table_tests)

        dbt_config["sources"][0]["tables"].append(table_info)
        table_count += 1

    logger.info(
        "Generated %d tables, %d columns, %d tests from %s",
        table_count,
        column_count,
        test_count,
        linkml_schema_path,
    )

    return dbt_config


def resolve_default_schema_path() -> Path:
    """Auto-detect src/*/schema/*.yaml, matching the original script's behavior."""
    schema_dirs = list(Path(".").glob("src/*/schema"))
    if not schema_dirs:
        raise FileNotFoundError(
            "Could not auto-detect a LinkML schema under src/*/schema/. "
            "Pass --schema explicitly."
        )
    model_name = schema_dirs[0].parent.stem
    return Path(f"src/{model_name}/schema/{model_name}.yaml")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Path to the LinkML schema YAML. Auto-detected from "
        "src/*/schema/*.yaml if omitted.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("project/dbt/src_dev_include_access.yml"),
        help="Path to write the generated dbt sources YAML file.",
    )
    parser.add_argument(
        "--source-name",
        default="dev_include_access",
        help="dbt source name to use in the generated file.",
    )
    parser.add_argument(
        "--source-description",
        default="Database schema containing access policy data.",
        help="dbt source description to use in the generated file.",
    )
    parser.add_argument(
        "--include-abstract-tables",
        action="store_true",
        help="Include LinkML abstract/mixin classes as dbt source tables. "
        "Off by default, matching the assumption that abstract/mixin "
        "classes aren't real database tables.",
    )
    parser.add_argument(
        "--no-composite-key-tests",
        dest="composite_key_tests",
        action="store_false",
        help="Omit dbt_utils.unique_combination_of_columns tests for "
        "composite primary keys and multi-slot unique_keys. Use this if "
        "your dbt project doesn't have the dbt_utils package installed.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        schema_path = args.schema or resolve_default_schema_path()
        if not schema_path.exists():
            raise FileNotFoundError(f"LinkML schema not found: {schema_path}")

        config_dict = generate_dbt_sources(
            str(schema_path),
            source_name=args.source_name,
            source_description=args.source_description,
            include_abstract=args.include_abstract_tables,
            composite_key_tests=args.composite_key_tests,
        )

        args.output.parent.mkdir(exist_ok=True, parents=True)
        with args.output.open("w") as f:
            # sort_keys=False preserves the version -> sources hierarchy
            yaml.dump(
                config_dict, f, sort_keys=False, default_flow_style=False, width=512
            )

        logger.info("Successfully generated dbt sources file at %s", args.output)
        return 0

    except Exception as exc:  # noqa: BLE001 - surface any failure clearly to CI
        logger.error("Failed to generate dbt sources file: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
