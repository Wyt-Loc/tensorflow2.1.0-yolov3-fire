# -*- coding: utf-8 -*-
# @File     : compress.py
# datetime  : 2023/11/12 11:22
# @Author   : 王永泰
# contact   : 1697556601@qq.com
# software  : PyCharm
"""
文件说明      :将指定文件目录的所有图片大小长宽不变的情况下进行压缩处理，
             并保存到新的目录下。
"""

import os
import argparse
from PIL import Image
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(description='对sourcedir中的图片进行压缩并保存到savedir目录')
    parser.add_argument('--sourcedir', type=str, default="./left", help=' Image Source Directory ')
    parser.add_argument('--savedir', type=str, default="./left1", help='Directory to save the compressed images')
    args = parser.parse_args()

    print("sourcedir = ", args.sourcedir)
    print("savedir = ", args.savedir)

    sourcepath = args.sourcedir
    savepath = args.savedir

    compress_num = 0
    count = 0
    imgquality = 50

    for _ in tqdm(os.listdir(str(sourcepath))):
        count = count + 1

    pbar = tqdm(total=count)

    while count:
        img = Image.open('./left/myimgleft{0}.jpg'.format(compress_num))
        if compress_num < 10:
            img.save("{0}/00{1}.jpg".format(str(savepath), compress_num), quality=imgquality)
        elif compress_num < 100:
            img.save("{0}/0{1}.jpg".format(str(savepath), compress_num), quality=imgquality)
        else:
            img.save("{0}/{1}.jpg".format(str(savepath), compress_num), quality=imgquality)

        compress_num += 1
        count -= 1
        pbar.update(1)


if __name__ == '__main__':
    main()
