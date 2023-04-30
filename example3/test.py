#coding:utf-8
import sys
import os

import example3.frozen as  frozen


path1 = frozen.resource_path(os.path.join('res', 'a.txt'))
appPath = frozen.app_path()

print(path1)
print(appPath)

# pyinstaller -w test.py test.spec
# pyinstaller  -F test.py test.spec

os.system("pause")