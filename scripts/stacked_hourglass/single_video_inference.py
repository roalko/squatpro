import cv2
import sys
import os
import numpy as np
import cv2
import pandas as pd
import csv

from hourglass import HourglassNet
from mpii_datagen import MPIIDataGen
from data_process import *


def load_model(model_json, model_weights, img, threshold = 0.05, num_stack = 2, num_class = 16, tiny = False):
    if tiny:
        xnet = HourglassNet(num_classes = num_class, num_stacks = num_stack, num_channels = 128, inres = (192, 192), outres = (48, 48))
    else:
        xnet = HourglassNet(num_classes = num_class, num_stacks = num_stack, num_channels = 256, inres = (256, 256), outres = (64, 64))

    xnet.load_model(model_json, model_weights)
    return xnet

def inference(xnet, model_json, model_weights, img, threshold = 0.05, num_stack = 2, num_class = 16, tiny = False):
    out, scale = xnet.inference_file(img)
    keypoints = post_process_heatmap(out[0, :, :, :])
    #ignore_kps = ['plevis', 'thorax', 'head_top']
    ignore_kps = []
    kp_keys = MPIIDataGen.get_kp_keys()

    mkps = []
    for i, keypoint in enumerate(keypoints):
        if kp_keys[i] in ignore_kps:
            conf = 0.0
        else:
            conf = 0.9
        mkps.append((4*scale[1]*keypoint[0], 4*scale[0]*keypoint[1], conf))

    coor_dict = {}
    key = 0
    for i in mkps:
        x,y = i[0],i[1]
        coor_dict[key] = x
        key+=1
        coor_dict[key] = y
        key+=1


    #im = cv2.imread(img)
    #x, y = int(mkps[0][0]), int(mkps[0][1])
    #im = cv2.circle(im, (x,y), radius=10, color=(0, 0, 255), thickness=-1)
    #cv2.imshow('output', im)
    #cv2.waitKey()
    #print(keypoints)
    #input('k')


    frame = render_connections(cv2.imread(img), mkps, kp_keys, connections)
    frame = render_joints(frame, mkps, threshold)

    return frame , coor_dict

model_json = '../../raw_data/trained_model/hg_s2_b1/net_arch.json'
model_weights = '../../raw_data/trained_model/hg_s2_b1/weights_epoch96.h5'
connections = [(0, 1), (1, 2), (2, 6), (3, 6), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (8, 12), (12, 11), (11, 10), (8, 13), (13, 14), (14, 15)]


for vid_num in range(100,101):
    video_path = f'../../raw_data/vids/{vid_num}.mov'
    cap = cv2.VideoCapture(video_path)

    if cap.isOpened() is False:
        print("Error opening video stream or file")


    xnet = load_model(model_json = model_json, model_weights = model_weights, img = '../../raw_data/out.jpg')

    coordinates = []
    while cap.isOpened():
        ret_val, input_image = cap.read()
        if ret_val ==True:
            cv2.imwrite('../../raw_data/out.jpg', input_image)
            frame, coor_dict = inference(xnet=xnet, model_json = model_json, model_weights = model_weights, img = '../../raw_data/out.jpg')
            coordinates.append(coor_dict)
        else:
            break

    print(f'../../raw_data/CSV_Files/{vid_num}.csv')
    with open(f'../../raw_data/CSV_Files/{vid_num}.csv', 'w') as output_file:
        fc = csv.DictWriter(output_file,fieldnames=coordinates[0].keys())
        fc.writeheader()
        fc.writerows(coordinates)

