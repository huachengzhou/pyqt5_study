# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QLabel, QDesktopWidget,  QVBoxLayout, QHeaderView
from PyQt5.QtGui import QIcon, QBrush, QColor, QFont
import random as randomUtils
from PyQt5.QtCore import Qt, QSize

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)


        # layout.addStretch(0)
        # layout.setSpacing(0)
        self.setLayout(layout)
        self.setupUi(layout)
        self.show()

    def setupUi(self,layout):
        self.setWindowTitle("单行文本框")
        self.setWindowIcon(QIcon("free.png"))

        lineEdit = QLineEdit()

        layout.addWidget(lineEdit)

        lineEdit.textChanged.connect(lambda item:print(f"文本改变:{item}"))
        lineEdit.editingFinished.connect(lambda item:print(f"当文本框中的内容编辑结束时发射该信号，以按下<Enter>键为编辑结束标志:{item}"))
        pass



if __name__ == '__main__':
    # sysUtils.argv
    app = QApplication([])
    print(sysUtils.argv)
    my = MyWindow()
    sysUtils.exit(app.exec_())