FROM ubuntu:latest

#packages
RUN apt-get update && apt-get install -y --no-install-recommends wget sudo ca-certificates gnupg\
	apt-transport-https x11-xserver-utils dirmngr gnupg-l10n alsa-utils libasound2\
	libasound2-plugins pulseaudio pulseaudio-utils libcanberra-gtk-module software-properties-common\
	python3 gcc libnss3 libxss1 fonts-liberation libappindicator3-1 libatk-bridge2.0-0 libatspi2.0-0\
	libgtk-3-0 libnspr4 xdg-utils libc6 locales locales-all

RUN apt-get install -y libgconf-2-4 && apt-get clean

RUN sh -c 'echo "deb http://archive.canonical.com/ubuntu trusty partner" >> /etc/apt/sources.list.d/canonical_partner.list'
