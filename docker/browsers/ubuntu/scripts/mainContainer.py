#!/usr/bin/python3
# -*-coding:utf-8 -*

import os
import random
import subprocess
import time
# import numpy
from chrome import *
from firefox import *
from checkedFonts import fontsList
from symbol import if_stmt
from fpParser import FPparser

homePath = "/home/local/"
fontsPath = homePath + ".fonts/"
procPath = "/home/fproc/"

fp = {}


############### Container Class
class Container(object):
    # Browsers dictionary
    browsersDict = {'Chrome':Chrome, 'Opera':Opera, 'Chromium':Chromium, 'Firefox':Firefox}
    browsersList = ['Chrome', 'Opera', 'Chromium', 'Firefox']

    # ## BROWSERS
    def selectBrowser(self, browser):
        browsersList = ['Chrome', 'Opera', 'Chromium', 'Firefox']

        return self.browsersDict[browsersList[browsersList.index(browser)]]()

    # ##It is assumed that all font's files are in lowercase
    def selectFonts(self, detectedFonts):
        tmp = [font for font in detectedFonts]
        detectedFonts.clear()
        for font in tmp:
            detectedFonts.append(font.lower().replace(" ", "").replace("-", "").replace("_", ""))

        tmp = fontsList.copy()
        fontsList.clear()
        for font in tmp:
            fontsList.append(font.lower().replace(" ", "").replace("-", "").replace("_", ""))

        for font in fontsList:
            if not font in detectedFonts:
                subprocess.call("sudo rm -rf " + fontsPath + font + "*", shell=True)
                subprocess.call("echo rm -rf " + fontsPath + font + "*", shell=True)

        subprocess.call(["fc-cache", "-f", "-v"])

    def getFileDetectedFonts(listDetecFonts):
        detectedFonts = []
        index = 0
        for i in range(0, len(listDetecFonts), 3):
            fi = listDetecFonts[i:i + 3]
            if "t" in fi:
                detectedFonts.append(listFonts[index].lower().replace(" ", "").replace("-", "").replace("_", ""))
                index = index + 1

        files = [f for f in listdir(fontsPath) if isfile(join(fontsPath, f))]
        fileFonts = []
        for file in files:
            name = file.split(".")[0]
            if name in detectedFonts:
                fileFonts.append(file)
        return fileFonts


############### Main
def main():

    parser = FPparser(procPath)

    container = Container()
    #####fonts
    container.selectFonts(parser.getDetectedFonts())

    dntChar = parser.fp['dntJs'][0]
    #if dntChar == '1' or dntChar == 'y' or dntChar == 'Y' or dntChar == 't' or dntChar == 'T':
     #   if parser.fp['browser'] == 'Firefox':


    shutdown = False

    while not shutdown :
        # ##browser
        br = parser.fp['browser']
        if "-" in br:
            br = br.split("-")[0]
        if "_" in br:
            br = br.split("_")[0]
        if " " in br:
            br = br.split(" ")[0]

        browser = container.selectBrowser(br)
        # We launch the browser
        browserProcess = browser.runBrowser()

        # We wait for either the browsing session to be finished
        while not isinstance(browserProcess.poll(), int):
            time.sleep(0.1)

        shutdown = True


if __name__ == "__main__":
    main()
