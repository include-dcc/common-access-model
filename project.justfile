## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540
[group('model development')]
_gen_sqla:
    mkdir -p {{dest}}/sqlalchemy && \
    uv run gen-sqla {{source_schema_path}} --declarative > {{dest}}/sqlalchemy/{{schema_name}}.py


_gen-linkml:
  -mkdir -p docs/schema
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -f yaml {{source_schema_path}} > {{dest}}/linkml/{{schema_name}}.yaml
