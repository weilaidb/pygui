# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import sys
import xml.etree.ElementTree as ET

from common import *
from checksum import *


class SYSXMLParser(object):
    def __init__(self,file):
        self.xmlFile = file
        self.sysXMLDict = {}

    def getSysXMLDict(self):
        tree = ET.parse(self.xmlFile)
        root = tree.getroot()

        for child in root.getchildren():
            self.sysXMLDict[child.tag] = child.attrib
            self.sysXMLDict[child.tag] = child.text

        return self.sysXMLDict