import shutil
import subprocess
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python 3.9 / 3.10

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        root = Path(self.root)

        with open(root / "pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
        schema_name = pyproject["project"]["name"]

        source_schema_path = (
            root / "src" / schema_name / "schema" / f"{schema_name}.yaml"
        )

        # Generate directly into the package dir - this gets included in the
        # sdist naturally and is present when hatchling builds the wheel
        pkg_dir = root / schema_name
        pkg_dir.mkdir(parents=True, exist_ok=True)
        dest_file = pkg_dir / f"{schema_name}.py"

        if not dest_file.exists():
            gen_sqla = root / ".venv" / "bin" / "gen-sqla"
            if not gen_sqla.exists():
                found = shutil.which("gen-sqla")
                if not found:
                    raise RuntimeError(
                        "gen-sqla not found. Run `uv sync --group dev` first, "
                        "or run `just _gen_sqla` before `uv build`."
                    )
                gen_sqla = Path(found)

            with open(dest_file, "w") as out:
                subprocess.run(
                    [str(gen_sqla), str(source_schema_path), "--declarative"],
                    stdout=out,
                    check=True,
                )

        # Also copy to project/sqlalchemy/ for consistency with just site output
        sqla_dir = root / "project" / "sqlalchemy"
        sqla_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(dest_file, sqla_dir / f"{schema_name}.py")

        build_data["shared_data"] = {}
        build_data["packages"] = [schema_name]
        build_data["include"] = [f"{schema_name}/*.csv", f"{schema_name}/*.py"]
        build_data["artifacts"].append(str(dest_file))
        build_data["force_include"][str(dest_file)] = f"{schema_name}/{schema_name}.py"

        # Bundle harmony CSVs if present
        harmony_src = root / "project" / "harmony"
        if harmony_src.exists():
            for csv_file in harmony_src.glob("*.csv"):
                dest_csv = pkg_dir / csv_file.name
                shutil.copy(csv_file, dest_csv)
                build_data["artifacts"].append(str(dest_csv))
                build_data["force_include"][str(dest_csv)] = (
                    f"{schema_name}/{csv_file.name}"
                )
