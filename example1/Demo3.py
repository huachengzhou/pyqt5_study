
from PyQt5 import QtCore
from PyQt5.Qt import *
import sys as sysUtils

class MyWindows(QWidget):

    def __init__(self ,title):
        # 先执行qt组件的构造器初始化方法
        super().__init__()
        # 设置标题
        self.setWindowTitle(title)
        # 设置位置
        self.resize(500, 500)
        self.setupInit()
        self.show()
        pass

    def setupInit(self):
        labelA = QLabel(self)
        labelA.setText("红色")
        labelA.resize(100, 200)
        labelA.setStyleSheet("background-color:red;")
        labelA.move(100, 100)

        labelB = QLabel(self)
        labelB.setText("蓝色")
        labelB.resize(400, 400)
        labelB.move(300, 300)
        labelB.setStyleSheet("background-color:blue;font-weight: bold; font-size: 20px; color: orange")
        pass


# 这个是 idea 默认生成的方法  当执行当前文件的时候会检测到是调用还是直接执行的
if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    myWindow = MyWindows("我是一只聪明又强壮的大懒猫")
    sysUtils.exit(app.exec_())
    pass
