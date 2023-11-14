# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 21:23
# @Author  : Wyt
# @File    : 单击拍照.py
# 打开摄像头实现拍照
import os
import camera_configs
import cv2
import argparse
from PIL import Image
from tqdm import tqdm

counter = 0
folder = ""


def shot(pos, frame):
    global counter, folder
    path = folder + pos + str(counter) + ".jpg"
    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)


def main():
    global counter, folder
    parser = argparse.ArgumentParser(description='对sourcedir中的图片进行压缩并保存到savedir目录')
    parser.add_argument('--videonum', type=int, default=1, help=' Image Source Directory ')
    parser.add_argument('--savedir', type=str, default="./imgtest/", help='Directory to save images')
    args = parser.parse_args()

    videonum = args.videonum
    folder = args.savedir  # 拍照文件目录
    counter = 0

    cv2.namedWindow("left")
    cv2.namedWindow("right")
    camera = cv2.VideoCapture(videonum, cv2.CAP_DSHOW)
    # 设置分辨率左右摄像机同一频率，同一设备ID；左右摄像机总分辨率2560x720；分割为两个1280x720
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = camera.read()
        print("ret:", ret)
        # 裁剪坐标为[y0:y1, x0:x1]    HEIGHT * WIDTH
        left_frame = frame[0:480, 0:640]
        right_frame = frame[0:480, 640:1280]

        # cv2.remap 重映射，就是把一幅图像中某位置的像素放置到另一个图片指定位置的过程。
        # 依据MATLAB测量数据重建无畸变图片
        # img1_rectified = cv2.remap(left_frame, camera_configs.left_map1, camera_configs.left_map2,
        #                            cv2.INTER_LINEAR)
        # img2_rectified = cv2.remap(right_frame, camera_configs.right_map1, camera_configs.right_map2,
        #                            cv2.INTER_LINEAR)

        cv2.imshow("left", left_frame)
        cv2.imshow("right", right_frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("s"):
            shot("left", left_frame)
            shot("right", right_frame)
            counter += 1
    camera.release()
    cv2.destroyWindow("left")
    cv2.destroyWindow("right")


if __name__ == '__main__':
    main()
