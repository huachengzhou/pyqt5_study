import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QStackedLayout, QPushButton, QVBoxLayout
from PyQt5.QtCore import *


class MyWindow(QWidget):

    def __init__(self):  # self 就是一个实例对象
        super().__init__()  # 子类的方法调用父类的方法进行初始化

        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('layout_stacked')

        self.layout_stacked01()
        # self.layout_stacked02()

    def layout_stacked01(self):
        button = QPushButton("切换")

        self.stackedLayout = QStackedLayout()

        label1 = QLabel("春")
        label1.setStyleSheet("background-color:red;")
        label2 = QLabel("夏")
        label2.setStyleSheet("background-color:green;")
        label3 = QLabel("秋")
        label3.setStyleSheet("background-color:yellow;")
        label4 = QLabel("冬")
        label4.setStyleSheet("background-color:cyan;")

        self.stackedLayout.addWidget(label1)
        self.stackedLayout.addWidget(label2)
        self.stackedLayout.addWidget(label3)
        self.stackedLayout.addWidget(label4)

        button.clicked.connect(self.connect)  # 按钮绑定切换事件

        vlayout = QVBoxLayout()
        vlayout.addWidget(button, Qt.AlignBottom)
        vlayout.addLayout(self.stackedLayout)

        self.setLayout(vlayout)
        print(self.stackedLayout.count(), self.stackedLayout.currentIndex())

    # 通过索引来设置切换界面
    def connect(self):
        self.stackedLayout.setCurrentIndex((self.stackedLayout.currentIndex()+1) % self.stackedLayout.count())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用对象
    window = MyWindow()  # 创建MyWindow实例
    window.show()   # 展示窗口
    sys.exit(app.exec_())  # 进入主程序循环 并安全退出