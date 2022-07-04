import numpy as np
#
#   DSAQueue taken and adapted from prac 3 submission
#

"""
Name: DSAQueue
Input: None
Function: allow for basic queue functionality
"""
class DSAQueue():
    def __init__(self, size):
        self.count = 0
        self.default_size = size
        self.queue = np.empty(self.default_size, dtype=object)
    
    """
    Name: getCount
    Input: None
    Return: int count
    Function: getter for count variable
    """
    def getCount(self):
        return self.count

    """
    Name: isEmpty
    Input: None
    Return: bool return_val
    Function: check if queue is empty
    """
    def isEmpty(self):
        return_val = False
        if(self.count == 0):
            return_val = True
        return return_val

    """
    Name: isFull
    Input: None
    Return: bool return_val
    Function: check if queue if full
    """
    def isFull(self):
        return_val = False
        if(self.count == self.default_size):
            return_val = True

        return return_val

"""
Name: DSARollingQueue
Input: None
Function: Queue where the removing from queue doesn't shuffle indexes forward
"""
class DSARollingQueue(DSAQueue):
    def __init__(self, size):
        super().__init__(size)
        self.start = 0
        self.end = 0

    """
    Name: peek
    Input: None
    Return: object frontVal
    Function: returns value at front of queue
    """
    def peek(self):
        frontVal = self.queue[self.start]
        return frontVal

    """
    Name: enqueue
    Input: object intVal
    Return: None
    Function: Adds to end of queue
    """
    def enqueue(self, intVal):
        if self.isFull() == False:
            if self.end>self.default_size-1:
                self.end = 0
            self.end += 1
            self.queue[self.end-1] = intVal
            self.count +=1

    """
    Name: dequeue
    Input: None
    Return: object return_val
    Function: removes from front of queue and returns value
    """
    def dequeue(self):
        return_val = None
        if self.isEmpty() == False:
            return_val = self.queue[self.start]
            self.start +=1
            if self.start > self.default_size-1:
                self.start = 0
            self.count -=1
        return return_val
                