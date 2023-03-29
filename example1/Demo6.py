from PyQt5 import QtCore
from PyQt5.Qt import *
import sys as sysUtils
import uuid as uuidUtils
import datetime as datetimeUtils
import random

# 简单 信号 机制 学习
class MyWindow(QWidget):

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(500, 500)
        self.move(200, 200)
        self.setupUi()

        self.setupQObject1()
        self.setupQObject2()
        self.setupObject3()
        self.setupObject4()
        self.setupObject5()
        self.setupObject6()
        self.setupDeleteLater()

        self.show()

        pass

    def setupUi(self):
        labelA = QLabel(self)
        labelA.resize(100, 100)
        labelA.setText("label")
        labelA.move(100, 100)
        labelA.setStyleSheet("font-weight: bold;background-color:gold;")
        pass

    # 简单设置一下name 看什么效果
    def setupQObject1(self):
        obj = QObject()
        str1 = str(datetimeUtils.datetime.now())

        print(obj.objectName(), str1)

        # 对象名称发生改变时发射此信号 connect 后面写触发后要调用的函数
        obj.objectNameChanged.connect(self.changeQObjectNameEvent)

        obj.setObjectName(str(uuidUtils.uuid3(uuidUtils.NAMESPACE_DNS, str1)))

        # 断开 信号与槽的连接
        obj.objectNameChanged.disconnect()

        obj.setObjectName(str(uuidUtils.uuid3(uuidUtils.NAMESPACE_DNS, str(random.randrange(100, 10000)))))
        pass

    # 连续改变 name 监听状态
    def setupQObject2(self):
        objX = QObject()
        # 使用匿名函数
        objX.objectNameChanged.connect(lambda e: print("setupQObject2 name 改变", e))
        # 连续设置 名称改变
        objX.setObjectName("x")
        objX.setObjectName("y")
        objX.setObjectName("z")
        pass

    # 阻断信号 之 disconnect
    def setupObject3(self):
        objX = QObject()
        # 使用匿名函数
        objX.objectNameChanged.connect(lambda e: print("setupQObject3 name 改变", e))
        objX.setObjectName("x")

        # 阻断连接
        # objX.objectNameChanged.disconnect()
        objX.setObjectName("y")
        pass

    # 阻断信号 之 blockSignals
    def setupObject4(self):
        objX = QObject()
        # 使用匿名函数
        objX.objectNameChanged.connect(lambda e: print("setupQObject4 name 改变", e))
        objX.setObjectName(str(random.randrange(100, 100000)))
        print("信号状态 False就表示没有被阻断,True表示阻断:", objX.signalsBlocked())
        # 注释下面的代码 本方法会打印两次
        objX.blockSignals(True)

        objX.setObjectName(str(random.randrange(100, 100000)))
        print("信号状态 False就表示没有被阻断,True表示阻断:", objX.signalsBlocked())
        pass

    # destroyed 信号 销毁事件
    def setupObject5(self):
        objX = QObject()
        objX.destroyed.connect(lambda e: print("setupObject5 对象被销毁 ", e))
        pass

    # 获取某个对象信号 到底有多少连接槽
    def setupObject6(self):
        objX = QObject()
        changeEd = objX.objectNameChanged
        changeEd.connect(lambda x: print("setupObject6 连接槽1:", x))
        changeEd.connect(lambda x: print("setupObject6 连接槽2:", x))
        changeEd.connect(lambda x: print("setupObject6 连接槽3:", x))

        print("setupObject6 连接槽数量:",objX.receivers(changeEd))
        pass

    # 删除
    def setupDeleteLater(self):
        objX = QObject()
        objY = QObject()

        objX.setParent(self)
        objY.setParent(objX)
        objX.destroyed.connect(lambda: print("objX被释放了"))
        objY.destroyed.connect(lambda: print("objY被释放了"))

        print(f"objX:{objX}")
        print(f"objY:{objY}")

        objX.deleteLater()
        print(objY.parent())
        print(objX.parent())
        print(objX.children())

        pass

    def changeQObjectNameEvent(self, e):
        print("QObject Name 改变", e)


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    myW = MyWindow("QObject 学习")

    sysUtils.exit(app.exec_())
    pass
