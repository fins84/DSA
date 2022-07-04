class DSALinkedList():
    def __init__(self) -> None:
        self.count = 0
        self.start = None
        self.end = None
        self.max_nodes = 100
    
    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        return_val = None

        if self.current != None:
            return_val = self.current.getData()
            self.current = self.current.getNext()
        else:
            raise StopIteration
        return return_val

    def isEmpty(self):
        return_val = False
        if self.count == 0:
            return_val = True
        return return_val

    def isFull(self):
        return_val = False
        if self.count == 100:
            return_val = True
        return return_val

    def insertFirst(self, data):
        if self.count == 0:
            node = DSALinkedList_Node(data, None, None, self.count)
            self.start = node
            self.end = node
            self.count += 1
        elif self.isFull() == False:
            next = self.start
            node = DSALinkedList_Node(data, next, None, 0)
            self.count += 1
            self.start = node
            next.setPrev(node)
            for i in range(1, self.count, 1):
                node = node.getNext()
                node.setIndex(i)

    
    def insertLast(self, data):
        if self.count == 0:
            node = DSALinkedList_Node(data, None, None, self.count)
            self.start = node
            self.end = node
            self.count += 1
        elif self.isFull() == False:
            prev = self.end
            node = DSALinkedList_Node(data, None, prev, self.count)
            self.count += 1
            self.end = node
            prev.setNext(node)

    def peekFirst(self):
        return_val = self.start.getData()
        return return_val
    
    def peekLast(self):
        return_val = self.end.getData()
        return return_val

    def removeFirst(self):
        return_val = None
        if self.count >= 2:
            return_val = self.peekFirst()
            node = self.start.next
            node.setPrev(None)
            self.start = node
            self.count -= 1
        elif self.isEmpty() == False:
            return_val = self.peekFirst()
            self.start = None
            self.end = None
            self.count -= 1
        return return_val

    def removeLast(self):
        return_val = None
        if self.count >= 2:
            return_val = self.peekLast()
            node = self.end.prev
            node.setNext(None)
            self.end = node
            self.count -= 1
        elif self.isEmpty() == False:
            return_val = self.peekLast()
            self.start = None
            self.end = None
            self.count -= 1
        return return_val

    def getCount(self):
        return self.count

class DSALinkedList_Node():
    def __init__(self, data, next, prev, index):
        self.data = data
        self.next = next
        self.prev = prev
        self.index = index
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def getIndex(self):
        return self.index
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setIndex(self, index):
        self.index = index

if __name__ == "__main__":
    test = DSALinkedList()
    #for i in range(0, 11, 1):
    #    test.insertLast(i)
    #for i in range(0, 12, 1):
    #    print(test.removeLast())

    for i in range(1, 11, 1):
        test.insertLast(i)
    for data in test:
        print(data)