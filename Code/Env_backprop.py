import numpy as np
import random
random.seed(1)
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from Neuron_backprop import Neuron_backprop

class Env_backprop():
    def __init__(self, x, y, z):
        super(Env_backprop, self).__init__()
        self.x = x
        self.y = y
        self.z = z

    def spawn_neurons(self):
        self.input_layer = [Neuron_backprop(),Neuron_backprop(),Neuron_backprop(),Neuron_backprop()]
        self.output_layer = [Neuron_backprop()]
        for inp_neu in self.input_layer:
            for out_neu in self.output_layer:
                inp_neu.children_connections.append(out_neu)
        for out_neu in self.output_layer:
            out_neu.parent_connections = self.input_layer
        print("neurons spawned!")

    def forward_pass(self, input_data):
        # here i insert data into the input neurons
        for d,neuron in zip(input_data,self.input_layer):
            neuron.activate(d)

        # here i start passing the data through the neurons
            for
        print("forward passed!")

    def backward_pass(self):
        print("backward passed!")


neuronspace = Env_backprop()
from sklearn import datasets
from sklearn import preprocessing
import pandas as pd
min_max_scaler = preprocessing.MinMaxScaler()
#training data
df = pd.DataFrame(datasets.load_digits().data)
#fit and transform the training data and use them for the model training
df1 = min_max_scaler.fit_transform(df)
digits = datasets.load_digits()
images = 0

print("Sensing images \n"
      "Symptoms: \n"
      "-Quick decay of axons \n"
      "-Activation function is the binary step function to simulate synapse transmitting signals \n"
      "-Not emergent")

for d,t in zip(df1, digits.target):
    #neuronspace.generate_image(d, t)
    print("durchgang ", images, " start tick: ", neuronspace.ticks)
    neuronspace.feed_image_unsupervised(d, t, learn = True)
    images += 1
    if images == 20:
        print("stop")
    if images == 10:
        print("stop")
        neuronspace.Visualization = True
        plt.ion()
        neuronspace.start_vis()


print("check")