import numpy as np 
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers 


def Create_RNN_Model(
    input_dim, # input dimension  
    output_dim, # output dimension 
    num_lstm_unit, # interal LSTM unit
): 
    model = keras.Sequential()     
    model.add(layers.Embedding(input_dim=input_dim, output_dim=output_dim))

    # Add a LSTM layers with N unit  
    model.add(layers.LSTM(num_lstm_unit))


    # Add dense layer 
    # model.add(layers.Dense(10))

    # Print out summary of model architecture
    model.summary()

    return model





