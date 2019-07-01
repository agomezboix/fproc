#!/usr/bin/python3
# -*-coding:utf-8 -*

from abc import ABCMeta, abstractmethod
import utils

class Browser(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def runBrowser(self):
        raise NotImplementedError("runBrowser function not implemented")
    

