import numpy as np

class Connection():
    def __init__(self):
        super(Connection, self).__init__()
        self.parent = [] # closer to input
        self.child = [] # closer to output
        self.weight = np.random.uniform(0,1,1)
        print("Hey, im a connection with random weight! ", self.weight)


