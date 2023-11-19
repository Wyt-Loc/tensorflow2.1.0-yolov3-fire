# -*- coding: utf-8 -*-
# @File     : mydetect.py
# datetime  : 2023/11/17 15:58
# @Author   : 王永泰
# contact   : 1697556601@qq.com
# software  : PyCharm
"""
文件说明      :
"""
import os
import time
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images, load_tfrecord_dataset
from yolov3_tf2.utils import draw_outputs


# flags.DEFINE_string('classes', './data/fire_voc2012.names', 'path to classes file')
# flags.DEFINE_string('weights', './checkpoints/yolov3_train_18.tf',
#                     'path to weights file')
# flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
# flags.DEFINE_integer('size', 416, 'resize images to')
# flags.DEFINE_string('image', '../Imagetransmission/RecognizingImages/rece.jpg', 'path to input image')
# flags.DEFINE_string('tfrecord', None, 'tfrecord instead of image')
# flags.DEFINE_string('output', './output.jpg', 'path to output image')
# flags.DEFINE_integer('num_classes', 2, 'number of classes in the model')


def main(_argv):
    js = 0
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

    yolo = YoloV3(classes=2)
    yolo.load_weights('./checkpoints/yolov3_train_18.tf').expect_partial()
    logging.info('weights loaded')

    class_names = [c.strip() for c in open('./data/fire_voc2012.names').readlines()]
    logging.info('classes loaded')

    while True:
        print("执行了几次了\n")
        with open(r"F:\CreatCar\wyt_data\Python\tensorflow\Imagetransmission\RecognizingImages\isok.txt", 'r+',
                  encoding='utf-8') as f:
            data = f.readline()
            if data == "2":
                f.close()
                file = open(r"F:\CreatCar\wyt_data\Python\tensorflow\Imagetransmission\RecognizingImages\isok.txt", "w")
                file.write('0')
                file.close()
                print("写入0")
                time.sleep(1)
            else:
                f.close()
                time.sleep(1)
        try:
            img_raw = tf.image.decode_image(
                open(r'../Imagetransmission/RecognizingImages/rece{}.jpg'.format(js), 'rb').read(),
                channels=3)
            js += 1
        except IOError:
            print("丢包\n")

        img = tf.expand_dims(img_raw, 0)
        img = transform_images(img, 416)

        t1 = time.time()
        boxes, scores, classes, nums = yolo(img)
        t2 = time.time()
        logging.info('time: {}'.format(t2 - t1))

        logging.info('detections:')
        for i in range(nums[0]):
            logging.info('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
                                               np.array(scores[0][i]),
                                               np.array(boxes[0][i])))

        img = cv2.cvtColor(img_raw.numpy(), cv2.COLOR_RGB2BGR)
        img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
        cv2.imwrite('./output{}.jpg'.format(js), img)

        logging.info('output saved to: {0}{1}'.format('./output.jpg', js))

        # 处理完一次删除本次
        # os.remove()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
