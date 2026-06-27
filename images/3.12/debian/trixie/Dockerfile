FROM ghcr.io/organicveggie/docker-ansible:py3.12-trixie-latest

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
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        dirmngr \
        git \
        gnupg \
        gnupg2 \
        libonig-dev \
        openssh-client \
        rsync \
        vim \
        wget

# Source /etc/os-release to get OS info
. /etc/os-release

# Fetch host/container arch.
architecture="$(dpkg --print-architecture)"

install -m 0755 -d /etc/apt/keyrings

 # Import key safely and import Docker apt repo
curl -fsSL https://download.docker.com/linux/${ID}/gpg | gpg --dearmor > /usr/share/keyrings/docker-archive-keyring.gpg

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.list <<EOF
Types: deb
URIs: https://download.docker.com/linux/${ID}
Architectures: ${architecture}
Suites: ${VERSION_CODENAME}
Components: stable
Signed-By: /usr/share/keyrings/docker-archive-keyring.gpg
EOF

apt-get update
apt-get install -y --no-install-recommends docker-ce-cli

# Remove useless Python environment warning flag.
find /usr -type f -name "EXTERNALLY-MANAGED" -print0 |xargs -0 rm -f 

# Clean up APT cache to reduce image size
rm -fR /var/lib/apt/lists/*
rm -fR /usr/share/doc
rm -fR /usr/share/man
RUN_CMD_EOF

# Set the active user for subsequent commands
USER $USERNAME

RUN --mount=type=bind,source=images/requirements.txt,target=/tmp/requirements.txt <<PIP_INSTALL_EOF
PIP="/usr/bin/pip3"
if [ -f "/usr/local/bin/pip3" ] ; then
    PIP="/usr/local/bin/pip3"
fi
${PIP} install --no-cache-dir -r /tmp/requirements.txt
PIP_INSTALL_EOF

LABEL org.opencontainers.image.title="organicveggie/ansible-devcontainer" \
    org.opencontainers.image.description="debian Ansible development container" \
    org.opencontainers.image.version="${IMAGE_BUILD_VERSION}" \
    org.opencontainers.image.licenses="GPL-3.0-or-later" \
    org.opencontainers.image.source="https://github.com/organicveggie/ansible-devcontainer"

WORKDIR /workspace