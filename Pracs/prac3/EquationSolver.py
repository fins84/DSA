import DSAStack as Stack
import DSAQueue as Queue

class EquationSolver():
    def __init__(self) -> None:
        self.PostFix = Queue.DSARollingQueue()

    def solve(self,equation):
        self.parseInfixToPostfix(equation)
        answer = self.evaluatePostfix()
        return answer

    def parseInfixToPostfix(self,equation):
        operatorStack = Stack.DSAStack()
        infixArray = equation.split()

        for char in infixArray:
            if char == "+" or char == "-" or char == "*" or char == "/":
                while operatorStack.isEmpty() ==  False and operatorStack.top() != "(" and self.precedenceOf(operatorStack.top()) >= self.precedenceOf(char):
                    self.PostFix.enqueue(operatorStack.pop())
                operatorStack.push(char)
            elif char == ")":
                while operatorStack.top() != "(":
                    self.PostFix.enqueue(operatorStack.pop())
                operatorStack.pop()
            elif char == "(":
                operatorStack.push(char)

            elif isinstance(char, str) == True:
                self.PostFix.enqueue(char)
            else:
                raise ValueError("Error in values for input equation")

            print("char: ",char)
            for values in operatorStack.queue:
                if values != None:
                    print(values, end="")
            print("")
            for values in self.PostFix.queue:
                if values != None:
                    print(values, end=" ")
            print("")

        while not operatorStack.isEmpty():
            self.PostFix.enqueue(operatorStack.pop())
                    

    def evaluatePostfix(self):
        postFixQueue = Stack.DSAStack()
        for i in range(0, self.PostFix.getCount()):
            char = self.PostFix.dequeue()
            if char == "+" or char == "-" or char == "*" or char == "/":
                a = postFixQueue.pop()
                b = postFixQueue.pop()
                postFixQueue.push(self.executeOperation(char, float(a),float(b)))
            else:
                postFixQueue.push(char)
        
        return postFixQueue.pop()
                    

    def precedenceOf(self,theOp):
        if theOp == "+":
            return_val = 1
        elif theOp == "-":
            return_val = 1
        elif theOp == "*":
            return_val = 2
        elif theOp == "/":
            return_val = 2

        return return_val


    def executeOperation(self,op, op2, op1):

        if op == "+":
            return_val = op1 + op2
        elif op == "-":
            return_val = op1 - op2
        elif op == "*":
            return_val = op1 * op2
        elif op == "/":
            return_val = op1 / op2


        return return_val

    def test(self):
        for i in range(0, self.PostFix.getCount()):
            print(self.PostFix.dequeue())

#main

equation = "( 100 + 2 ) * 3 + ( 4 + 5 ) * 7"
eqSolver = EquationSolver()
print(eqSolver.solve(equation))