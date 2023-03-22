#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a more
complicated window layout using
the QGridLayout manager.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication,QPushButton)

import os as osUtils
import json as jsonUtils
import pathlib as pathLib


DIR_FILE_BASE = ""
DIR_FILE_PAGE_JSON = ""
DIR_FILE_PAGE_NEW_JSON = ""
DIR_FIRST_PATH = "schedule/schedule"


def writeJSONFile():
    fileList = pathLib.Path.iterdir(pathLib.Path(DIR_FILE_BASE))
    listTotal = []

    # 遍历列表
    for filePath in fileList:
        fileJSON = pathLib.Path.open(filePath, mode="r+", encoding="UTF-8")
        strTemp = "  ".join(fileJSON.readlines())
        pageJSON = jsonUtils.loads(strTemp)
        listTemp = pageJSON.get("pages")
        for json in listTemp:
            json['path'] = pageJSON.get("root") + "/" + json['path']
        listTotal = listTotal + listTemp
        fileJSON.close()
        print("已经处理:", type(strTemp), filePath)
        pass

    # 定义原始文件
    fileJSONParent = pathLib.Path.open(pathLib.Path(pathLib.Path(DIR_FILE_PAGE_JSON)), mode="r+", encoding="UTF-8")
    # 读取json串字符
    listJSONParent = fileJSONParent.readlines()
    fileJSONParent.close()

    # 排序
    try:
        listTotal = sorted(listTotal, key=lambda entityJSON: entityJSON["path"].find(DIR_FIRST_PATH), reverse=True)
        print("已经排序")
    except:
        print("没有定义首个路由")

    # 生成 json对象
    pageJSONParent = jsonUtils.loads(" ".join(listJSONParent))
    # 添加路由列表属性
    pageJSONParent["pages"] = listTotal
    # 将 json转化为字符串
    jsonString = jsonUtils.dumps(pageJSONParent, ensure_ascii=False)

    # 定义文件对象
    fileWrite = open(pathLib.Path(DIR_FILE_PAGE_NEW_JSON), "w", encoding="UTF-8")
    # 写入json字符串到文件中
    fileWrite.write(jsonString)
    fileWrite.flush()

    fileWrite.close()

    print("完成!")

    pass

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('请输入json文件夹')
        author = QLabel('请输入 uniapp pages.json 位置')
        review = QLabel('请输入 新的 uniapp pages.json 位置')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QLineEdit()
        button = QPushButton("开始")
        self.button = button

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1)


        grid.addWidget(button, 4, 1)

        self.setLayout(grid)

        self.setGeometry(500, 300, 750, 700)
        self.setWindowTitle('Review')
        self.show()

        DIR_FILE_BASE = titleEdit.text()
        DIR_FILE_PAGE_JSON = authorEdit.text()
        DIR_FILE_PAGE_NEW_JSON = review.text()
        pass




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())