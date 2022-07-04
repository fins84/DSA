import linkedLists as linked

class DSAQueue():
    def __init__(self):
        self.count = 0
        self.default_size = 100
        self.queue = linked.DSALinkedList()
    
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
        frontVal = self.queue.peekFirst()
        return frontVal

    def enqueue(self,intVal):
        if self.isFull() == False:
            self.queue.insertLast(intVal)
            self.count+=1
    
    def dequeue(self):
        frontVal = None
        if self.isEmpty() == False:
            frontVal = self.queue.removeFirst()
            self.count -=1            
        return frontVal
