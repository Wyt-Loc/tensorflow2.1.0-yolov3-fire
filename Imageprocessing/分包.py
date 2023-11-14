# -*- coding: utf-8 -*-
# @File     : 分包.py
# datetime  : 2023/11/12 15:21
# @Author   : 王永泰
# contact   : 1697556601@qq.com
# software  : PyCharm
"""
文件说明      :
"""

import os
from PIL import Image
from tqdm import tqdm

sourcepath = "./left"
savepath1 = "./one"
savepath2 = "./two"
savepath3 = "./three"
savepath4 = "./four"
imgquality = 50
count = 0
compress_num = 0

for _ in tqdm(os.listdir(str(sourcepath))):
    count = count + 1

pbar = tqdm(total=count)

while tqdm(count):
    img = Image.open('./left/myimgleft{0}.jpg'.format(compress_num))
    if compress_num <= 100:
        if compress_num <= 9:
            img.save("{0}/00{1}.jpg".format(str(savepath1), compress_num), quality=imgquality)
        elif compress_num <= 100:
            img.save("{0}/0{1}.jpg".format(str(savepath1), compress_num), quality=imgquality)
    elif compress_num <= 200:
        img.save("{0}/{1}.jpg".format(str(savepath2), compress_num), quality=imgquality)
    elif compress_num <= 300:
        img.save("{0}/{1}.jpg".format(str(savepath3), compress_num), quality=imgquality)
    elif compress_num > 300:
        img.save("{0}/{1}.jpg".format(str(savepath4), compress_num), quality=imgquality)
    compress_num += 1
    count -= 1
    pbar.update(1)
