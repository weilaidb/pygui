# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer
import logging

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.showInputDialog()

    def showInputDialog(self):
        opN,okPressed = QInputDialog.getText(self,"**科技","请输入生产订单号:",QLineEdit.Normal, " ")
        if okPressed and opN.strip():
            print('PON:' + opN)
            logging.info('PON:' + opN)
            self.poNumber = opN
            self.lineedit_order.setText(self.poNumber)

        else:
            QMessageBox.critical(self,ERRORTITLE,"请输入订单号,点击OK进入系统!")
            exit(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())