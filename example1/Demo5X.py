import sys

from PyQt5.Qt import *

import os as osUtils


class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        """从文件中读取qss的静态方法"""
        with open(qss_file_name, "r", encoding="UTF-8") as file:
            return file.read()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS-导入外部样式")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        cb = QCheckBox("复选框", self)
        cb.move(300, 200)
        le = QLineEdit(self)
        le.move(100, 200)
        tw = QTabWidget(self)
        tw.addTab(QTextEdit(), "第一个标签页")
        tw.move(100, 250)
        sb = QSpinBox(self)
        sb.move(300, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    # style_file = "./resources/flatwhite/style.qss"
    style_file = osUtils.path.join("resources","flatwhite", "style.qss")
    style_sheet = QSSLoader.read_qss_file(style_file)
    window.setStyleSheet(style_sheet)

    window.show()
    sys.exit(app.exec_())
