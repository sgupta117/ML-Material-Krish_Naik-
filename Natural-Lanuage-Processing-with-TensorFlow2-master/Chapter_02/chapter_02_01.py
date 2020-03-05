# -*- coding: utf-8 -*-
"""
Chapter 02 script 01
"""
import tensorflow as tf

W = tf.Variable(tf.ones(shape=(2,2)), name="W")
b = tf.Variable(tf.zeros(shape=(2)), name="b")
#define multiplication and addition operation as decorator function


def forward(x):
  return W * x + b
#evaluate TensorFlow graph
out_a = forward([1,0])
print(out_a)
