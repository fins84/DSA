#
#   Linked List code taken and adapted from my prac 4 code
#

"""
Name: DSALinkedList
Input: None
Function: provide a linked list to store complex data
"""
class DSALinkedList():
    def __init__(self) -> None:
        self.count = 0
        self.start = None
        self.end = None
        self.max_nodes = 100000
    
    """
    Name: __iter__
    Input: None
    Return: self
    Function: Iterate through each value in linked list (allows for 'for data in linkedlist' statements)
    """
    def __iter__(self):
        currND = self.start
        while currND is not None:
            yield currND.getData()
            currND = currND.getNext()
        return self
    """
    Name: isEmpty
    Input: None
    Return: bool return_value
    Function: True or false if the linked list has values in it
    """
    def isEmpty(self):
        return_val = False
        if self.count == 0:
            return_val = True
        return return_val

    """
    Name: isFull
    Input: None
    Return: bool return_val
    Function: True or false if linked list is full or not
    """
    def isFull(self):
        return_val = False
        if self.count == self.max_nodes:
            return_val = True
        return return_val

    """
    Name: insertFirst
    Input: object data
    Return: None
    Function: insert data into first index and push all data back 1 index
    """
    def insertFirst(self, data):
        if self.count == 0:
            #count == 0, create new index with start and end pointing to it
            node = DSALinkedList_Node(data, None, None, self.count)
            self.start = node
            self.end = node
            self.count += 1
        elif self.isFull() == False:
            #count != 0, create new index with prev pointing to first index
            next = self.start
            node = DSALinkedList_Node(data, next, None, 0)
            self.count += 1
            self.start = node
            next.setPrev(node)
            for i in range(1, self.count, 1):
                node = node.getNext()
                node.setIndex(i)

    """
    Name: insertlast
    Input: object data
    Return: None
    Function: insert data into a node at end of linked list
    """
    def insertLast(self, data):
        if self.count == 0:
            #count == 0, create new index with start and end pointing to it
            node = DSALinkedList_Node(data, None, None, self.count)
            self.start = node
            self.end = node
            self.count += 1
        elif self.isFull() == False:
            #count != 0, create new index with prev pointing to last index
            prev = self.end
            node = DSALinkedList_Node(data, None, prev, self.count)
            self.count += 1
            self.end = node
            prev.setNext(node)

    """
    Name: peekFirst
    Input: None
    Return: object return_val
    Function: return the data contained in first index of linked list
    """
    def peekFirst(self):
        return_val = self.start.getData()
        return return_val

    """
    Name: peeklast
    Input: None
    Return: object return_val
    Function: return the data contained in the last index of linked list
    """
    def peekLast(self):
        return_val = self.end.getData()
        return return_val

    """
    Name: removeFirst
    Input: None
    Return: object return_val
    Function: delete first val in linked list and return its data
    """
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

    """
    Name: removeLast
    Input: None
    Return: object return_val
    Function: delete last val in linked list and return its data
    """
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

    """
    Name: removeNode
    Input: int index
    Return: None
    Function: remove node in index position in linked list
    """
    def removeNode(self, index):
        if index == 0:
            self.removeFirst()
        elif index == self.end.getIndex():
            self.removeLast()
        else:
            node = self.start
            if self.end.getIndex() > index and index >= 0:
                while node.getIndex() != index:
                    node = node.getNext()

            prev = node.getPrev()
            next = node.getNext()

            prev.next = next
            next.prev = prev

    """
    Name: getCount
    Input: None
    Return: int count
    Function: gets number of indexes in linked list
    """
    def getCount(self):
        return self.count

"""
Name: DSALinkedList_Node
Input: object data, DSALinkedList_Node next, DSALinkedList_Node prev, int index
Function: stores the data for each index in linked list including next and previous index references
 """
class DSALinkedList_Node():
    def __init__(self, data, next, prev, index):
        self.data = data
        self.next = next
        self.prev = prev
        self.index = index
    
    """
    Name: getData
    Input: None
    Return: object Data
    Function: getter function for data variable
    """
    def getData(self):
        return self.data

    """
    Name: getNext
    Input: None
    Return: object next
    Function: getter for next index in linked list
    """
    def getNext(self):
        return self.next
    
    """
    Name: getPrev
    Input: None
    Return: object prev
    Function: getter for prev index in linked list 
    """
    def getPrev(self):
        return self.prev
    
    """
    Name: getIndex
    Input: None
    Return: int index
    Function: getter for index variable
    """
    def getIndex(self):
        return self.index
    
    """
    Name: setData
    Input: object data
    Return: None
    Function: setter for data variable
    """
    def setData(self, data):
        self.data = data

    """
    Name: setNext
    Input: object next
    Return: None
    Function: setter for next variable
    """
    def setNext(self, next):
        self.next = next

    """
    Name: setPrev
    Input: object prev
    Return: None
    Function: setter for prev variable
    """
    def setPrev(self, prev):
        self.prev = prev

    """
    Name: setIndex
    Input: int index
    Return: None
    Function: setter for index variable
    """
    def setIndex(self, index):
        self.index = index

if __name__ == "__main__":
    test = DSALinkedList()
    for i in range(0, 11, 1):
        test.insertLast(i)
    for i in range(0, 12, 1):
        print(test.removeLast())

    for i in range(1, 11, 1):
        test.insertLast(i)
    for data in test:
        print(data)