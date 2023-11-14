# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 12:50
# @Author  : Wyt
# @File    : camera_configs.py

import cv2
import numpy as np

# 左相机内参1
left_camera_matrix = np.array([[478.164263410335, 0, 269.870809749008],
                               [0, 479.894390965820, 230.586706557442],
                               [0, 0, 1]])

# 左相机畸变参数1
left_distortion = np.array(
    [[0.0720202844008067, -0.0240018687805291, 0.0, 0.0, 0.0]])

# 右相机内参1
right_camera_matrix = np.array([[474.753025170916, 0, 311.577501752326],
                                [0, 476.416208392632, 237.874213693502],
                                [0, 0, 1.0000]])

# 右相机畸变参数1
right_distortion = np.array(
    [[0.0713574201847601, -0.0324979545877006, 0, 0, 0]])

R = np.matrix([
    [0.999998304822596, 4.23866769458641e-05, -0.00184080289679108],
    [-4.03236447271575e-05, 0.999999371150131, 0.00112074678021802],
    [0.00184084924393413, -0.00112067065247138, 0.999997677682978],
])

T = np.array([-59.0061405175631, -0.177677759910340, -0.588519868643672])  # 平移关系向量

size = (480, 640)  # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
