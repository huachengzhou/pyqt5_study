# -*- coding: utf-8 -*-
# 例1，简单的窗口

import sys as sysUtils
from  PyQt5.QtWidgets import QWidget,QPushButton,QApplication

class MyWindow2 (QWidget):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        # 注意坐标是从左上角为原点开始计算
        # w, h
        self.resize(200,200)
        # x,y
        self.move(200,200)
        # 显示位置与大小 ： x, y , w, h
        # self.setGeometry(200,200,200,200)
        self.show()
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    myW = MyWindow2("app")

    sysUtils.exit(app.exec_())