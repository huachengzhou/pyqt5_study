from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(450, 640)  # 设置固定大小

        # self.setWindowFlags(Qt.CustomizeWindowHint)  # 隐藏标题栏
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        # 设置总样式，QWidget
        self.setStyleSheet('''
            QWidget
            {border:15px;
            margin:10px;
            margin-left:82px;
            margin-right:50px;
            font-family:'华文新魏';
            font-size:40px;
            font-weight:bold;
            background-color:rgb(200,255,255);
            }
            QWidget#right_widget
            {border-radius:15;}
        ''')
        # 创建布局
        layout = QVBoxLayout()
        # 创建一个4个控件
        lb = QLabel('XXX登录系统')
        lineEdit1 = QLineEdit('')
        lineEdit2 = QLineEdit('')
        # 设置账号输入形式
        lineEdit1.setPlaceholderText('账号名')
        # 设置密码形式
        lineEdit2.setPlaceholderText('密码')
        lineEdit2.setEchoMode(QLineEdit.Password)
        # 设置LineEdit1格式
        lineEdit1.setStyleSheet('''
            QLineEdit
            {border:0px;
            border-radius:0;
            margin:10px;
            margin-left:50px;
            margin-right:50px;
            border-bottom: 2px solid #B3B3B3;
            font-family:'等线';
            font-size:25px;
            font-weight:bold;}
            QLineEdit:hover{
                border-bottom:3px solid #66A3FF;
            }
            QLineEdit:focus{
                border-bottom:3px solid #E680BD
            }
        ''')
        # 设置LineEdit2格式
        lineEdit2.setStyleSheet('''
            QLineEdit
            {border:0px;
            border-radius:0;
            margin:10px;
            margin-left:50px;
            margin-right:50px;
            border-bottom: 2px solid #B3B3B3;
            font-family:'等线';
            font-size:25px;
            font-weight:bold;}
            QLineEdit:hover{
                border-bottom:3px solid #66A3FF;
            }
            QLineEdit:focus{
                border-bottom:3px solid #E680BD;
            }
        ''')

        btn = QPushButton('登录')
        btn.setFixedSize(400, 60)
        # 设置按钮格式
        btn.setStyleSheet(''' 
                            QPushButton
                            {text-align : center;
                            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);
                            font: bold;
                            border-color: grey;
                            border-width: 2px;
                            border-radius: 10px;
                            padding: 6px;
                            height: 28px;
                            border-style: outset;
                            font-family:'黑体';
                            font : 18px;}

                            QPushButton:pressed
                            {text-align : center;
                            background-color : light gray;
                            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);
                            font: bold;
                            color:lightblue;
                            border-color: gray;
                            border-width: 2px;
                            border-radius: 10px;
                            padding: 6px;
                            height : 28px;
                            border-style: outset;
                            font-family:'黑体';
                            font : 18px;}
                            QPushButton:hover:!pressed
                            {color:red;}
                            ''')

        layout.addWidget(lb)
        layout.addWidget(lineEdit1)
        layout.addWidget(lineEdit2)
        layout.addWidget(btn)
        self.setLayout(layout)
        print(type(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = widget()
    demo.show()
    sys.exit(app.exec_())

