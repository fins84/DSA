import numpy as np

class DSAHeaps():
    def __init__(self, heapSize):
        self.count = 0
        self.heapSize = heapSize
        self.heap = np.empty(heapSize, dtype=object)

    def add(self, priority, value):
        if self.count <= self.heapSize:
            self.heap[self.count] = DSAHeapEntry(priority, value)
            self.count += 1
        else:
            raise IndexError("Heap array is full")
        if self.count > 1:
            self.trickleUp(self.count)

    def trickleUp(self, curIdx):
        parentIdx = (curIdx-1)/2
        if curIdx > 0:
            if self.heap[curIdx].getPriority() > self.heap[parentIdx].getPriority():
                temp = self.heap[parentIdx]
                self.heap[parentIdx] = self.heap[curIdx]
                self.heap[curIdx] = temp
                self.trickleUp(parentIdx)

    def trickleDown(self, curIdx):
        numItems = self.count

        lchildIdx = curIdx * 2 + 1

        rchildIdx = lchildIdx + 1

        if lchildIdx < numItems:
            largeIdx = lchildIdx
            if rchildIdx < numItems:
                if self.heap[lchildIdx].getPriority() < self.heap[rchildIdx].getPriority():
                    largeIdx = rchildIdx
            if self.heap[largeIdx].getPriority() > self.heap[curIdx].getPriority():
                self.swap(largeIdx, curIdx)
                self.trickleDown(largeIdx)

    def swap(self, largeIdx, curIdx):
        temp = self.heap[largeIdx]
        self.heap[largeIdx] = self.heap[curIdx]
        self.heap[curIdx] = temp

    def remove():
        pass

    def heapify(self):
        numItems = self.count

        for ii in range((numItems//2)-1, 0, -1):
            self.trickleDown(ii)

    def heapSort(self):
        numItems = self.count
        for ii in range((numItems -1), 1, -1):
            self.swap(0, ii)
            self.trickleDown(ii)

    def display(self):
        for i in range(0, self.count, 1):
            print(self.heap[i].getPriority())


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

if __name__ == "__main__":
    test = DSAHeaps(100)
    test.add(2,2)
    test.add(3,3)   
    test.add(9,9)
    test.add(8,8)
    test.add(5,5)
    test.add(6,6)
    test.add(0,0)
    test.display()
    test.heapify()
    print("Sorted")
    test.display()