#!/usr/bin/python3
# -*-coding:utf-8 -*

import re
import os
import sys
import random
import datetime
import subprocess
import urllib.request
from installContainers import buildDockerImageLocal, instantiateContainer
from installUtils import prefixRepoLocal, prefixRepoHub
from _datetime import timezone
from pytz import _CountryTimezoneDict
from fpParser import FPparser
from languages import supported_languages
from languages import default_languages

timezonePath = "/usr/share/zoneinfo/"
fp = {}


def checkInstallation():
    # Check the presence of the two main containers
    # and the two main OS images
    output = subprocess.check_output(["sudo", "docker", "ps", "-a"]).decode()
    if len(regExp.findall(output)) != 2:
        sys.exit("System is not installed")

    output = subprocess.check_output(["sudo", "docker", "images"]).decode()
    for image in osImages :
        if image not in output:
            sys.exit("System is not installed")

    # If the installation is correct, we generate the LD Preload libraries



def updateOS():
    print("Start updating OS containers")
    updateFile = profilePath + "/update"
    # We write the "update" file to inform containers tu update
    subprocess.call(["touch", updateFile])

    # We run the update script in each container
    # to update packages and plugins
    for image in osImages:
        subprocess.call(["sudo", "docker", "run", "-it", "-v", profilePath + ":/home/blink/profile", "--volumes-from", "blinkbrowsers", prefixRepoLocal + image])
        dockerID = subprocess.check_output(["sudo", "docker", "ps", "-l", "-q"])
        subprocess.call(["sudo", "docker", "commit", dockerID.decode().strip(), prefixRepoLocal + image])
        print("Update of " + image + " complete")

    # We remove the update file
    subprocess.call(["rm", updateFile])
    print("OS Containers updated")

def writeInstallComplete(mode):
    #######
    # We write a file that indicates that the installation is complete
    # Format of the install complete file
    # data = "XXXX YYYY"
    # data[0] = "XXXX" -> days since the last update of OS containers
    # data[1] = "YYYY" -> days since the last update of browsers
    #######

    data = []

    if mode < 2:
        # We read the current installComplete file
        with open('installComplete', 'r') as f:
            data = f.read().strip().split(" ")
        # We update either the first or second counter
        data[mode] = datetime.date.today().toordinal()
    elif mode == 2:
        # We update both counters
        # (in the case of a fresh install)
        nowDate = datetime.date.today().toordinal()
        data = [nowDate, nowDate]

    if len(data) == 2:
        with open('installComplete', 'w') as f:
            f.write("{} {}".format(data[0], data[1]))
    print("installComplete file written")


def main():
    
    if os.path.isfile("fp.txt"):
        os.rename("fp.txt","fp")
    
    if not os.path.isfile("fp"):
        print("No configuration file detected.\nProvide a proper configuration file in order to proceed.")
    else:
    
        print("running browser container...")

        chosenImage = "fproc/ubuntu-fproc"

        print("Image " + chosenImage + " chosen")

        subprocess.call("sudo cp fp docker/run/ubuntu/", shell=True)
        #subprocess.call("sudo cp fpParser.py docker/run/ubuntu/scripts/", shell=True)

        parser = FPparser("")

        chosenTimezone = parser.getTimeZone()

        # setting languages
        lang = parser.getLanguages();
        language = 'C'
        # check that the 1st and 2nd lang are the same

        if len(lang) > 1 and lang[0].split('-')[0] == lang[1].split('-')[0]:
            l = lang[1].replace('-', '_')
            if l in supported_languages:
                language = l
            else:
                l = lang[0].replace('-', '_')
                if l in supported_languages:
                    language = l
        else:
            l = lang[0].replace('-', '_')
            if l in supported_languages:
                language = l
            else:
                language = default_languages[lang[0].split('-')[0]]

        launchCommand = "sudo docker run -ti --rm -e DISPLAY " \
                    "--group-add $(getent group audio | cut -d: -f3) " \
                    "-v /tmp/.X11-unix:/tmp/.X11-unix " \
                    "--device /dev/snd " \
                    "-v /run/user/`id -u`/pulse/native:/run/user/`id -u`/pulse/native " \
                    "-v /dev/shm:/dev/shm " \
                    "-v /etc/machine-id:/etc/machine-id " \
                    "-v /var/lib/dbus:/var/lib/dbus " \
                    "-v  " + os.environ['HOME'] + "/Downloads/://home/local/Downloads/  " \
                    "-e TZ=" + chosenTimezone + " "\
                    "-e LANG=" + language + ".UTF-8 "\
                    "-e LC_ALL=" + language + ".UTF-8 "\
                    "--net host "


    # map a directory on the host to the Downloads dir in the container
    # -v  /home/$user/Downloads:/home/local/Downloads

        subprocess.call("docker build --no-cache -t " + chosenImage + " docker/run/ubuntu/", shell=True)    
        subprocess.call(launchCommand + chosenImage, shell=True)

        print("End of script")


if __name__ == "__main__":
    main()
