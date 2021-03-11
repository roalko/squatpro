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
import tempfile




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('vid', type=str,
                        help='Your video')
    args = parser.parse_args()

    return args


def res_model():

    resnet50 = tf.keras.applications.ResNet50(include_top=False, weights='imagenet', input_shape=[256, 256, 3])
    resnet50.trainable = False
    feature = resnet50.output
    feature = tf.keras.layers.GlobalAveragePooling2D(name='feature')(feature)
    model_arch = tf.keras.Model(inputs=resnet50.input, outputs=feature)

    return model_arch


def get_feature_vector(model, input_frame):
    feature = model.predict(input_frame)
    return feature


def videos_to_features(model,video):

    csv_dict = {}
    feature_dim = model.output.shape[1]


    #fp = tempfile.TemporaryFile()
    #fp.write(video)
    with tempfile.NamedTemporaryFile(suffix='.mov', prefix='squat_temp_video', dir='/scripts/', delete=False) as temp:


        temp.write(video)

        temp.flush()

        cap = skvideo.io.vread(temp.name)


    for frame in cap:
        preprocessed_frame = cv2.resize(frame, (256, 256))
        preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)
        preprocessed_frame = tf.keras.applications.resnet.preprocess_input(preprocessed_frame)
        feature = list(get_feature_vector(model, preprocessed_frame)[0])

        for i, val in enumerate(feature):
            if f"feature_{str(i)}" in csv_dict:

                csv_dict[f"feature_{str(i)}"].append(val)
            else:
                csv_dict[f"feature_{str(i)}"] = [val]
    df = pd.DataFrame(csv_dict)

    temp.close()

    return df


model_arch = res_model()
my_model = keras.models.load_model('my_model')
my_model.load_weights("weights.h5")

def predict_test(video):


    X_test = videos_to_features(model_arch,video)
    X_test = X_test.values
    X_test_dim = np.expand_dims(X_test, axis=0)
    score = my_model.predict(X_test_dim)

        #REMOVE BEFORE DEPLOYEMENT!!!!!!!!
    '''print(f'Your Squat Score is {round(score[0][0]*100)}!')

    if score[0][0] < 0.5:

        print('Your form needs work')

    if score[0][0] >= 0.5:

        print('Congratulations, you squat like a PRO!')'''

    return score



if __name__ == '__main__':
    args = main()

    predict_test()



