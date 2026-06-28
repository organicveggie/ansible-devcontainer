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
