
# 导入需要的包
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
import sys as sysUtils

# 创建一个应用程序
app = QApplication(sysUtils.argv)


# 控件也可以作为一个容器(承载其他的控件)

window = QWidget()
window.setWindowTitle( "燕雀安知鸿鹄之志哉")
window.resize(600, 600)
window.move(200, 200)

# window 相当于是构建器
label = QLabel(window)


label.setText(
    "一个人要博学 审问 慎思 明辨 然后力行")

label.move(100,100)

# 作为独立控件
btn1 = QPushButton()
btn1.setText("按钮")
# 独立控件默认不显示的
btn1.show()

# show方法 不要放在前面了
window.show()





sysUtils.exit(app.exec_())
