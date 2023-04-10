# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QBrush, QColor, QFont
import random as randomUtils
from PyQt5.QtCore import Qt, QSize

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("水平布局")
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.setGeometry(100,100,400,400)
        self.setupUi(layout)
        self.show()
        pass
    def setupUi(self,layout):
        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零
        # 会将你放在layout中的空间压缩成默认的大小
        layout.addStretch(2)
        btn1 = QPushButton("a-")
        layout.addWidget(btn1)

        btn2 = QPushButton("b-")
        layout.addWidget(btn2)
        layout.addStretch(2)
        pass


if __name__ == '__main__':
    app = QApplication([])
    my = MyWindow()
    sysUtils.exit(app.exec())