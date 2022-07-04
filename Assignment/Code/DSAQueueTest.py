import DSAQueue as Queue

#
# DSAQueue test code taken and adapted from prac 3
#

class DSAQueueTest():
    def __init__(self,typeQ):
        if typeQ == "roll":
            self.rollingQueue = Queue.DSARollingQueue(100)
        else:
            raise ValueError("Didn't parse a valid test type")

    def testEmpty(self):
        assert (self.rollingQueue.getCount() == 0), "Count should be 0 as no elements inside"
        assert (self.rollingQueue.isEmpty() == True), "isEmpty should be true as 0 elements"
        assert (self.rollingQueue.isFull() == False), "isFull should be false as 0 elements"
    
    def testMiddle(self):
        for i in range(1,11):
           self.rollingQueue.enqueue(i)
        assert (self.rollingQueue.getCount() == 10), "Count should be 11"
        assert (self.rollingQueue.isEmpty() == False), "isEmpty should be false as there are few elements"
        assert (self.rollingQueue.isFull() == False), "isFull should be false as max capacity not reached"
        for i in range(1,11):
           assert (self.rollingQueue.dequeue() == i), "Should be ascending values from 1 to 10 when removing values"

    def testFull(self):
        for i in range(1,101):
           self.rollingQueue.enqueue(i)
        assert (self.rollingQueue.getCount() == 100), "Count should be 100"
        assert (self.rollingQueue.isEmpty() == False), "isEmpty should be True as queue is full"
        assert (self.rollingQueue.isFull() == True), "isFull should be True as queue is full"
        for i in range(1,101):
           assert (self.rollingQueue.dequeue() == i), "Should be ascending values from 1 to 100 when removing values"

    def ExceedBounds(self):
        for i in range(1,105):
           self.rollingQueue.enqueue(i)
        assert (self.rollingQueue.getCount() == 100), "Count should be 100"
        assert (self.rollingQueue.isEmpty() == False), "isEmpty should be True as queue is full"
        assert (self.rollingQueue.isFull() == True), "isFull should be True as queue is full"
        for i in range(1,100):
           assert (self.rollingQueue.dequeue() == i), "Should be ascending values from 1 to 100 when removing values"
        for i in range(1,4):
           self.rollingQueue.dequeue()
        
        self.testEmpty()

### Shuffling Queue Test ###
def queueTest():
    print("Queue Test ***...")
    try:
        test = DSAQueueTest("roll")
    except ValueError as e:
        print(e)
    try:
        test.testEmpty()
    except AssertionError as e:
        print(e,"One of the tests came failed")
    except ValueError as e:
        print(e, "Output type from test was wrong")
    except IndexError as e:
        print(e, "Test pushed the queue out of array size bounds")
    try:
        test.testMiddle()
    except AssertionError as e:
        print(e,"One of the tests came failed")
    except ValueError as e:
        print(e, "Output type from test was wrong")
    except IndexError as e:
        print(e, "Test pushed the queue out of array size bounds")
    try:
        test.testFull()
    except AssertionError as e:
        print(e,"One of the tests came failed")
    except ValueError as e:
        print(e, "Output type from test was wrong")
    except IndexError as e:
        print(e, "Test pushed the queue out of array size bounds")
    try:
        test.ExceedBounds()
    except AssertionError as e:
        print(e,"One of the tests came failed")
    except ValueError as e:
        print(e, "Output type from test was wrong")
    except IndexError as e:
        print(e, "Test pushed the queue out of array size bounds")
    
    print("If no exception print... passed test\n")