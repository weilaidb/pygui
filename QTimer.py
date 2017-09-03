# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.timer = QBasicTimer()
        self.count = 0
        self.timer.timeout.connect(self.showNum)
        self.startCount()

    def startCount(self):
        self.timer.start(1000)

    def showNum(self):
        self.count = self.count + 1
        print(self.count)


    

