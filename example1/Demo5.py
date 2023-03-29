from PyQt5.Qt import *
import sys as sysUtils
import pathlib as pathLib


# 导入文件 qcss
class QSSLoader:
    def __init__(self):
        pass

    # 注解表示本方法是静态方法 不需要创建对象就可以调用 注意这个是高版本python语法
    @staticmethod
    def read_qss_file(qss_file_name):
        """从文件中读取qss的静态方法"""
        with open(qss_file_name, "r", encoding="UTF-8") as file:
            return file.read()


class MyWindow1(QWidget):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(500, 500)
        self.move(300, 300)
        self.setupUi()
        self.show()
        pass

    def setupUi(self):
        # 定义一个主容器
        parentQWidget = QWidget()
        parentQWidget.setParent(self)
        doubleX = 200
        doubleY = 200

        btnA = QPushButton(parentQWidget)
        btnA.setText("按钮")
        btnA.move(doubleX, doubleY)
        btnA.resize(50, 50)

        labelA = QLabel()
        labelA.setParent(parentQWidget)
        labelA.move(doubleX + 70, doubleY + 50)
        labelA.setText("标签A")
        labelA.resize(50, 50)

        labelB = QLabel()
        labelB.setParent(parentQWidget)
        labelB.move(doubleX + 70 + 50+20, doubleY + 50)
        # 设置 id选择器
        labelB.setObjectName("b")
        labelB.setText("标签B")
        labelB.resize(50, 50)

        labelB_1 = QLabel()
        labelB_1.setParent(parentQWidget)
        labelB_1.move(doubleX + 70, doubleY + 50 + 30 + 50)
        # 设置 id选择器
        labelB_1.setObjectName("b")
        # 设置属性
        labelB_1.setProperty("level", "1")
        labelB_1.setText("标签B1")
        labelB_1.resize(50, 50)

        labelB_2 = QLabel()
        labelB_2.setParent(parentQWidget)
        labelB_2.move(doubleX + 70 + 50+20, doubleY + 50 + 30 + 50)
        # 设置 id选择器
        labelB_2.setObjectName("b")
        # 设置属性
        labelB_2.setProperty("level", "2")
        labelB_2.setText("标签B2")
        labelB_2.resize(50, 50)

    pass


if __name__ == '__main__':
    dirCss = pathLib.Path(pathLib.Path.cwd().joinpath(*('resources', "d.qcss")))
    style_sheet = QSSLoader.read_qss_file(str(dirCss))
    app = QApplication(sysUtils.argv)

    myWindow = MyWindow1("qcss学习")
    # 注入 css 样式
    myWindow.setStyleSheet(style_sheet)

    print(style_sheet)

    sysUtils.exit(app.exec_())
