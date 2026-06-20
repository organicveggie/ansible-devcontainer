FROM python:3.14-trixie

# Create a non-root user with UID 1000 and GID 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN <<RUN_CMD_EOF
apt-get update
apt-get install -y --no-install-recommends \
        build-essential \
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
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian trixie stable" \
       > /etc/apt/sources.list.d/docker.list

apt-get update
apt-get install -y --no-install-recommends docker-ce-cli
rm -rf /var/lib/apt/lists/*

groupadd --gid $USER_GID $USERNAME 
useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME 
chmod 0440 /etc/sudoers.d/$USERNAME
RUN_CMD_EOF

# Set the active user for subsequent commands (like installing global tools)
USER $USERNAME

COPY image/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /workspace
