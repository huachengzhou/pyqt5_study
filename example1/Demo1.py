
# 导入需要的包
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
import sys as sysUtils

# 创建一个应用程序
app = QApplication(sysUtils.argv)


# 控件也可以作为一个容器(承载其他的控件)
# 控件操作 start
window = QWidget()
window.setWindowTitle( "燕雀安知鸿鹄之志哉")
window.resize(600, 600)
window.move(200, 200)

# window 相当于是构建器
label = QLabel(window)

label.setText(
    "第一眼就看上的衣服往往你买不起，第一眼就心动的人往往他不会喜欢你。你真正喜欢想要的，没有一样是可以轻易得到的。这就是努力的理由")

label.move(100,100)

# show方法 不要放在前面了
window.show()

# 控件操作 end


# 开始执行应用程序，并进入消息循环
# 让整个程序开始执行,并且进入到消息循环(无限循环)
# 检测整个程序所接收到的用户的交互信息
# sysUtils.exit(app.exec())
sysUtils.exit(app.exec_())
# sysUtils.exit(1)
# while True:
#     pass