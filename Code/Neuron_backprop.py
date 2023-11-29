import numpy as np

class Neuron_backprop():
    def __init__(self):
        super(Neuron_backprop, self).__init__()
        self.parent_connections = [] # closer to input
        self.children_connections = [] # closer to output
        self.signals = []
        print("Hey, im a neuron!")

    def sigmoid(z):
        return 1. / (1 + np.exp(-z))

    def reset(self):
        self.signals = []

    def receive_signal(self, signal):
        self.signals.append(signal)

    def activation(self):
        activation = sum(self.parent_connections * self.signals) + bias
