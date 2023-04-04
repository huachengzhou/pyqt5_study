# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QTextEdit, QApplication, QLabel, QDesktopWidget,  QVBoxLayout, QHeaderView
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
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setupUi(layout)
        self.show()

    def setupUi(self,layout):
        self.setWindowTitle("多行文本框")
        self.setWindowIcon(QIcon("free.png"))

        text_edit = QTextEdit()
        text_edit.setPlainText(
            '假如生活欺骗了你''不要悲伤，不要心急！''忧郁的日子里需要镇静：''相信吧，快乐的日子将会来临。''心儿永远向往着未来，''现在却常是忧郁；''一切都是瞬息，''一切都将会过去，''而那过去了的，''就会成为亲切的回忆。')  # 设置HTML文本显示

        layout.addWidget(text_edit)

        # text_edit.textChanged.connect(lambda item:print(f"文本改变:{item}"))
        pass



if __name__ == '__main__':
    # sysUtils.argv
    app = QApplication([])
    print(sysUtils.argv)
    my = MyWindow()
    sysUtils.exit(app.exec_())