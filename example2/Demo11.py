import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.mainSplitter = QSplitter(self)
        self.layout.addWidget(self.mainSplitter)
        self.setLayout(self.layout)
        # 水平线分割
        self.mainSplitter.setOrientation(Qt.Horizontal)

        rightSplitter = QSplitter(self)
        # 垂直线分割
        rightSplitter.setOrientation(Qt.Vertical)
        textEdit = QTextEdit()
        textEdit.setText("Window2")
        rightSplitter.addWidget(textEdit)
        textEdit = QTextEdit()
        textEdit.setText("Window3")
        rightSplitter.addWidget(textEdit)

        textEdit = QTextEdit()
        textEdit.setText("Window1")
        self.mainSplitter.addWidget(textEdit)
        self.mainSplitter.addWidget(rightSplitter)
        # 分割比例
        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 2)

        self.mainSplitter.show()
        self.setWindowTitle("Splitter")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())