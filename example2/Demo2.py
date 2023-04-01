# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel


class MyWindow(QWidget):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 600, 500)
        self.setupUi()
        self.show()
        pass

    def setupUi(self):
        labelA = QLabel(self)
        labelA.setText("标签")
        labelA.setGeometry(100, 100, 50, 50)
        labelA.setStyleSheet(" background-color:blue;")

        print(labelA.geometry().center().x())
        print(labelA.geometry().center().y())
        print(labelA.geometry().height())
        print(labelA.geometry().width())

        btnA = QPushButton(self)
        btnA.setText("按钮a")
        #  x, y , w, h
        # 其实这里 直接读的x y坐标是系统修正后的坐标
        btnA.setGeometry(labelA.geometry().center().x() +50, 100 ,
                         labelA.geometry().width() , labelA.geometry().height())
        btnA.setStyleSheet(" background-color:red;")

        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    mW = MyWindow("简单例子")
    sysUtils.exit(app.exec())
