# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QWidget,  QStackedLayout, QLabel, QDesktopWidget


class WindowChild(QWidget):
    def __init__(self, text, style):
        super().__init__()
        label = QLabel(text)
        label.setParent(self)
        self.setStyleSheet(style)
        self.setGeometry(300,300,200,200)
        pass


class MyWindow(QWidget):

    def __init__(self, title):
        super().__init__()

        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)

        self.setupUi()
        self.setWindowTitle(title)
        self.show()

        pass

    def setupUi(self):
        stacked_layout = QStackedLayout()

        # 创建单独的Widget
        win1 = WindowChild("red", "background-color:red;")
        win2 = WindowChild("blue", "background-color:blue;")

        stacked_layout.addWidget(win1)
        stacked_layout.addWidget(win2)

        stacked_layout.setCurrentIndex(0)
        self.setLayout(stacked_layout)
        pass


if __name__ == '__main__':
    app = QApplication([])
    myWindow = MyWindow("QStackedLayout 选项卡布局")
    sysUtils.exit(app.exec_())
