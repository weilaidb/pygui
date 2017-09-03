#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
#?PyQt???QtWidget?????
class mywindow(QtWidgets.QWidget):
    #?????mywindows???class???mywindows???????
    #?QtWidgets.QWidget????QtWidgets.QWidget????
    def __init__(self):
        super(mywindow,self).__init__()



import sys
app = QtWidgets.QApplication(sys.argv)
windows = mywindow()
label=QtWidgets.QLabel(windows)     #??????label
label.setText("hello world,the world all in my heart")


windows.show()
sys.exit(app.exec_())
