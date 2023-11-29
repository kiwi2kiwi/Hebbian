from Neuron import *

input = [1.5]
weights = [0.8,0.2]
target = [0.5]

n1 = Neuron()
n2 = output_Neuron()
inn = input_Neuron()
#n1.children_connections.append([n2,0.8])
inn.children_connections.append([n2,weights[0]])
n1.parent_connections.append([inn,weights[0]])
n1.children_connections.append([n2,weights[1]])
n2.parent_connections.append([n1,weights[1]])
#n1.parent_connections.append([inn,1])


def error_function(pre,tar):
    return (pre - tar)**2

def deriv_error_function(pre,tar):
    return 2*(pre - tar)

def compute_error():
    inn.set_input(input[0])
    inn.activation()
    n2.activation()
    print(n2.output)
    print("error: ", error_function(n2.output, target[0]))

def update_weights(weight):
    learning_rate = 0.1
#    a_null_durch_w = n2.deri_activation()
#    error_durch_a_null = deriv_error_function(n2.activation(),target[0])
#    error_durch_w = a_null_durch_w * error_durch_a_null
    n2.gradient_descent(deriv_error_function, target[0], learning_rate)

#    new_weight = weight - (learning_rate * error_durch_w)


#    n2.change_weight(new_weight)

#    print("weight: ", new_weight, " adjust: ", (weight - new_weight))
#    return new_weight


compute_error()
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
update_weights(weight)
print("end")