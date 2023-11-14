# -*- coding: utf-8 -*-
# @File     : change.py
# datetime  : 2023/11/12 18:23
# @Author   : 王永泰
# contact   : 1697556601@qq.com
# software  : PyCharm
"""
文件说明      :
"""

import os
from PIL import Image
from tqdm import tqdm

sourcepath = "Imageprocessing/left"
savepath = "VOCdevkit_fire/VOC2012/JPEGImages/"

imgquality = 50
count = 0
compress_num = 0

for _ in tqdm(os.listdir(str(sourcepath))):
    count = count + 1

pbar = tqdm(total=count)

while tqdm(count):
    img = Image.open('{0}/myimgleft{1}.jpg'.format(sourcepath, compress_num))
    if compress_num <= 9:
        img.save("{0}/00{1}.jpg".format(str(savepath), compress_num), quality=imgquality)
    elif compress_num <= 99:
        img.save("{0}/0{1}.jpg".format(str(savepath), compress_num), quality=imgquality)
    elif compress_num <= 999:
        img.save("{0}/{1}.jpg".format(str(savepath), compress_num), quality=imgquality)

    # if compress_num <= 9:
    #     os.rename('./okxml/00{0}.xml'.format(compress_num), './suceexml/000{0}.xml'.format(compress_num))
    # elif compress_num < 100:
    #     os.rename('./okxml/0{0}.xml'.format(compress_num), './suceexml/00{0}.xml'.format(compress_num))
    # elif compress_num <= 999:
    #     os.rename('./okxml/{0}.xml'.format(compress_num), './suceexml/0{0}.xml'.format(compress_num))

    compress_num += 1
    count -= 1
    pbar.update(1)
