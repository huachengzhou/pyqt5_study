# 使用浅色主题
import sys
import qdarkstyle
from PyQt5 import QtWidgets
from qdarkstyle.light.palette import LightPalette

# 必须安装 皮肤 qdarkstyle
# pip install qdarkstyle

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))

# run
window.show()
app.exec_()