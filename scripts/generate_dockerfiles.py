#!/usr/bin/env python3

from enum import StrEnum
from dataclasses import dataclass
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class OSName(StrEnum):
    DEBIAN = "debian"
    UBUNTU = "ubuntu"


class OSRelease(StrEnum):
    BOOKWORM = "bookworm"
    TRIXIE = "trixie"
    NOBLE = "24.04"
    QUESTING = "25.10"
    RESOLUTE = "26.04"


OS_RELEASE_ALIAS: dict[OSRelease, str | None] = {
    OSRelease.BOOKWORM: None,
    OSRelease.TRIXIE: None,
    OSRelease.NOBLE: "noble",
    OSRelease.QUESTING: "questing",
    OSRelease.RESOLUTE: "resolute",
}

OS_RELEASE_MAP: dict[OSRelease, OSName] = {
    OSRelease.BOOKWORM: OSName.DEBIAN,
    OSRelease.TRIXIE: OSName.DEBIAN,
    OSRelease.NOBLE: OSName.UBUNTU,
    OSRelease.QUESTING: OSName.UBUNTU,
    OSRelease.RESOLUTE: OSName.UBUNTU,
}

OS_RELEASES: list[OSRelease] = [
    OSRelease.BOOKWORM,
    OSRelease.TRIXIE,
    OSRelease.NOBLE,
    OSRelease.QUESTING,
    OSRelease.RESOLUTE,
]

PYTHON_VERSIONS: list[str] = ["3.12", "3.13", "3.14"]

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "images"
TEMPLATE_PATH = IMAGES_DIR / "Dockerfile.j2"


@dataclass(frozen=True)
class Combo:
    python: str
    os_release: OSRelease

    @property
    def os_name(self) -> OSName:
        return OS_RELEASE_MAP[self.os_release]

    @property
    def alias(self) -> str | None:
        return OS_RELEASE_ALIAS[self.os_release]


def all_combos() -> list[Combo]:
    return [
        Combo(python=python, os_release=os_release)
        for python in PYTHON_VERSIONS
        for os_release in OS_RELEASES
    ]


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
            )
        )

        print(
            f"wrote {out_path.relative_to(REPO_ROOT)} from {TEMPLATE_PATH.relative_to(REPO_ROOT)}"
        )


def main() -> None:
    generate()


if __name__ == "__main__":
    main()
