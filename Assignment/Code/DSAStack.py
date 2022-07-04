import numpy as np

#
#   DSAStack code taken and adapted from my prac 3 submission
#

"""
Name: DSAStack
Input: None
Function: Stack, top in top out
"""
class DSAStack():
    def __init__(self, size):
        self.count = 0
        self.default_size = size
        self.queue = np.empty(self.default_size, dtype=object)
    
    """
    Name: getCount
    Input: None
    Return: int count
    Function: returns number of values in stack
    """
    def getCount(self):
        return self.count

    """
    Name: isEmpty
    Input: none
    Return: bool return_val
    Function: check if stack is empty
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
    Function: check if stack is full
    """
    def isFull(self):
        return_val = False
        if(self.count == self.default_size):
            return_val = True

        return return_val

    """
    Name: push
    Input: object value
    Return: None
    Function: add to top of stack
    """
    def push(self, value):
        if(self.isFull() == False):
            self.queue[self.count] = value
            self.count +=1

    """
    Name: pop
    Input: None
    Return: object topVal
    Function: remove from top of queue and return it
    """
    def pop(self):
        topVal = self.top()
        if self.isEmpty() == False:
            self.count -=1
        return topVal

    """
    Name: top
    Input: None
    Return: object topVal
    Function: gets value from top of stack
    """
    def top(self):
        topVal = None
        if self.isEmpty() == False:
            topVal = self.queue[self.count -1]
        return topVal

    """
    Name: getStackList
    Input: None
    Return: array return_ray
    Function: getter converting stack into array
    """
    def getStackList(self):
        return_ray = np.empty(self.count, dtype=object)
        for i in range(0, self.count):
            return_ray[i] = self.queue[i]
        return return_ray

    """
    Name: display
    Input: None
    Return: None
    Function: prints all values in stack
    """
    #call stack
    def display(self):
        for i in range(0, self.count):
            print(i,": ", self.queue[i], "\n")
