import random
from Neuron import *

input = [1.5]
weights = [0.8,0.2,0.5]
target = [0.5]

n1 = Neuron()
n2 = Neuron()
i1 = input_Neuron()

i1.children_connections.append([n1, weights[0]])
n1.parent_connections.append([i1, weights[0]])
n1.children_connections.append([n2, weights[1]])
n2.parent_connections.append([n1, weights[1]])

active_neurons = [n1,n2]
'''
weights = []
layers = 2

for i in range(layers):
    weights.append(round(random.uniform(0,1),2))


for i in range(layers):
    n = Neuron
    active_neurons.append(n)

active_neurons.append(o1)
'''
#inn.children_connections.append([n2,weights[0]])
#n2.parent_connections.append([inn,weights[0]])




def error_function(pre,tar):
    return round((pre - tar)**2,3)

def deriv_error_function(pre,tar):
    return 2*(pre - tar)

def compute_error():
    i1.set_input(input[0])
    active_neurons[-1].activation()
    print("error: ", error_function(active_neurons[-1].activation(), target[0]))

def backprop():
    compute_error()
    learning_rate = 0.1
#    a_null_durch_w = n2.deri_activation()
#    error_durch_a_null = deriv_error_function(n2.activation(),target[0])
#    error_durch_w = a_null_durch_w * error_durch_a_null
    error_through_a_zero = deriv_error_function(active_neurons[-1].activation(), target[-1])
    active_neurons[-1].gradient_descent(error_through_a_zero, learning_rate)

#    new_weight = weight - (learning_rate * error_durch_w)

def change_weights():
    [n.change_weight() for n in active_neurons]
#    n2.change_weight(new_weight)

#    print("weight: ", new_weight, " adjust: ", (weight - new_weight))
#    return new_weight


backprop()
change_weights()
backprop()
change_weights()
backprop()
change_weights()
backprop()
change_weights()
backprop()
change_weights()
backprop()
change_weights()
backprop()
change_weights()
print("end")