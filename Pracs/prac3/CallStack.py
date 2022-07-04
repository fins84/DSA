import DSAStack as Stack

class CallStack():
    stack = Stack.DSAStack()

    def factorial(self, n):
        self.stack.push(self.factorial.__name__ + "(" + str(n) + ")")
        print("\n\nDISPLAYING STACK")
        self.stack.display()
        if n == 0:
            nFact = 1
        else:
            nFact = n*self.factorial(n-1)
        print("Popped: ", self.stack.pop())
        return nFact

    def factorial_Iter(self, n):
        nFact = 1
        for i in range(n,1,-1):
            self.stack.push(self.factorial.__name__ + "(" + str(n) + ")")
            nFact = nFact * i
            print("\n\nDISPLAYING STACK")
            self.stack.display()
        return nFact

#main
callstack = CallStack()
print("\n######### Recursive Factorial #########")
print(callstack.factorial(5))
print("\n######### Factorial Iteration #########")
print(callstack.factorial_Iter(5))

