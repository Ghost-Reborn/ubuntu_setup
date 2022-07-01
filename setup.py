import os

# update and upgrade
os.system('sudo apt update')
os.system('sudo apt upgrade -y')

# Repo tool
os.system('sudo apt install python -y')
os.system('mkdir -p ~/.bin')
os.system('PATH="${HOME}/.bin:${PATH}"')
os.system('curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo')
os.system('chmod a+rx ~/.bin/repo')

# AOSP Specific
os.system('sudo apt install \
    git-core \
    gnupg \
    flex \
    bison \
    build-essential \
    zip \
    curl \
    zlib1g-dev \
    gcc-multilib \
    g++-multilib \
    libc6-dev-i386 \
    libncurses5 \
    lib32ncurses5-dev \
    x11proto-core-dev \
    libx11-dev \
    lib32z1-dev \
    libgl1-mesa-dev \
    libxml2-utils \
    xsltproc \
    unzip \
    fontconfig \
    -y')