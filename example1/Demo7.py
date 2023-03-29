from PyQt5.Qt import *
import sys as sysUtils
import time as timeUtils
import datetime as datetimeUtils


# 按钮 点击事件 简单学习
class MyWindowsX(QWidget):

    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.resize(500, 500)
        self.move(200, 200)
        self.setupUiBtn()
        self.show()
        pass

    def setupUiBtn(self):
        btn = QPushButton()
        btn.setParent(self)
        btn.setText("点击我")
        btn.resize(50, 50)
        btn.move(300, 300)
        btn.setStyleSheet("font-weight: bold;background-color:#1E90FF;color:white;border-radius: 4px 3px 6px 10px;")

        btn.clicked.connect(lambda x: print(datetimeUtils.datetime.now(), "我被点击了", x))
        btn.clicked.connect(self.btnClickEvent)
        pass

    def btnClickEvent(self, e):
        print(timeUtils.time(), " 按钮被点击", e)
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)

    myW = MyWindowsX("按钮点击事件学习")

    sysUtils.exit(app.exec_())
