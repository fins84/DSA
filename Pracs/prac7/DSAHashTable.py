from cmath import e
import numpy as NP
import math

class DSAHashTable():
    def __init__(self, tSize):
        self.HashArray = NP.empty(shape=tSize, dtype=object)
        self.count = 0
        self.tSize = tSize
        self.lower_lf = 0.4
        self.upper_lf = 0.7
        self.maxStep = 3
        self.populateEmpRay()

    def populateEmpRay(self):
        for i in range(0, self.tSize, 1):
            self.HashArray[i] = DSAHashNode(None, None, 0)
    
    def put(self, inKey, inValue):
        hashIdx = self.hash(inKey)
        origIdx = hashIdx

        found = False
        clone = False

        while found == False and clone == False:
            if self.HashArray[hashIdx].getState() == 0:
                found = True
                self.HashArray[hashIdx].setState(1)
                self.HashArray[hashIdx].setKey(inKey)
                self.HashArray[hashIdx].setValue(inValue)
                self.count += 1
                #hashIdx index is empty

            elif self.HashArray[hashIdx].getState() == 1:
                #hashIdx index
                if self.HashArray[hashIdx].getKey() == inKey:
                    clone = True
                    raise KeyError("Key already in hashtable")
                else:
                    hashIdx = ((hashIdx + self.stepHash(origIdx))%self.tSize)
                    if hashIdx == origIdx:
                        raise KeyError("No empty space for new key")

        if self.getLoadFactor() > self.upper_lf:
            self.resize(self.tSize * 2)

    def stepHash(self, index):
        maxS = self.tSize
        return (maxS - (index % maxS ))

    def get(self, inKey):
        hashKey = self.hash(inKey)
        origKey = hashKey
        found = False
        noKey = False

        if self.HashArray[hashKey].getState() == 1:
            while found == False and noKey == False:
                if self.HashArray[hashKey].getKey() == inKey:
                    found = True
                    return_val = self.HashArray[hashKey].getValue()
                hashKey = ((hashKey + self.stepHash(origKey)) % self.tSize)

                if hashKey == origKey:
                    noKey == True
                    raise Exception("Key not in hasharray")

        else:
            raise Exception("Key not in hasharray")

        return return_val

    def remove(self, inKey):
        hashKey = self.hash(inKey)
        origKey = hashKey
        found = False
        noKey = False

        if self.HashArray[hashKey].getState() == 1:
            while found == False and noKey == False:
                if self.HashArray[hashKey].getKey() == inKey:
                    found = True
                    self.HashArray[hashKey].setValue(None)
                    self.HashArray[hashKey].setKey(None)
                    self.HashArray[hashKey].setState(0)
                    self.count -= 1
                hashKey = ((hashKey + self.stepHash(origKey))%self.tSize)

                if hashKey == origKey:
                    noKey == True
                    raise Exception("Key not in hasharray")

        else:
            raise Exception("Key not in hasharray")

        if self.getLoadFactor() > self.lower_lf:
            self.resize(self.tSize / 2)

    def getLoadFactor(self):
        return (self.count/self.tSize)

    def export(self):
        exportList= NP.empty(shape=self.count, dtype=object)
        j = 0
        for i in range(0, self.tSize, 1):
            if self.HashArray[i].getState() == 1:
                exportList = self.HashArray[i].getKey() + "," + self.HashArray[i].getValue()
                j += 1
        return exportList

    def resize(self, size):
        size = self.nextPrime(size)
        oldSize = self.tSize
        oldRay = self.HashArray
        self.HashArray = NP.empty(shape=size, dtype=object)
        self.tSize = size
        self.populateEmpRay()

        for i in range(0, oldSize):
            if oldRay[i].getState() == 1:
                key = oldRay[i].getKey()
                value = oldRay[i].getValue()
                self.put(key, value)
                self.count -= 1

    def hash(self, inKey):
        a = 63689
        b = 378551
        hashIdx = 0
        inKey = str(inKey)
        
        for i in inKey:
            byteKey = ord(i)
            hashIdx = (hashIdx * a) + byteKey
            a *= b

        return hashIdx % len(self.HashArray)

    def nextPrime(self, inNum):
        primeVal = inNum

        if primeVal%2 == 0:
            primeVal += 1
        
        primeVal -= 2

        isPrime = False
        while not isPrime:
            primeVal += 2
            i = 3
            isPrime = True
            rootVal = math.sqrt(primeVal)

            while i <= rootVal and isPrime:
                if primeVal % i == 0:
                    isPrime = False
                else:
                    i+=2


        return primeVal


class DSAHashNode():
    def __init__(self, key, value, state):
        self. value = value
        self.key = key
        self.state = state

    def getValue(self):
        return self.value

    def getKey(self):
        return self.key

    def getState(self):
        return self.state

    def setValue(self, value):
        self.value = value

    def setKey(self, key):
        self.key = key

    def setState(self, state):
        self.state = state




def testCase(hashTable, j):
    for i in range(0, j):
        try:
            test.put(i, i)
        except Exception as e:
            print(i,e)

    print("Count ", test.count)
    print("Hash Table Size ", test.tSize)

"""    for i in range(0,j):
        try:
            assert test.get(i) == i, ("Error Tried to get Key", i, "but return val wrong")
        except Exception as e:
            print(e)"""

if __name__ == "__main__":
    test = DSAHashTable(10)
    testCase(test, 8)
    #testCase(test, 25)
    

    

