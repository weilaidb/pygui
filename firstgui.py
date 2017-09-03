#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets


#pyqt?????QApplication?????
app=QtWidgets.QApplication(sys.argv)


label=QtWidgets.QLabel("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")      #qt??html??????
#?????????show()????
label.show()


sys.exit(app.exec_())
