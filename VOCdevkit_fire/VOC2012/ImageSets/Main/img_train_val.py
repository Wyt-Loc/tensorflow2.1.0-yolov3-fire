# -*- coding: utf-8 -*-
# @File     : img_train_val.py
# datetime  : 2023/11/12 17:51
# @Author   : 王永泰
# contact   : 1697556601@qq.com
# software  : PyCharm
"""
文件说明      :
"""

import os, glob

path = r"../../../../Imageprocessing/myxml/okxml"
path_list = os.listdir(path)
path_list.sort()
print(len(path_list))
for i in path_list[0:375]:
    print(i[:-4] + " -1")

for i in path_list[375:-1]:
    print(i[:-4] + " -1")
