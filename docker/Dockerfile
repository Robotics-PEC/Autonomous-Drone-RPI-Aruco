# Base image with Ubuntu
FROM ubuntu:22.04

# Avoid prompts from tzdata, etc.
ENV DEBIAN_FRONTEND=noninteractive

# Install required tools and dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    wget \
    curl \
    lsb-release \
    && apt-get clean

# Create user and add to sudo group
RUN useradd -m -s /bin/bash px4user && \
    echo "px4user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    usermod -aG sudo px4user

USER px4user
WORKDIR /home/px4user

# Clone PX4 Firmware
RUN git clone https://github.com/PX4/PX4-Autopilot.git --recursive --depth=1

# Go into firmware and run the setup script
WORKDIR /home/px4user/PX4-Autopilot

# Install PX4 dependencies (script installs more via apt and pip)
RUN ./Tools/setup/ubuntu.sh --no-nuttx

# Set up environment
ENV PATH="/home/px4user/.local/bin:$PATH"

# Build SITL (you can change jmavsim to gazebo if preferred)
RUN make px4_sitl_default

# Entry point to run PX4 SITL
CMD ["make","px4_sitl", "gz_x500_mono_cam_down"]
