import numpy as np 
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers 

from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense, Activation
from keras import optimizers

# TODO: working on create model 
def Create_RNN_Model(
    input_dim, # input dimension  
    output_dim, # output dimension 
    num_lstm_unit, # interal LSTM unit
    learning_rate, # learning rate
    optimizer
): 
    model = keras.Sequential()     
    model.add(layers.Embedding(input_dim=input_dim, output_dim=output_dim))

    # Add a LSTM layers with N unit  
    model.add(layers.LSTM(num_lstm_unit))

    # Add dense layer 
    # model.add(layers.Dense(10))

    # NOTICE: need further document research
    # model.compile(optimizer=Adam(lr=learning_rate), loss='mse')

    return model


class RNN: 
    def __init__(self, 
        input_dim, # input dimension  
        output_dim, # output dimension 
        num_lstm_unit, # interal LSTM unit
        learning_rate, # learning rate
        tie_weights=False, # based on TYING WORD VECTORS and .... 
    ): 
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.num_lstm_unit = num_lstm_unit

        # TODO: reference to the paper and implement here 
        # if tie_weights: 

    
    def model_info(self):
        # Print out summary of model architecture
        self.model.summary()
           
    # def forward(self): 

    # def train(self): 

    # def save_model(self,path,model_name): 

    # def load_model(self): 





