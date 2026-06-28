<div align="center">

# Ansible Dev Container

[![Build Status](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml/badge.svg)](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml) [![License](https://img.shields.io/github/license/organicveggie/ansible-devcontainer)](https://github.com/organicveggie/ansible-devcontainer/blob/master/LICENSE)

**A devcontainer image for Ansible Development Tools (ADT).**

</div>

---

These images are built on top of [python:3.14, python:3.13, python:3.12](https://hub.docker.com/_/python), include the latest release of Ansible, and have [`Docker`](https://www.docker.com/) container-outside-container support.

More details on ADT can be found in <https://ansible.readthedocs.io/projects/dev-tools/>.

# Container Images

## Support Matrix

* **Python:** `3.12`, `3.13`, `3.14`
* **OS:**
  * **Debian:** `Bookworm`, `Trixie`
  * **Ubuntu:** `24.04`, `25.10`, `26.04`
* **Architectures:** ([more info](https://github.com/docker-library/official-images#architectures-other-than-amd64))
  * `amd64`, `arm64v8`

## Tags

<!--
Regenerated automatically by `scripts/update_readme_tags.py` whenever a `vX.Y.Z` tag is pushed — do not hand-edit between the markers.
-->

<!-- TAGS:START -->
| Python | OS     | Release  | Tags |
|:------ | ------ | -------- | ---- |
| 3.12   | Debian | Bookworm    | [`5.1.3-py3.12-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/bookworm/Dockerfile), [`5.1-py3.12-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/bookworm/Dockerfile), [`5-py3.12-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/bookworm/Dockerfile), [`py3.12-bookworm-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/bookworm/Dockerfile) |
| 3.12   | Debian | Trixie    | [`5.1.3-py3.12-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/trixie/Dockerfile), [`5.1-py3.12-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/trixie/Dockerfile), [`5-py3.12-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/trixie/Dockerfile), [`py3.12-trixie-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/debian/trixie/Dockerfile) |
| 3.12   | Ubuntu | 24.04    | [`5.1.3-py3.12-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`5.1-py3.12-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`5-py3.12-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`py3.12-24.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`5.1.3-py3.12-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`5.1-py3.12-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`5-py3.12-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile), [`py3.12-noble-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/24.04/Dockerfile) |
| 3.12   | Ubuntu | 25.10    | [`5.1.3-py3.12-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`5.1-py3.12-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`5-py3.12-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`py3.12-25.10-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`5.1.3-py3.12-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`5.1-py3.12-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`5-py3.12-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile), [`py3.12-questing-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/25.10/Dockerfile) |
| 3.12   | Ubuntu | 26.04    | [`5.1.3-py3.12-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`5.1-py3.12-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`5-py3.12-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`py3.12-26.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`5.1.3-py3.12-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`5.1-py3.12-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`5-py3.12-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile), [`py3.12-resolute-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.12/ubuntu/26.04/Dockerfile) |
| 3.13   | Debian | Bookworm    | [`5.1.3-py3.13-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/bookworm/Dockerfile), [`5.1-py3.13-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/bookworm/Dockerfile), [`5-py3.13-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/bookworm/Dockerfile), [`py3.13-bookworm-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/bookworm/Dockerfile) |
| 3.13   | Debian | Trixie    | [`5.1.3-py3.13-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/trixie/Dockerfile), [`5.1-py3.13-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/trixie/Dockerfile), [`5-py3.13-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/trixie/Dockerfile), [`py3.13-trixie-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/debian/trixie/Dockerfile) |
| 3.13   | Ubuntu | 24.04    | [`5.1.3-py3.13-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`5.1-py3.13-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`5-py3.13-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`py3.13-24.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`5.1.3-py3.13-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`5.1-py3.13-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`5-py3.13-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile), [`py3.13-noble-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/24.04/Dockerfile) |
| 3.13   | Ubuntu | 25.10    | [`5.1.3-py3.13-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`5.1-py3.13-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`5-py3.13-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`py3.13-25.10-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`5.1.3-py3.13-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`5.1-py3.13-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`5-py3.13-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile), [`py3.13-questing-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/25.10/Dockerfile) |
| 3.13   | Ubuntu | 26.04    | [`5.1.3-py3.13-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`5.1-py3.13-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`5-py3.13-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`py3.13-26.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`5.1.3-py3.13-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`5.1-py3.13-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`5-py3.13-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile), [`py3.13-resolute-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.13/ubuntu/26.04/Dockerfile) |
| 3.14   | Debian | Bookworm    | [`5.1.3-py3.14-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/bookworm/Dockerfile), [`5.1-py3.14-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/bookworm/Dockerfile), [`5-py3.14-bookworm`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/bookworm/Dockerfile), [`py3.14-bookworm-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/bookworm/Dockerfile) |
| 3.14   | Debian | Trixie    | [`5.1.3-py3.14-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`5.1-py3.14-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`5-py3.14-trixie`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`py3.14-trixie-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`5.1.3`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`5.1`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`5`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile), [`latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/debian/trixie/Dockerfile) |
| 3.14   | Ubuntu | 24.04    | [`5.1.3-py3.14-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`5.1-py3.14-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`5-py3.14-24.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`py3.14-24.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`5.1.3-py3.14-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`5.1-py3.14-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`5-py3.14-noble`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile), [`py3.14-noble-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/24.04/Dockerfile) |
| 3.14   | Ubuntu | 25.10    | [`5.1.3-py3.14-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`5.1-py3.14-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`5-py3.14-25.10`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`py3.14-25.10-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`5.1.3-py3.14-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`5.1-py3.14-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`5-py3.14-questing`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile), [`py3.14-questing-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/25.10/Dockerfile) |
| 3.14   | Ubuntu | 26.04    | [`5.1.3-py3.14-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`5.1-py3.14-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`5-py3.14-26.04`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`py3.14-26.04-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`5.1.3-py3.14-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`5.1-py3.14-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`5-py3.14-resolute`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile), [`py3.14-resolute-latest`](https://github.com/organicveggie/ansible-devcontainer/blob/main/images/3.14/ubuntu/26.04/Dockerfile) |
<!-- TAGS:END -->

# Usage

## Using this as a VS Code Dev Container

Dev Containers provide you with a containerized development environment in VS code. Details on what they are and how to use them can be found in [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers).

This image can be used as an image for a Dev Container where you build and consume Ansible content.

This repository comes with a sample [`.devcontainer directory`](https://github.com/organicveggie/ansible-devcontainer/tree/main/.devcontainer) with a `devcontainer.json` file.

You can simply copy over the `.devcontainer` directory to your Ansible project and start using it!

**NOTE**: If you are using this image with Molecule and the [geerlingguy/docker-ubuntu2404-ansible](https://github.com/geerlingguy/docker-ubuntu2404-ansible) image, you should to pick an image with the same major/minor version of Python as the geerlingguy image.

## Resolute and Trixie

Debian Trixie and Ubuntu Resolute do not include the `moby-cli` packages, so you have to explicitly disable them in the `docker-outside-of-docker` feature in `devcontainer.json`:

```json
  "features": {
    "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {
      "version": "latest",
      "enableNonRootDocker": "true",
      "moby": false
    }
  }
```

## Related Links

- [adt](https://github.com/ansible/ansible-dev-tools)
- [ansible-builder](https://github.com/ansible/ansible-builder)
- [ansible-creator](https://github.com/ansible/ansible-creator)

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
