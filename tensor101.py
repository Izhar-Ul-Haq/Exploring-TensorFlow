import tensorflow as tf
import numpy as np
import flask as fk
print(tf.__version__)
print(np.__version__)
print(fk.__version__)


x = tf.constant([[1., 2., 3.],
                 [4., 5., 6.]])

print(x)
print(x.shape)
print(x.dtype)

z = x + x
print(z)
