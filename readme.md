# 安装

```cmd
pip install PyQt5 -i https://pypi.douban.com/simple


pip install PyQt5-tools -i https://pypi.douban.com/simple
```

+ 验证是否安装成功 code

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(640, 480)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec())

```