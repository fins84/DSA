import numpy as np

class DSAStack():
    def __init__(self):
        self.count = 0
        self.default_size = 100
        self.queue = np.empty(self.default_size, dtype=object)
    
    def getCount(self):
        return self.count

    def isEmpty(self):
        return_val = False
        if(self.count == 0):
            return_val = True
        
        return return_val

    def isFull(self):
        return_val = False
        if(self.count == self.default_size):
            return_val = True

        return return_val

    def push(self, value):
        if(self.isFull() == False):
            self.queue[self.count] = value
            self.count +=1

    def pop(self):
        topVal = self.top()
        if self.isEmpty() == False:
            self.count -=1
        return topVal

    def top(self):
        topVal = None
        if self.isEmpty() == False:
            topVal = self.queue[self.count -1]
        return topVal

    #call stack
    def display(self):
        for i in range(0, self.count):
            print(i,": ", self.queue[i], "\n")
