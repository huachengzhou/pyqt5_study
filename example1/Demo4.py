import typing

from PyQt5 import QtCore
from PyQt5.Qt import *
import sys as sysUtils

class WindowsA(QWidget):

    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        self.setupUi()
        self.show()
    def setupUi(self):
        btn1 = QPushButton(self)
        btn1.setText("按钮1")
        btn1.move(100,100)
        btn1.resize(200,200)

        btn2 = QPushButton()
        btn2.setParent(self)
        btn2.setText("按钮2")
        btn2.move(350, 100)
        btn2.resize(200, 200)

        print(btn2.parent())
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    window1 = WindowsA("杀生丸")
    sysUtils.exit(app.exec_())
    pass