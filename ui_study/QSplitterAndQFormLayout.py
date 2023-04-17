import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QSplitter, QAction, QMenu, QMainWindow,QWidget,QFormLayout,QLabel,QLineEdit,QVBoxLayout,QTreeWidget,QTreeWidgetItem
from PyQt5.QtCore import Qt
import random as randomUtils
import qdarkstyle



class MyWindow(QMainWindow):

    def __init__(self, title, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle(title)
        # 设置菜单
        self.setupMean()
        # 设置ui
        self.setupUi()
        # self.resize(370, 250)
        self.setGeometry(200, 200, 1000, 400)
        self.show()

    def setupUi(self):
        hSplitter = QSplitter(self)
        # 设置窗口中心的控件
        self.setCentralWidget(hSplitter)
        # 水平线分割
        hSplitter.setOrientation(Qt.Horizontal)
        aWidget = QWidget()
        bWidget = QWidget()
        self.myQFormLayout(bWidget)
        self.myTree(aWidget)
        hSplitter.addWidget(aWidget)
        hSplitter.addWidget(bWidget)
        hSplitter.setStretchFactor(1,3)
    # 设置右边的表单
    def myQFormLayout(self,widget):
        formlayout = QFormLayout()
        widget.setLayout(formlayout)
        for x in range(1,20):
            label = QLabel("标签"+str(x))
            lineEdit = QLineEdit()
            formlayout.addRow(label,lineEdit)
        pass
    # 设置左边 树
    def myTree(self,widget):
        layout = QVBoxLayout()
        widget.setLayout(layout)
        tree = QTreeWidget()
        # 设置树形控件头部的标题
        tree.setHeaderLabels(['动态树'])
        # 设置列数
        tree.setColumnCount(1)
        for rootIndex in range(7,300,7):
            root = QTreeWidgetItem(tree)
            root.setText(0, str(rootIndex))
            for childIndex in range(1,rootIndex,3):
                childItem = QTreeWidgetItem()
                childItem.setText(0, str(childIndex))
                root.addChild(childItem)

        layout.addWidget(tree)
        pass

    # 设置菜单
    def setupMean(self):
        menubar = self.menuBar()
        listMeans = ["文件", "编辑", "搜索", "视图", "编码", "语言", "设置", "工具", "宏", "运行", "插件", "窗口"]
        for meanText in listMeans:
            fileMenu = menubar.addMenu(meanText)
            rootIndex =  randomUtils.randrange(1,100)
            impMenu = QMenu('file'+str(rootIndex), self)
            twoIndex = randomUtils.randrange(0, rootIndex)
            impAct = QAction('Import '+str(twoIndex), self)
            impMenu.addAction(impAct)

            newAct = QAction('New File', self)

            fileMenu.addAction(newAct)
            fileMenu.addMenu(impMenu)

    pass


if __name__ == '__main__':
    print(sysUtils.argv)
    app = QApplication([])
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    myW = MyWindow("分割器学习+菜单")
    sysUtils.exit(app.exec_())
