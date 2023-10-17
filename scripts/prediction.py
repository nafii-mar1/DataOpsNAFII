import pandas as pd
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
import cv2


def predict_funct(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 256))
    loaded_model = tf.keras.models.load_model('model_balanced.h5')
    input_image = np.expand_dims(image, axis=0)
    pred = loaded_model.predict(input_image)
    pred=pred[0,0]
    if pred<0.5:
        pred="normal"
    else:
        pred="not normal"
    return pred