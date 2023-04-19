"""
动态加载ui文件
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic as uicUtils

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uicUtils.loadUi("./test.ui")
    print(ui.__dict__)
    print(ui.horizontalLayout.itemAt(1).widget())

    for x in range(0,ui.verticalLayout.count()):
        print(x)
        ui.verticalLayout.itemAt(x).widget().clicked.connect(lambda xx: print(xx,ui.verticalLayout.itemAt(x).widget().text(),"被点击了"))
        ui.verticalLayout.itemAt(x).widget().clicked.connect(lambda xx: ui.horizontalLayout.itemAt(0).widget().setText(ui.verticalLayout.itemAt(x).widget().text()+"点击了"))
        pass
    # 展示窗口
    ui.show()

    app.exec()
