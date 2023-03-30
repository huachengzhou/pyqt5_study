# -*- coding: utf-8 -*-
# 例1，简单的窗口

import sys as sysUtils
from  PyQt5.QtWidgets import QWidget,QPushButton,QApplication

class MyWindow (QWidget):

    def __int__(self):
        super().__int__()
        self.resize(200,200)
        self.move(200,200)
        self.show()
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    myW = MyWindow()

    sysUtils.exit(app.exec_())