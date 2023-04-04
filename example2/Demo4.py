# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)
        self.setupUi()
        self.show()
        pass
    def setupUi(self):
        self.setWindowTitle("图标测试")
        self.setWindowIcon(QIcon("free.png"))
        pass



if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    my = MyWindow()
    sysUtils.exit(app.exec())