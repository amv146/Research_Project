from os import name
from keras.models import Sequential
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.layers.normalization import BatchNormalization
from ResidualLayer import ResidualLayer

class ResidualFCNetwork(keras.Model):
    def __init__(self, num_first_blocks, num_second_blocks, num_neurons, num_inputs, num_outputs):
        super(ResidualFCNetwork, self).__init__()

        self.input_block = keras.Input(shape=(num_inputs,))

        self.first_blocks = Sequential(name="FirstBlocks")

        for i in range(0, num_first_blocks):
            self.add_residual_block(self.first_blocks, num_inputs)

        self.intermediate_block = Sequential([
            BatchNormalization(), 
            Dense(num_neurons, activation="relu")])

        self.second_blocks = Sequential(name="SecondBlocks")

        for i in range(0, num_second_blocks):
            self.add_residual_block(self.second_blocks, num_neurons)

        self.output_block = Sequential([
            tf.keras.layers.BatchNormalization(),
            Dense(num_outputs, activation='sigmoid')
        ])

    def call(self, inputs, training):

        x = self.first_blocks(inputs)
        x = self.intermediate_block(x)
        x = self.second_blocks(x)
        x = self.output_block(x)

        return x

    def add_residual_block(self, modules, num_neurons):
        layers = Sequential([
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dense(num_neurons, activation=tf.keras.layers.LeakyReLU())
        ])

        modules.add(ResidualLayer(layers))