# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QDesktopWidget, QTableWidget, QTableWidgetItem, \
    QVBoxLayout
from PyQt5.QtGui import QIcon, QBrush, QColor
import random as randomUtils


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setupUI(layout)
        self.show()

    def setupUI(self ,layout):
        self.setWindowTitle("复杂表格学习")
        self.setWindowIcon(QIcon("free.png"))

        table = QTableWidget()
        layout.addWidget(table)

        # 隐藏水平表头
        # table.horizontalHeader().hide()
        # 隐藏垂直表头
        # table.verticalHeader().hide()

        # 设置 表格 行的数量
        table.setRowCount(19)
        # 设置表格 列的数量
        table.setColumnCount(int(randomUtils.randrange(6, 12)))

        list1 = []
        for columnIndex in range(1, table.columnCount() + 1):
            list1.append(str(columnIndex) + "列")
            pass
        table.setHorizontalHeaderLabels(list1)

        list2 = []
        for rowIndex in range(1, table.rowCount() + 1):
            list2.append(str(rowIndex) + "行")
            pass
        table.setVerticalHeaderLabels(list2)

        for rowIndex in range(1, table.rowCount() + 1):
            for columnIndex in range(1, table.columnCount() + 1):
                item = QTableWidgetItem(str(rowIndex) + "-" + str(columnIndex))
                item.setBackground(QBrush(QColor(174, 238, 238)))
                table.setItem(rowIndex - 1, columnIndex - 1, item)
                pass
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    my = MyWindow()

    sysUtils.exit(app.exec_())
