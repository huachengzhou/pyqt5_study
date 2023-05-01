import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QTextEdit, QSplitter, QAction, QMenu, QMainWindow
from PyQt5.QtCore import Qt
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
        self.setGeometry(200, 200, 500, 400)
        self.show()

    def setupUi(self):
        hSplitter = QSplitter(self)
        # 设置窗口中心的控件
        self.setCentralWidget(hSplitter)
        # 水平线分割
        hSplitter.setOrientation(Qt.Horizontal)
        aText = QTextEdit()
        bText = QTextEdit()
        aText.setPlainText("a")
        bText.setPlainText("b")

        hSplitter.addWidget(aText)
        hSplitter.addWidget(bText)
        hSplitter.setStretchFactor(1, 2)

    def setupMean(self):
        menubar = self.menuBar()
        listMeans = ["文件", "编辑", "搜索", "视图", "编码", "语言", "设置", "工具", "宏", "运行", "插件", "窗口"]
        for meanText in listMeans:
            fileMenu = QMenu(meanText, self)
            # fileMenu = menubar.addMenu(meanText)
            # fileMenu = menubar.addMenu(mean)
            menubar.addMenu(fileMenu)
            impMenu = QMenu('Import', self)
            impAct = QAction('Import mail', self)
            impMenu.addAction(impAct)

            newAct = QAction('New', self)
            # newAct.triggered.connect(lambda x:print('菜单被点击了'+x))
            newAct.triggered.connect(self.toggleMenu)

            fileMenu.addAction(newAct)
            fileMenu.addMenu(impMenu)

    pass

    def toggleMenu(self, state):
        print(state)


if __name__ == '__main__':
    print(sysUtils.argv)
    app = QApplication([])
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    myW = MyWindow("分割器学习+菜单")
    sysUtils.exit(app.exec_())
