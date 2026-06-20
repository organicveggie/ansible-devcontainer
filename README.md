<div align="center">

# Ansible Dev Container

[![Build Status](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml/badge.svg)](https://github.com/organicveggie/ansible-devcontainer/actions/workflows/docker.yml) [![License](https://img.shields.io/github/license/organicveggie/ansible-devcontainer)](https://github.com/organicveggie/ansible-devcontainer/blob/master/LICENSE) [![Docker](https://ghcr-badge.egpl.dev/organicveggie/ansible-devcontainer/tags?label=ghcr.io&trim=major)](https://github.com/organicveggie/ansible-devcontainer/pkgs/container/ansible-devcontainer)

**A container image for Ansible Development Tools (ADT).**

</div>

---

These images are built on top of [python:3.14, python:3.13, python:3.12, python:3.11](https://hub.docker.com/_/python) and have container-outside-container support with [`Docker`](https://www.docker.com/).

More details on ADT can be found in <https://ansible.readthedocs.io/projects/dev-tools/>.

## Supported Tags

* [3.1-trixe-py3.14, 3-trixie-py3.14, 3.1-py3.14, 3-py3.14, 3.1-trixe, 3-trixie, 3.1, 3, latest](https://github.com/organicveggie/ansible-devcontainer/blob/main/image/trixie/3.14/Dockerfile)
* [3.1-trixe-py3.13, 3-trixie-py3.13, 3.1-py3.13, 3-py3.13](https://github.com/organicveggie/ansible-devcontainer/blob/main/image/trixie/3.13/Dockerfile)
* [3.1-trixe-py3.12, 3-trixie-py3.12, 3.1-py3.12, 3-py3.12](https://github.com/organicveggie/ansible-devcontainer/blob/main/image/trixie/3.12/Dockerfile)
* [3.1-bookworm-py3.14, 3-bookworm-py3.14, 3.1-bookworm, 3-bookworm]((https://github.com/organicveggie/ansible-devcontainer/blob/main/image/bookworm/3.14/Dockerfile))
* [3.1-bookworm-py3.13, 3-bookworm-py3.13]((https://github.com/organicveggie/ansible-devcontainer/blob/main/image/bookworm/3.13/Dockerfile))
* [3.1-bookworm-py3.12, 3-bookworm-py3.12]((https://github.com/organicveggie/ansible-devcontainer/blob/main/image/bookworm/3.12/Dockerfile))

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

**NOTE**: If you are using this image with Molecule and the [geerlingguy/docker-ubuntu2404-ansible](https://github.com/geerlingguy/docker-ubuntu2404-ansible) image, you need to pick an image with the same major/minor version of Python as the geerlingguy image.

### Trixie

Trixie does not include the `moby-cli` packages, so you have to explicitly disable them in the `docker-outside-of-docker` feature in `devcontainer.json`:

```json
  "features": {
    "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {
      "version": "latest",
      "enableNonRootDocker": "true",
      "moby": false
    }
  }
```

Or use the `bookworm` release instead.

## Related Links

- [adt](https://github.com/ansible/ansible-dev-tools)
- [ansible-builder](https://github.com/ansible/ansible-builder)
- [ansible-creator](https://github.com/ansible/ansible-creator)

## License

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
