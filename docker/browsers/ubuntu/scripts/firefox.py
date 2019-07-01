#!/usr/bin/python3
# -*-coding:utf-8 -*

import os
import json
import pickle
import subprocess
from subprocess import CalledProcessError
from browser import Browser,utils

class FirefoxBase(Browser):
    
    def __init__(self,path):
        super().__init__()
        self.firefoxPath = path
       
    def runBrowser(self):
        return subprocess.Popen(self.firefoxPath+" -no-remote -setDefaultBrowser --no-first-run -width 5000 -height 5000", shell=True)

class Firefox(FirefoxBase):
    def __init__(self):
        super().__init__("/firefox-latest/firefox")

