import time
import random

import numpy as np

import Coordinates
import Processing_neuron

class Axon():
    # simulates the axon and its synapse
    def __init__(self, neuron1, neuron2, name, size, base_space, threshold = 0.65):#, signal = 0.7):
        super(Axon, self).__init__()
        self.cooldown = 30 # when signal successfully gets transmitted, how long does it take before the axon is ready again
        self.learning_time = 300 # if axon gets used 3 times during this learning time, the axon threshold gets lower, decay is lowered
        self.base_space = base_space
        self.first_signal = -600 #self.base_space.ticks-600
        self.second_signal = -600 #self.base_space.ticks-600
        self.third_signal = -600 #self.base_space.ticks-600
        # cooldown could also be implemented in the cell class
        self.neuron1 = neuron1
#        self.signal = signal # default 70 mV current that travels along the axon
        self.neuron2 = neuron2
        self.threshold = threshold
        self.last_signal = -40 #self.base_space.ticks - 40
        self.name = name
        if type(neuron1) != Processing_neuron.ProcessingNeuron or type(neuron2) != Processing_neuron.ProcessingNeuron:
            self.relevant_axon = True
        else:
            self.relevant_axon = False

        self.delay = Coordinates.clamp(int(np.log(Coordinates.distance_finder(neuron1.coordinates, neuron2.coordinates))),1,5)
#        print("length of axon: ", self.delay)
        self.decay = Coordinates.clamp(2*np.log(self.delay * (self.delay/size)*7), 0.85, 1)
        self.time_when_activated = 0
#        print("decay: ", self.decay)
        self.active = False

    def receive_signal(self, sourceNeuron, signal):
        if self.cooldown < (self.base_space.ticks - self.last_signal):
            if self.threshold < signal:# * self.decay:
                self.active = True
                self.time_when_activated = self.base_space.ticks
                self.base_space.active_axons[self.name] = self
                self.sourceNeuron = sourceNeuron
                #self.signal = signal

    def step(self):
        if self.time_when_activated == self.base_space.ticks - self.delay:
            if self.sourceNeuron == self.neuron1:
                self.neuron2.activation(self.neuron1, self.decay*1)
            else:
                self.neuron1.activation(self.neuron2, self.decay*1)
            self.third_signal = self.second_signal
            self.second_signal = self.first_signal
            self.first_signal = self.base_space.ticks
            self.last_signal = self.base_space.ticks
            if self.base_space.learn:
                if self.first_signal - self.third_signal < self.learning_time:
                    self.strengthen()
            self.active = False
            self.base_space.active_axons.pop(self.name)


        # send signal if

    def strengthen(self):
        self.threshold = self.threshold * 0.95
        #print(self.base_space.ticks, " axon grew threshold")
        self.base_space.grown_axons.append(self.name)

    def forget(self):
        self.threshold = Coordinates.clamp(self.threshold+0.05, 0.02,1)
        # Axon disappears because it was never used
        if not self.relevant_axon:
            if self.threshold == 1:
                self.base_space.to_remove.append(self)

    def randomize(self):
        self.threshold = self.threshold * random.uniform(0.8,1.2)

    def other_side(self, own):
        if own == self.neuron1:
            return self.neuron2
        return self.neuron1

    def reset_for_next_run(self):
        self.active = False

    def color_me(self, color="black"):
        value = self.base_space.axon_line_dict[self.name]
        if value[1].active:
            value[0][0].set_color(color)