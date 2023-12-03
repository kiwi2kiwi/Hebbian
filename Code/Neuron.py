import numpy as np
import random

class Neuron():
    def __init__(self):
        super(Neuron, self).__init__()
        self.parent_connections = [] # closer to input
        self.children_connections = [] # closer to output
        self.output = 0
        self.new_weight = 0
        self.activated = False
        print("Hey, im a neuron!")

    def reset_neuron(self):
        self.output = 0
        self.activated = False

    def wire(self):
        weight = round(random.uniform(0, 1), 2)
        for p in self.parent_connections:
            p[1] = weight
            p[0].children_connections.append([self, weight, 0])

    def change_weight(self):
        self.parent_connections[0][1] = self.new_weight
        self.parent_connections[0][0].children_connections[0][1] = self.new_weight


    def change_weight_old(self):
        self.parent_connections[0][1] = self.new_weight
        self.parent_connections[0][0].children_connections[0][1] = self.new_weight

    def get_weight(self):
        return self.parent_connections[0][1]

    def gradient_descent(self, bis_hier, learning_rate):

        ab_hier = self.a_null_a_eins() * bis_hier
        self.parent_connections[0][0].gradient_descent(ab_hier, learning_rate)

        error_durch_w = self.a_null_w_null() * bis_hier
        self.new_weight = self.get_weight() - (learning_rate * error_durch_w)
        print("weight: ", round(self.new_weight,2), " adjust: ", round(self.new_weight - self.get_weight(),2))
        self.change_weight()


    def activation_function(self, z):
        return z

    #        return 1. / (1 + np.exp(-z))

    def deri_activation_function(self, z):
        return z

    def activation(self):
        if self.activated:
            return self.output

        summation = 0
        for neuron, weight in self.parent_connections:
            summation += neuron.activation() * weight
        self.output = self.activation_function(summation)
        self.activated = True
        return self.output

    def deri_activation(self):
        summation = 0
        for neuron, weight in self.parent_connections:
            summation += neuron.deri_activation()
        return self.deri_activation_function(summation)

    def a_null_w_null(self):
        summation = 0
        for neuron, weight in self.parent_connections:
            summation += neuron.activation()
        return self.deri_activation_function(summation)

    def a_null_a_eins(self):
        summation = 0
        for neuron, weight in self.parent_connections:
            summation += weight
        return self.deri_activation_function(summation)



class input_Neuron():
    def __init__(self):
        super(input_Neuron, self).__init__()
        self.children_connections = [] # closer to output
        self.output = 0
        self.activated = False

    def gradient_descent(self, a, b):
        pass

    def set_input(self, input):
        self.activated = True
        self.output = input

    def activation_function(z):
        return 1. / (1 + np.exp(-z))

    def activation(self):
        return self.output

    def deri_activation(self):
        return self.output

    def reset_neuron(self):
        self.output = 0
        self.activated = False