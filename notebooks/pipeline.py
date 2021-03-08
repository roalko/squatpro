import sys
import cv2
import os
import math
import pandas as pd
import numpy as np
import tensorflow as tf
import csv
import skvideo.io
import argparse
from tensorflow.keras import Sequential, layers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.sequence import pad_sequences
import keras


INPUT_SHAPE = [256, 256, 3]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('vid', type=str,
                        help='Your video')
    args = parser.parse_args()

    return args



resnet50 = tf.keras.applications.ResNet50(include_top=False, weights='imagenet', input_shape=INPUT_SHAPE)
resnet50.trainable = False
feature = resnet50.output
feature = tf.keras.layers.GlobalAveragePooling2D(name='feature')(feature)
model_arch = tf.keras.Model(inputs=resnet50.input, outputs=feature)


def get_feature_vector(model, input_frame):
    feature = model.predict(input_frame)
    return feature


def videos_to_features(model,args):

    csv_dict = {}
    feature_dim = model.output.shape[1]
    cap = skvideo.io.vread(args.vid)

    for frame in cap:
        preprocessed_frame = cv2.resize(frame, (INPUT_SHAPE[0], INPUT_SHAPE[1]))
        preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)
        preprocessed_frame = tf.keras.applications.resnet.preprocess_input(preprocessed_frame)
        feature = list(get_feature_vector(model, preprocessed_frame)[0])

        for i, val in enumerate(feature):
            if f"feature_{str(i)}" in csv_dict:

                csv_dict[f"feature_{str(i)}"].append(val)
            else:
                csv_dict[f"feature_{str(i)}"] = [val]
    df = pd.DataFrame(csv_dict)

    return df




if __name__ == '__main__':
    args = main()

    X_test = videos_to_features(model_arch,args)

    my_model = keras.models.load_model('my_model')
    my_model.load_weights("weights.h5")
    X_test = X_test.values
    X_test_dim = np.expand_dims(X_test, axis=0)
    score = my_model.predict(X_test_dim)

    #REMOVE BEFORE DEPLOYEMENT!!!!!!!!
    print(f'Your Squat Score is {round(score[0][0]*100)}!')

    if score[0][0] < 0.5:

        print('Your form needs work')

    if score[0][0] >= 0.5:

        print('Congratulations, you squat like a PRO!')

