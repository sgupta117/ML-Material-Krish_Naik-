# -*- coding: utf-8 -*-
"""
Chapter 02 script 02
"""

import tensorflow as tf
tf.constant(1) #scalar

tf.constant([[1., 2., 3.], [4., 5., 6.]]) #2 by 3 array

tf.constant(1.) + tf.constant(3.)  #addition operation

t = tf.constant([[1., 2., 3.], [4., 5., 6.]])

t

t[:, 1:]

t+5

t@tf.transpose(t)

tf.square(t)

a = np.array([1., 2., 3.])
tf.constant(a)

t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
t.numpy()
np.square(t)

tv = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
tv.assign(2*tv) 

tv[0, 1].assign(5)
