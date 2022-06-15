# Hebbian
Trying to make neurons that can learn by themself without instructions from the outside. Each neuron should only receive information from the neurons it's connected to.
I haven't decided if i want to keep it unsupervised, semi-supervised or supervised.
What's currently implemented:
- Unsupervised
- Input from scikit 8 x 8 MNIST
- There are Neurons and their Axons
- neurons:
  - when a neuron is depolarized with a signal it sends the signal to all other axons
  - the depolarization of a neuron does not disappear after one tick but decays in a short time. 
    This short time window provides the ability for other adjacent neurons to further depolarize this neuron.
  
- axons:







Classical neural network architectures are rigid and will not change their architecture by themselves.
This network is supposed to be "anarchist" in the sense of providing general rules that are the same for every neuron. 
With these rules it should be able to learn how to learn better. 
It should change it's architecture dynamically and without the need of a hierarchy between an outside observer and the neuron.

I'm looking for a set of basic instructions applicable to every neuron that enables them to autonomically arrange themselves according to the input.
The network should not be made to predict an classes that an outside observer defines, but rather an output that the network itself defined as the best way to split the classes.
Usually in neural networks the target lables are always defining what the network learnes, forcing the network to understand the data the same way the class lables do.
What if, to the network, the target lables do not provide the best way to understand and classify data?


If you use this for research, cite and contact me because i'm very curious. 
Please do not use this for commercial purposes. If you somehow make money from it, please send it to charity.
