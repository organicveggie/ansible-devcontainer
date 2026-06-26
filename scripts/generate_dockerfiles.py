#!/usr/bin/env python3

from enum import StrEnum
from dataclasses import dataclass
from pathlib import Path

from combos import OS_DEFAULT_PYTHON_VERSION, all_combos
from jinja2 import Environment, FileSystemLoader

PYTHON_VERSIONS: list[str] = ["3.12", "3.13", "3.14"]

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
TEMPLATE_PATH = IMAGES_DIR / "Dockerfile.j2"


def generate() -> None:
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_PATH.parent)))
    template = env.get_template(TEMPLATE_PATH.name)

    for combo in all_combos():
        out_dir = (
            IMAGES_DIR / combo.python / combo.os_name.value / combo.os_release.value
        )
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "Dockerfile"

        out_path.write_text(
            template.render(
                python_version=combo.python,
                os_name=combo.os_name.value,
                os_release=combo.os_release.value,
                os_default_python=OS_DEFAULT_PYTHON_VERSION[combo.os_release],
            )
        )

        print(
            f"wrote {out_path.relative_to(REPO_ROOT)} from {TEMPLATE_PATH.relative_to(REPO_ROOT)}"
        )


def main() -> None:
    generate()


if __name__ == "__main__":
    main()
