import numpy as np

class Neuron():
    def __init__(self):
        super(Neuron, self).__init__()
        self.parent_connections = [] # closer to input
        self.children_connections = [] # closer to output
        self.signals = []
        self.output = 0
        print("Hey, im a neuron!")

        def change_weight(self, w):
            self.parent_connections[0][1] = w
            self.parent_connections[0].children_connections[0][1] = w

        def get_weight(self):
            return self.parent_connections[0][1]

        def gradient_descent(self, error_durch_a_null, learning_rate):
            a_durch_w = self.deri_activation()
            #error_durch_a_null = deriv_error_function(self.activation(), target)
            error_durch_w = a_durch_w * error_durch_a_null
            new_weight = self.get_weight() - (learning_rate * error_durch_w)
            print("weight: ", new_weight, " adjust: ", (self.get_weight() - new_weight))
            self.change_weight(new_weight)

        def activation_function(self, z):
            return z

        #        return 1. / (1 + np.exp(-z))

        def deri_activation_function(self, z):
            return z

        def activation(self):
            summation = 0
            for neuron, weight in self.parent_connections:
                summation += neuron.activation() * weight
            self.output = self.activation_function(summation)
            return self.output

        def deri_activation(self):
            summation = 0
            for neuron, weight in self.parent_connections:
                summation += neuron.deri_activation()
            return self.deri_activation_function(summation)



class input_Neuron():
    def __init__(self):
        super(input_Neuron, self).__init__()
        self.children_connections = [] # closer to output
        self.output = 0

    def set_input(self, input):
        self.output = input

    def activation_function(z):
        return 1. / (1 + np.exp(-z))

    def activation(self):
        return self.output

    def deri_activation(self):
        return self.output



class output_Neuron():
    def __init__(self):
        super(output_Neuron, self).__init__()
        self.parent_connections = [] # closer to output
        self.output = 0

    def change_weight(self, w):
        self.parent_connections[0][1] = w
        self.parent_connections[0][0].children_connections[0][1] = w

    def get_weight(self):
        return self.parent_connections[0][1]

    def gradient_descent(self, deriv_error_function, target, learning_rate):
        a_null_durch_w = self.deri_activation()
        error_durch_a_null = deriv_error_function(self.activation(), target)
        self.parent_connections[0][0].gradient_descent(error_durch_a_null, learning_rate)

        error_durch_w = a_null_durch_w * error_durch_a_null
        new_weight = self.get_weight() - (learning_rate * error_durch_w)
        print("weight: ", new_weight, " adjust: ", (self.get_weight() - new_weight))
        self.change_weight(new_weight)

    def activation_function(self,z):
        return z
#        return 1. / (1 + np.exp(-z))

    def deri_activation_function(self,z):
        return z

    def activation(self):
        summation = 0
        for neuron, weight in self.parent_connections:
            summation += neuron.activation() * weight
        self.output = self.activation_function(summation)
        return self.output

    def deri_activation(self):
        summation = 0
        for neuron, weight in self.parent_connections:
            summation += neuron.deri_activation()
        return self.deri_activation_function(summation)