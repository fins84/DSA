import DSAStack as Stack

class DSAStackTest():
    def __init__(self) -> None:
        self.stack = Stack.DSAStack()

    def testEmpty(self):
        assert (self.stack.getCount() == 0), "Count should 0 as its empty"
        assert (self.stack.isEmpty() == True), "isEmpty Should be true as empty"
        assert (self.stack.isFull() == False), "isFull should False as its empty"
    
    def testMiddle(self):
        for i in range(1,11):
           self.stack.push(i)
        assert (self.stack.getCount() == 10), "Count should 10"
        assert (self.stack.isEmpty() == False), "isEmpty Should be false as few values inside"
        assert (self.stack.isFull() == False), "isFull should False as full values inside"
        for i in range(10,0,-1):
           assert (self.stack.pop() == i), "Should be descending values from 10 to 11 when removing values"


    def testFull(self):
        for i in range(1,101):
           self.stack.push(i)
        assert (self.stack.getCount() == 100), "Count should 100 as full"
        assert (self.stack.isEmpty() == False), "isEmpty Should be false as its full"
        assert (self.stack.isFull() == True), "isFull shoudl be true as its full"
        for i in range(100,0,-1):
           assert (self.stack.pop() == i), "Should be descending values from 100 to 1 when removing values"


    def ExceedBounds(self):
        for i in range(1,105):
           self.stack.push(i)
        assert (self.stack.getCount() == 100), "Count should 100 as full"
        assert (self.stack.isEmpty() == False), "isEmpty Should be false as its full"
        assert (self.stack.isFull() == True), "isFull shoudl be true as its full"
        for i in range(100,0,-1):
           assert (self.stack.pop() == i), "Should be descending values from 100 to 1 when removing values"
        for i in range(5,0,-1):
           self.stack.pop()
        self.testEmpty()


test = DSAStackTest()
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

