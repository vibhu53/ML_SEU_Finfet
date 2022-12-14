# -*- coding: utf-8 -*-
"""Id_prediction_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ylRYsHuf-ukFB_axW5w_vlhTaJ5dPOn

### Neural Network
"""

#Importing Libraries for data preparation
import pandas as pd
import numpy as np
#Read Necessary files
dataset = pd.read_csv("datasetall.csv")

dataset = np.asmatrix(dataset)

Y_data = dataset[:,4]
X_data = dataset[:,:-1]

X_data_norma1 = dataset[:,3]
X_data_norma1 = X_data_norma1/X_data_norma1.max()
X_data[:,3] = X_data_norma1
Y_max = Y_data.max()
Y_data = Y_data/Y_data.max()

X_data = pd.DataFrame(X_data)
Y_data = pd.DataFrame(Y_data)

"""Split in training and testing data"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.10, random_state=42)

print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

"""ANN model"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define model
model = keras.Sequential()
model.add(layers.Dense(8, input_dim=4, activation= "relu"))
model.add(layers.Dense(8, activation= "relu"))
model.add(layers.Dense(1))
model.summary() #Print model Summary

# Compile model
model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])

model.fit(X_train, Y_train, epochs=100)

"""Inference """

from sklearn.metrics import mean_squared_error
pred= model.predict(X_test)
score = np.sqrt(mean_squared_error(Y_test,pred))
print (score)

print(pred*Y_max)
print(Y_test*Y_max)



"""### Random Forest Regressor"""

from tensorflow.python.ops.gen_array_ops import reshape
import random
from sklearn.ensemble import RandomForestRegressor
random.seed(42)

rf = RandomForestRegressor(n_estimators=10)
rf.fit(X_train, Y_train.values.ravel())

predrf=rf.predict(X_test)
score = np.sqrt(mean_squared_error(Y_test,predrf))
print (score)

