import numpy as np

class DSAQueue():
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

class DSAShufflingQueue(DSAQueue):
    def __init__(self):
        super().__init__()

    def peek(self):
        frontVal = self.queue[0]
        return frontVal

    def enqueue(self,intVal):
        if self.isFull() == False:
            self.queue[self.count] = intVal
            self.count+=1
    
    def dequeue(self):
        frontVal = None
        if self.isEmpty() == False:
            frontVal = self.peek()
            for i in range(1,self.count):
                self.queue[i-1] = self.queue[i]

            self.count -=1            
        return frontVal

class DSARollingQueue(DSAQueue):
    def __init__(self):
        super().__init__()
        self.start = 0
        self.end = 0

    def peek(self):
        frontVal = self.queue[self.start]
        return frontVal

    def enqueue(self, intVal):
        if self.isFull() == False:
            if self.end>self.default_size-1:
                self.end = 0
            self.end += 1
            self.queue[self.end-1] = intVal
            self.count +=1

    def dequeue(self):
        return_val = None
        if self.isEmpty() == False:
            return_val = self.queue[self.start]
            self.start +=1
            if self.start > self.default_size-1:
                self.start = 0
            self.count -=1
        return return_val
                