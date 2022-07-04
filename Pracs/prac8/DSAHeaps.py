import numpy as np

class DSAHeaps():
    def __init__(self, heapSize):
        self.count = 0
        self.heapSize = heapSize
        self.heap = np.empty(heapSize, dtype=object)

    def add(self, priority, value):
        if self.count <= self.heapSize:
            self.heap[self.count] = DSAHeapEntry(priority, value)
            self.trickleUp(self.count)
            self.count += 1
        else:
            raise IndexError("Heap array is full")

    def trickleUp(self, curIdx):
        parentIdx = (curIdx-1)//2
        if curIdx > 0 and self.heap[curIdx].getPriority() > self.heap[parentIdx].getPriority():
            temp = self.heap[parentIdx]
            self.heap[parentIdx] = self.heap[curIdx]
            self.heap[curIdx] = temp
            self.trickleUp(parentIdx)

    def trickleDown(self, curIdx, numItems):

        lchildIdx = (curIdx * 2) + 1
        rchildIdx = (curIdx * 2) + 2
        keepGoing = True

        while keepGoing and lchildIdx<numItems:
            keepGoing = False
            largeIdx = lchildIdx
            if rchildIdx < numItems:
                if self.heap[lchildIdx].getPriority() < self.heap[rchildIdx].getPriority():
                    largeIdx = rchildIdx
            if self.heap[largeIdx].getPriority() > self.heap[curIdx].getPriority():
                self.swap(largeIdx, curIdx)
                keepGoing = True
            curIdx = largeIdx
            lchildIdx = (curIdx * 2) + 1
            rchildIdx = (curIdx *2) + 2

    def swap(self, largeIdx, curIdx):
        temp = self.heap[largeIdx]
        self.heap[largeIdx] = self.heap[curIdx]
        self.heap[curIdx] = temp

    def remove(self):
        return_val = self.heap[0]
        self.count -= 1
        self.heap[0] = self.heap[self.count]
        self.trickleDown(0, self.count)
        return return_val


    def heapify(self):
        numItems = self.count
        for ii in range((numItems//2)-1, -1, -1):
            self.trickleDown(ii, self.count)

    def heapSort(self):
        numItems = self.count
        self.heapify()
        for ii in range(numItems-1, 0, -1):
            self.swap(0, ii)
            self.trickleDown(0, ii)

    def display(self):
        for i in range(0, self.count, 1):
            print(self.heap[i].getPriority())

    def readFile(self, filename):
        try:
            with open(filename, "r") as f:
                for lines in f:
                    lett = lines.split(",")
                    try:
                        self.add(lett[0], lett[1])
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e, "Error reading file")


class DSAHeapEntry():
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def getPriority(self):
        return self.priority

    def getValue(self):
        return self.value

    def setPriority(self, priority):
        self.priority = priority

    def setValue(self, value):
        self.value = value


def testHarness():
    for i in range(test.count, 0, -1):
        print("Removing", i, "th element")
        print("remove output: ", test.remove().getPriority())
        test.display()

    def addValues():
        test.add(5,5)
        test.add(4,4)   
        test.add(3,3)
        test.add(11,11)
        test.add(10,10)
        test.add(3,3)
        test.add(2,2)
        test.add(16,16)
        test.add(12,12)
        test.display()
if __name__ == "__main__":
    test = DSAHeaps(7000)
    test.readFile("RandomNames7000.csv")
    #testHarness()


    print("Heap sort")
    test.heapSort()
    test.display()

    #testHarness()