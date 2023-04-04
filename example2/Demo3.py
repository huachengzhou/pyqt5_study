# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QDesktopWidget


class MyWindow(QWidget):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)
        self.show()
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    my = MyWindow("窗口居中")
    sysUtils.exit(app.exec_())
