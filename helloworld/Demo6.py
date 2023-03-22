import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon,QPixmap

class pushButtonDemo(QWidget):
    def __init__(self):
        super(pushButtonDemo, self).__init__()

        #定义button
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()

        #设置button1
        self.button1.setText("button1")
        #设置按钮点击按钮后保持“已经点击"状态,再次点击才释放。如果设置,则按下按钮后自动释放
        self.button1.setCheckable(True)
        #设置初始状态,如果设置为True,初始状态为已经按下了
        #self.button1.setChecked(True)
        #如果调用了这函数,类似self.button1.setChecked(True)一样,初始状态为已经按下了
        #self.button1.toggle()
        #信号:
        # Pressed: 当鼠标左键按下按键，触发该信号
        # Released: 当鼠标左键按下释放按键，触发该信号
        # Clicked: 当鼠标左键按下按键后马上释放,触发该信号
        # toggled: 当按钮的标记状态发生改变时触发该信号
        self.button1.clicked.connect(self.buttonStatus)
        #self.button1.released.connect(self.releasedSignalHandle)
        #self.button1.clicked.connect(self.clickedSignalHandle)
        #self.button1.toggled.connect(self.toggledSignalHandle)


        #设置button2
        #self.button2.setText("button2")
        #设置Icon
        self.button2.setIcon(QIcon(QPixmap('python-logo.png')))
        #设置button不可点击
        self.button2.setEnabled(False)
        self.button2.setFixedSize(600,600)


        #布局
        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(self.button1)
        vboxlayout.addWidget(self.button2)


        #self.resize(200,100)
        self.setLayout(vboxlayout)

    def pressSignalHandle(self):
        print("button is pressed")

    def releasedSignalHandle(self):
        print("button is released")

    def buttonStatus(self):
        if self.button1.isChecked():
            print("button has been pressed")
        else:
            print("button has been released")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    pushbutton = pushButtonDemo()
    pushbutton.show()
    sys.exit(app.exec_())