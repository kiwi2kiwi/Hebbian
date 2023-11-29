# Hebbian
Looking for a set of rules that enables neurons to learn. 
1. Learning should not be goal oriented.
2. The network should decide by itself what it wants to learn.

Trying to make neurons that can learn by themselves without instructions from the outside. Each neuron should only receive information from the neurons it's connected to.
I would summarize this as "Autonomous neuron learning rules"
I haven't decided if I want to keep it unsupervised, semi-supervised or supervised.
Also haven't decided if the random distribution of neurons in a sphere between input and output should be kept or if a preexisting rough neuron structure is essential for the ability to learn on a certain dataset.
If you want to try this out but don't get it working or don't understand something, contact me and I'll add more comments for explanation.


What's currently implemented:
- Visualized in Matplotlib for easy debugging.
- There's a picture folder where for each tick a picture is taken. Active neurons and axons in red. If a new Axon is grown or its threshold is lowered it blinks in green. Unfortunately the green is not easily visible. Everything else is grey.
- Unsupervised
- Input from scikit 8 x 8 MNIST
- There are Neurons and their Axons
- The simulation is run in ticks
Neurons:
  - Processing neurons are scattered randomly in a distribution between output (Interactive) and input (Perceptive) neurons
  - has connections to other neurons (Axons)
  - when a neuron is depolarized with a signal it sends the signal to all other axons.
  - the depolarization of a neuron does not disappear after one tick but decays in a short time. 
    This short time window provides the ability for other adjacent neurons to further depolarize this neuron.
  
Axons:
  - connection between two neurons
  - can be depolarized by either of it's two neurons (bi-directional)
  - has a threshold. If the depolarization from its adjacent neurons surpasses the threshold, it will depolarize the other neuron after a delay that 
    is corresponding to the 3D distance between it's two neurons. Somehow looks like a ReLU activation function.
  - has a cooldown during which it cannot be depolarized again
  - if it's depolarized frequently within a time period, it's threshold for depolarization is lowered
  - after each image input, the threshold of every Axon is increased to simulate "Forgetting".
    If the threshold is too high, the Axon is removed. The Axon is not removed if either of its adjacent neurons have less than 3 Axons

Neuron space:
  - 3D space where neurons and axons exist. Current size is 100 x 100 x 100
  - Input (Perceptive) neurons exist on a Plane at x: -50
  - Output (Interactive) neurons exist on a Plane at x: +50
  - Processing neurons are randomly distributed in a sphere with radius 45
  - Axons are generated between Perceptive and Processing, Processing and Processing, Interactive and Processing.
    The never connect two Perceptive or two Interactive

Other general rules:
- If two neurons are repeatedly active at the same time, they wire together (Hebb: "fire together, wire together"). 
  Because I'm doing that in the Neuron_space class, the neurons technically do not connect on their own, violating the concept of not telling them what to do.
  It should instead be implemented in the neurons themselves.


What I'm working on:
- trying to normalize the signals
- Most axons died off by the 100th tick so I need to change some parameters. The goal is balancing "forgetting" and "strengthening" Axons. 
  Obviously axons should not "forget" when they are not constantly being used but still important.



Thoughts behind this experiment:
I started this after being frustrated by neural networks. Most projects don't benefit from deep learning, and you just end up shifting around hyperplanes in a hyperdimensional space.
Classical neural network architectures are rigid and will not change their architecture by themselves.

This network should change its architecture dynamically and without the need of a hierarchy between an outside observer and the neuron.
I'm looking for a set of basic instructions applicable to every neuron that enables them to autonomously arrange themselves according to the input.
The network should not be made to predict classes that an outside observer defines, but rather an output that the network itself defined as the best way to split the classes.
Usually in neural networks the target labels are always defining what the network learns, forcing the network to understand the data the same way the class labels do.
What if, to the network, the target labels do not provide the best way to understand and classify data?


If you use this for research or are interested, contact me because I'm very curious. 
Please do not use this for commercial purposes.
