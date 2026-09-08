## Welcome to the Common Access Model 🚀

This repository represents the core model, Common Access Model (CAM). In order
to allow downstream models to extend a common set of classes and their
properties, those models should adhere to use this model as a Git submodule.

## Key Integration Guidelines

All changes to this model should be made with the understanding that those
changes are completely valid for all or many of the downstream models. Those
changes should be made directly within this repository and not as changes to the
versions from the submodules themselves.

Please see the following notes when integrating this model as a submodule within
one of the downtream modules:

- Do Not Modify the Submodule from within this repository: All foundational
  classes, slots, and enums live in the core submodule. Any program-specific
  customizations must happen strictly in your downstream files.
- Leverage Imports: At this time, the current model imports the
  common_access_model.yaml directly within the main model definition.
- Extend via Inheritance: Use the is_a or mixins keys to create program-specific
  subclasses that inherit core slots while allowing you to add local attributes.
- Refine via Slot Usage: If you need to restrict or change the behavior of an
  inherited core slot just for your program's classes, use the slot_usage
  feature.

## Getting Started

If you aren't already familiar with working with submodules, there are just a
couple of key takeaways to keep in mind:

- The submodule has been pinned to a specific git commit hash to avoid
  unexpected changes the CAM creeping into downstream model interfering with
  local builds, CI/CD scripts, etc.
- The submodule itself should only be updated by deliberate action with the
  expectation that downstream model changes may be required to reflect incoming
  updates.

### Initializing the submodule

Before you can actually compile the model on a new machine, you'll need to pull
the submodule's content down. A convenient just recipe has been created for
exactly that:

```bash
just init-submodule
```

or, if you prefer to do it directly yourself:

```bash
git submodule update --init --recursive
# make sure nothing is broken
just lint && just test
```

Subsequent calls can drop the init if you know for a fact that no other
submodules have been added. The just recipe does call the linter and runs the
linkml test as a subsequent dependency, in case there are upstream changes that
invalidate the downstream model.

### Updating the pinned hash

Once it has been decided that it is time to update the CAM to use the latest
version, the maintainer should run the following commands to fetch, test and
lock the new version into the downstream model's main.

```bash
# Navigate into the submodule directory
cd src/kf_access_model/schema/common_access_model

# Fetch and check out the desired remote target (e.g., main branch)
git fetch origin
git checkout origin/main

# Move back to the repository root
cd -

# Run linter and tests
just lint && just test


# Commit the new submodule hash pointer to this repository
git add src/kf_access_model/schema/common_access_model
git commit -m "chore: update common_access_model submodule to latest hash"
```

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

This has also been added as a dependency to the recipes _test-schema and lint, and will automatically be run with `just test` and `just lint`.

#### Regenerate expanded output
Enums that already have a `permissible_values` will not be expanded.
To rerun the expansion script on a file, delete the current `permissible_values` from the YAML file, then run `just expand`, `just _test`, or `just lint`.

The `permissible_values` for any given enum can be deleted manually or by running the following command for each file:

`just clear {file_name}`

Example:

`just clear EnumName`
