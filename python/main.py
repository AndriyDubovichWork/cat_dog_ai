from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
from os import listdir

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

tc =tf.feature_column

animals = ['Dog','Cat']

for animal in animals:
    folder_dir="G:/projects/cat_dog_ai/data/"+animal
    for image in os.listdir(folder_dir):
        if (image.endswith(".jpg")):
            print(image)