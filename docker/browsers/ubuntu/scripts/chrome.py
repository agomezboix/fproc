#!/usr/bin/python3
# -*-coding:utf-8 -*

import os
import json
import pickle
import subprocess
from subprocess import CalledProcessError
from browser import Browser,utils

class ChromeBase(Browser):
    
    def __init__(self,cmd):
        super().__init__()
        self.chromePath = cmd
   
    def runBrowser(self):
        return subprocess.Popen(self.chromePath+" --no-sandbox --no-default-browser-check --no-first-run --start-maximized",shell=True)
 
class Chrome(ChromeBase):
    def __init__(self):
        super().__init__("google-chrome")

class Opera(ChromeBase):
    def __init__(self):
        super().__init__("opera")

class Chromium(ChromeBase):
    def __init__(self):
        super().__init__("chromium-browser")
