FROM ghcr.io/organicveggie/docker-ansible:py3.14-bookworm-latest

# Create a non-root user with UID 1100 and GID 1100
ARG USERNAME=vscode
ARG USER_UID=1100
ARG USER_GID=$USER_UID

# Set build-time argument for build version, with a default value
ARG IMAGE_BUILD_VERSION=v0.0.0-unknown
ENV IMAGE_BUILD_VERSION=${IMAGE_BUILD_VERSION}

# Setup the devcontainer user and permissions
RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends sudo

# Create the devcontainer user and add to sudoers
groupadd --gid $USER_GID $USERNAME 
useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME 
chmod 0440 /etc/sudoers.d/$USERNAME

# Ensure bash is set as the default shell for the devcontainer user
chsh -s /bin/bash $USERNAME
RUN_CMD_EOF

# Install Docker CLI and other necessary tools
RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        gnupg \
        libonig-dev \
        openssh-client \
        rsync \
        vim

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

apt-get update
apt-get install -y --no-install-recommends docker-ce-cli

# Clean up APT cache to reduce image size
rm -fR /var/lib/apt/lists/*
rm -fR /usr/share/doc
rm -fR /usr/share/man
RUN_CMD_EOF

# Set the active user for subsequent commands
USER $USERNAME

RUN --mount=type=bind,source=images/requirements.txt,target=/tmp/requirements.txt <<PIP_INSTALL_EOF
pip3 install --no-cache-dir --upgrade pip
pip3 install --no-cache-dir -r /tmp/requirements.txt
PIP_INSTALL_EOF

LABEL org.opencontainers.image.title="organicveggie/ansible-devcontainer" \
    org.opencontainers.image.description="debian Ansible development container" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/ansible-devcontainer"

WORKDIR /workspace