FROM ubuntu:latest

RUN apt update
RUN apt -y install cron nano python3 python3-pip software-properties-common
RUN add-apt-repository -y ppa:mozillateam/ppa
RUN echo '\nPackage: *\nPin: release o=LP-PPA-mozillateam\nPin-Priority: 1001\n' | tee /etc/apt/preferences.d/mozilla-firefox
RUN apt install -y firefox
RUN echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox

ARG cronSettings=""
ENV cronSettings=$cronSettings

ENV workdir="PolitoMaterialDownload"

WORKDIR /${workdir}

COPY . /${workdir}/

RUN rm -r ./docker

RUN pip3 install -r requirements.txt

COPY ./docker/docker_run_cron.sh /pmdUtils/start.sh

RUN ls -la /pmdUtils | echo;

CMD bash /pmdUtils/start.sh
