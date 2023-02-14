import os

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


number = tf.Variable([123.2],tf.float64)

print(number)
