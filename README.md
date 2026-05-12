<div align="center">

# Ansible Dev Container

[![Build Status](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml/badge.svg)](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml) [![License](https://img.shields.io/github/license/organicveggie/ansible-devcontainer)](https://github.com/organicveggie/ansible-devcontainer/blob/master/LICENSE) [![Docker](https://ghcr-badge.egpl.dev/organicveggie/ansible-devcontainer/tags?label=ghcr.io&trim=major)](https://github.com/organicveggie/ansible-devcontainer/pkgs/container/ansible-devcontainer)

**A container image for Ansible Development Tools (ADT).**

</div>

---

This image is built on top of [python:3.13-slim-bookworm](https://hub.docker.com/_/python) and has container-outside-container support with [`Docker`](https://www.docker.com/).

More details on ADT can be found in <https://ansible.readthedocs.io/projects/dev-tools/>.

## Installation

```bash
docker pull ghcr.io/organicveggie/ansible-devcontainer:latest
```

## Usage

### Using this as a VS Code Dev Container

Dev Containers provide you with a containerized development environment in VS code. Details on what they are and how to use them can be found in [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers).

This image can be used as an image for a Dev Container where you build and consume Ansible content.

This repository comes with a sample [`.devcontainer directory`](https://github.com/organicveggie/ansible-devcontainer/tree/main/.devcontainer) with a `devcontainer.json` file.

You can simply copy over the `.devcontainer` directory to your Ansible project and start using it!

## Related Links

- [adt](https://github.com/ansible/ansible-dev-tools)
- [ansible-builder](https://github.com/ansible/ansible-builder)
- [ansible-creator](https://github.com/ansible/ansible-creator)

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
