# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow
from ui_mainwindow import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # self.action_exit.triggered.connect(self.onExitTriggered)
        #
        # self.action_copy.triggered.connect(self.onCopyTriggered)
        # self.action_paste.triggered.connect(self.onPasteTriggered)
        # self.action_cut.triggered.connect(self.onCutTriggered)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())