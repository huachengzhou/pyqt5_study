import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QFormLayout


class MyWindow(QWidget):

    def __init__(self):  # self 就是一个实例对象
        super().__init__()  # 子类的方法调用父类的方法进行初始化

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('form')

        self.layout_form()

    def layout_form(self):

        formlayout = QFormLayout()
        labl1 = QLabel("标签1")
        lineEdit1 = QLineEdit()
        labl2 = QLabel("标签2")
        lineEdit2 = QLineEdit()
        labl3 = QLabel("标签3")
        lineEdit3 = QLineEdit()

        formlayout.addRow(labl1, lineEdit1)
        formlayout.addRow(labl2, lineEdit2)
        formlayout.addRow(labl3, lineEdit3)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用对象
    window = MyWindow()  # 创建MyWindow实例
    window.show()   # 展示窗口
    sys.exit(app.exec_())  # 进入主程序循环 并安全退出