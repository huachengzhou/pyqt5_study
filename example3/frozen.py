import os
import sys


# 获取当前目录
def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  # 使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)  # 没打包前的py目录


#生成资源文件目录访问路径
def resource_path(relative_path):
    if hasattr(sys, 'frozen'):    #是否Bundle Resource
        base_path = sys._MEIPASS    #返回临时路径
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



# https://blog.csdn.net/weixin_44214830/article/details/118338380