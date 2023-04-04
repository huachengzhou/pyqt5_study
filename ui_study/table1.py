# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QDesktopWidget, QTableWidget, QTableWidgetItem, \
    QVBoxLayout
from PyQt5.QtGui import QIcon
import random as randomUtils


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
                         available.height() / 2)
        self.setLayout(layout)
        self.setupUi(layout)
        self.show()
        pass

    def setupUi(self,layout):
        self.setWindowTitle("表格")
        self.setWindowIcon(QIcon("free.png"))

        table = QTableWidget()
        layout.addWidget(table)

        table.horizontalHeader().hide()  # 隐藏水平表头
        table.verticalHeader().hide()  # 隐藏垂直表头

        # 设置 表格 行的数量
        table.setRowCount(10)
        # 设置表格 列的数量
        table.setColumnCount(int(randomUtils.randrange(4,8)))

        for rowIndex in range(1, table.rowCount() + 1):
            for columnIndex in range(1, table.columnCount() + 1):
                item = QTableWidgetItem("第%d行 %d列" % (rowIndex, columnIndex))
                table.setItem(rowIndex - 1, columnIndex - 1, item)
                pass
        pass


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    my = MyWindow()
    sysUtils.exit(app.exec())
