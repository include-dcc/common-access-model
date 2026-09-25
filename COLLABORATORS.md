## Welcome to the Common Access Model 🚀

This repository represents the core model, Common Access Model (CAM). In order
to allow downstream models to extend a common set of classes and their
properties, those models should adhere to use this model as a Git submodule.

## Key Integration Guidelines

The classes and slots defined herein are shared across all downstream models. As
such, changes required to satisfy a downstream model's requirements should be
contained solely within the downstream model itself, or updated here with the
understanding that those changes will make their way to all of the other
downstream models in time.

Downstream model development guidance:

- Leverage Imports: At this time, the downstream model imports the
  common_access_model-{version}.yaml directly within the main model definition.
- Extend via Inheritance: Use the is_a or mixins keys to create program-specific
  subclasses that inherit core slots while allowing you to add local attributes.
- Refine via Slot Usage: If you need to restrict or change the behavior of an
  inherited core slot just for your program's classes, use the slot_usage
  feature.

## Getting Started

When you initialized your working environment using 'just install', a pre-commit
hook should have been installed for you that will apply various style fixes
before each commit. In general, only the files being committed are tested.

For those whose local copies of the model predate this change, you may simply
run the following just recipe to hook the pre-commit runs into your local clone.
Please note that this must be run again if you ever pull the code down into a
new directory.

```bash
just precommit
```

### Updating (and initializing) the Common Access Model

To incorporate the Common Access Model into a downstream model, either for the
first time or to update to a newer version, a just recipe has been provided:

```bash
just update-cam
```

This will download the latest version of the common access model to
src/{model_name}/upstream-models/. The resulting file will be a complete
monolithic copy of the common access model with the version as part of the name.
It is up to the user to update the downstream model to include the updated CAM
model file.

This file is tracked in github, so once the newest version is correctly checked
in, other contributors will pick up the correct version directly from their git
pulls.

## Release Artifacts

There are a number of artifacts which are used by various scripts including the
dbt utilities which are built via github actions during release. To trigger the
build, create releases linked to a semantic version preceded with a v (i.e.
v1.0.1).

These artifacts include:

- SQL Alchemy model
- dbt model yml file
- SQL Schema
- data dictionary conformant to the current FTD spec
- enumerations csv file extracted from all of the permissible values

The last two are used by this group's dbt utilities tooling. The SQL Alchemy
model is used by a handful of other scripts.

## Beautification

### Code Quality & Formatting with pre-commit

We use `pre-commit` to catch minor issues automatically before your changes
reach code review. This saves you time by automating formatting and linting
tasks, allowing code reviews to focus strictly on functionality and logic rather
than style choices.

The hooks automatically run the following optimizations when you execute a
`git commit`:

- **Formatting:** Standardizes Python code via **Ruff** and YAML configurations
  via **Prettier** (matching the default styling behavior of editors like Zed).
- **Linting:** Analyzes code patterns and auto-fixes formatting anomalies on the
  fly.
- **Checks:** Verifies structural syntax sanity for TOML/YAML layouts, removes
  trailing whitespace, and forces trailing newlines.

#### Getting Started (First-Time Setup)

If you are setting up the repository for the first time, you don't even need to
install `pre-commit` globally on your system. You can handle everything through
**`uv`**:

1. **Register the Git hook scripts** inside the local `.git/` directory using
   `uv run`:
   ```bash
   uv run pre-commit install
   ```

---

#### Subsequent Uses & Everyday Workflow

Once registered, the tool seamlessly hooks into your normal Git workflow without
any manual intervention:

- **Automatic Execution:** Every time you run `git commit`, the hooks
  automatically run against your _staged changes_. `uv` will transparently
  manage the tool environments in the background.
- **If a hook modifies a file (or fails):** The commit is safely aborted so you
  can inspect the adjustments. Simply stage the updated files (`git add .`) and
  run your `git commit` command again.
- **Manual Repository Check:** If you ever want to force formatting across the
  entire repository manually without creating a commit, run:
  ```bash
  uv run pre-commit run --all-files
  ```

## Commands to Expand Enum Files

### To write the expanded output:

`just expand`

This has also been added as a dependency to the recipes _test-schema and lint,
and will automatically be run with `just test` and `just lint`.

#### Regenerate expanded output

Enums that already have a `permissible_values` will not be expanded. To rerun
the expansion script on a file, delete the current `permissible_values` from the
YAML file, then run `just expand`, `just _test`, or `just lint`.

The `permissible_values` for any given enum can be deleted manually or by
running the following command for each file:

`just clear {file_name}`

Example:

`just clear EnumName`
