# PyQt5 使用例子
import sys
import qdarkstyle
from PyQt5 import QtWidgets

# 必须安装 皮肤 qdarkstyle
# pip install qdarkstyle

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

# run
window.show()

sys.exit(app.exec_())
