FROM gomezboix/ubuntu-origin

#Chrome OK
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo dpkg -i google-chrome-stable_current_amd64.deb && sudo apt-get install -f && rm google-chrome-stable_current_amd64.deb #&& bash extensions/nativeApp/install_host.sh

#Opera OK
RUN wget -qO- https://deb.opera.com/archive.key | sudo apt-key add - && \
	sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install --yes opera-stable

#Chromium OK check alsa-base and xauth
RUN apt-get install -y alsa-base chromium-browser xauth

#Firefox (latest stable and latest ESR) OK
RUN wget -O firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && tar -xvjf firefox* && mv firefox firefox-latest && rm firefox.tar.bz2
RUN wget -O firefox-esr.tar.bz2 "https://download.mozilla.org/?product=firefox-esr-latest&os=linux64&lang=en-US" && tar -xvjf firefox-esr.tar.bz2  && mv firefox firefox-latest-esr && rm firefox-esr.tar.bz2

#creating file system and execution environment
RUN mkdir /home/fproc
ADD scripts/*.py /home/fproc/

ENV USER local
RUN mkdir /home/${USER} &&  sudo useradd ${USER} -d /home/${USER} && passwd -d ${USER}

# Replace 1000 with your user / group id
RUN export uid=0 gid=0 && \
    echo "${USER}:x:${uid}:${gid}:${USER},,,:/home/${USER}:/bin/bash" >> /etc/passwd && \
    echo "${USER}:x:${uid}:" >> /etc/group && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER} && \
    chown ${uid}:${gid} -R /home/${USER}

RUN sudo mkdir /home/${USER}/.fonts
ADD fonts/* /home/${USER}/.fonts/

USER ${USER}

CMD /bin/sh
