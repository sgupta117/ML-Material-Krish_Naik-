# -*- coding: utf-8 -*-
"""
Chapter 02 script 02
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)
#should see 2.0.0 or higher1.0
print(keras.__version__)
#should see 2.2.4 – tf

# the four different states of the XOR gate
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
 
# the four expected results in the same order
target_data = np.array([[0],[1],[1],[0]], "float32")

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[2]))
model.add(keras.layers.Dense(16, activation = 'sigmoid'))
model.add(keras.layers.Dense(16, activation = 'sigmoid'))
model.add(keras.layers.Dense(1, activation = 'sigmoid'))

model.summary()

model.layers

hidden1 = model.layers[1]
hidden1.name

model.get_layer('dense') is hidden1

weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape)

weights.shape

biases

biases.shape

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])

history = model.fit(training_data, target_data, epochs=750, verbose=2)

import pandas as pd
import matplotlib.pyplot as plt
 
pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()


print(model.predict(training_data).round())
