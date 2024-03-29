FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
        python3-pip \
        python3-mock \
        libpython3-all-dev \
        python-is-python3 \
        pkg-config \
        software-properties-common \
        nano \
        sudo \
        libgl1-mesa-dev \
        libsm6 \
        libxext6 \
        libxrender-dev \
    && sed -i 's/# set linenumbers/set linenumbers/g' /etc/nanorc \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pip -U \
    && pip install mediapipe --no-deps \
    && pip install opencv-python \
    && pip install --upgrade attrs

ENV USERNAME=user
RUN echo "root:root" | chpasswd \
    && adduser --disabled-password --gecos "" "${USERNAME}" \
    && echo "${USERNAME}:${USERNAME}" | chpasswd \
    && echo "%${USERNAME}    ALL=(ALL)   NOPASSWD:    ALL" >> /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}
USER ${USERNAME}
ARG WKDIR=/home/${USERNAME}/workdir
WORKDIR ${WKDIR}
RUN sudo chown ${USERNAME}:${USERNAME} ${WKDIR}
RUN echo 'export QT_X11_NO_MITSHM=1' >> ${HOME}/.bashrc
RUN echo 'sudo chmod 776 /dev/video*' >> ${HOME}/.bashrc
