import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
# from tensorflow import keras
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model

import tensorflow.keras.backend as K
import logging
logging.getLogger('tensorflow').disabled = True

from variables import*
from util import get_data

'''
Use following command to run the script
        python main.py

'''

class TripRecommendation(object):
    def __init__(self, locations, rssi):
        self.X = rssi
        self.Y = locations
        self.num_classes = len(set(self.Y))
        print("num locations : {}".format(len(set(locations))))
        print("Input Shape : {}".format(self.X.shape))
        print("Label Shape : {}".format(self.Y.shape))

    def classifier(self):
        inputs = Input(shape=(n_features,), name='inputs')
        x = Dense(dense1, activation='relu', name='dense1')(inputs)
        x = Dense(dense2, activation='relu', name='dense2')(x)
        x = Dense(dense3, activation='relu', name='dense3')(x)
        x = Dropout(keep_prob)(x)
        outputs = Dense(self.num_classes, activation='softmax', name='output')(x)
        self.model = Model(inputs, outputs)

    def train(self):
        self.classifier()
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'],
        )
        self.history = self.model.fit(
                            self.X,
                            self.Y,
                            batch_size=batch_size,
                            epochs=num_epoches,
                            validation_split=validation_split
                            )

    def save_model(self):
        self.model.save(model_weights)

    def load_model(self):
        loaded_model = load_model(model_weights)
        loaded_model.compile(
                        loss='sparse_categorical_crossentropy',
                        optimizer='adam',
                        metrics=['accuracy']
                        )
        self.model = loaded_model

    def run(self):
        if os.path.exists(model_weights):
            print("Model Loading !!")
            # self.load_model()
        else:
            print("Model Training !!")
            self.classifier()
            self.train()
            self.save_model()

if __name__ == "__main__":
    locations, rssi = get_data()
    model = TripRecommendation(locations, rssi)
    model.run()