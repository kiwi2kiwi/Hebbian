import random
from Neuron import *

input = [1.5]
weights = [0.8,0.2,0.5]
target = [0.5]
input_layer = [input_Neuron()]

'''
n1 = Neuron()
n2 = Neuron()

i1.children_connections.append([n1, weights[0]])
n1.parent_connections.append([i1, weights[0]])
n1.children_connections.append([n2, weights[1]])
n2.parent_connections.append([n1, weights[1]])

active_neurons = [n1,n2]
'''


weights = []

layer_layout = [[1],[1],[1],[1]]

layers = []
active_neurons = []
for idx, l in enumerate(layer_layout):
    layer = []
    for neur in l:
        n = Neuron()

        if idx == 0:
            for i in input_layer:
                n.parent_connections.append([i, 100])
        else:
            for i in layers[idx-1]:
                n.parent_connections.append([i, 100])
        layer.append(n)
    layers.append(layer)

for layer in layers:
    for n in layer:
        n.wire()



def error_function(pre,tar):
    return round((pre - tar)**2,3)

def deriv_error_function(pre,tar):
    return 2*(pre - tar)

def compute_error():
    input_layer[0].set_input(input[0])
    for n in layers[-1]:
        pred = n.activation()
        print("error: ", error_function(pred, target[0]))

def backprop():
    compute_error()
    learning_rate = 0.1
    for n in layers[-1]:
        error_through_a_zero = deriv_error_function(n.activation(), target[-1])
        n.gradient_descent(error_through_a_zero, learning_rate)


#    new_weight = weight - (learning_rate * error_durch_w)


backprop()
backprop()
backprop()

print("end")