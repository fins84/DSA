import timeit

#factorial

def factorial_Iter(n):
    nFactorial = 1
    for i in range(n,1,-1):
        nFactorial = nFactorial * i
    return nFactorial

def factRecurs(n):
    factorial = 1
    if(n==0):
        factorial = 1
    else:
        factorial = n*factRecurs(n-1)

    return factorial

def fact_WrpRecurs(n):
    if type(n) ==  str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif n<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return factRecurs(n)

def factorial_WrpIter(n):
    if type(n) ==  str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif n<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return factorial_Iter(n)

#fibonacci sequence

def fibIterative(n):
    fibVal = 0
    currVal = 1
    lastVal = 0
    
    if n==0:
        fibVal = 0
    elif n==1:
        fibVal = 1
    else:
        for i in range(2,n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibRecurs(n):
    fibVal = 0
    if n==0:
        fibVal = 0

    elif n==1:
        fibVal = 1
    else:
        fibVal = fibRecurs(n-1)+fibRecurs(n-2)
    return fibVal


def fib_WrpRecurs(n):
    if type(n) ==  str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif n<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return fibRecurs(n)

def fib_WrpIter(n):
    if type(n) ==  str:
        raise TypeError("Arguments cannot be character (integers only)")

    elif n<0:
        raise ValueError("Argument values (number/base) cannot be negative")

    return fibIterative(n)


#main
n = -5

return_val = 0

print("\nFactorial Time Elapse: \n")
start = timeit.default_timer()
try:
    return_val = factorial_WrpIter(n)
except Exception as e:
    print("Error: ", e)

end = timeit.default_timer()
time = end-start
print("Factorial Iteration of value ", n, " is ", return_val, " taking " , time, " seconds.\n")
start = timeit.default_timer()
try:
    return_val = fact_WrpRecurs(n)
except Exception as e:
    print("Error: ", e)
end = timeit.default_timer()
time = end-start
print("Factorial Recursion of value ", n, " is ", return_val, " taking " , time, " seconds.\n")

print("\nFibonacci Time Elapse: \n")
start = timeit.default_timer()
try:    
    return_val = fib_WrpIter(n)
except Exception as e:
    print("Error: ", e)
end = timeit.default_timer()
time = end-start
print("Fibonacci Iteration of value ", n, " is ", return_val, " taking " , time, " seconds.\n")
start = timeit.default_timer()
try:
    return_val = fib_WrpRecurs(n)
except Exception as e:
    print("Error: ", e)
end = timeit.default_timer()
time = end-start
print("Fibonacci Recursion of value ", n, " is ", return_val, " taking " , time, " seconds.\n")


"""
/mnt/c/Users/diamo/OneDrive/Desktop/My Stuff/Uni/DSA/Pracs/prac2

factorial Iteration
n = 10: 9.599999998499698e-06
n = 25: 6.8999999882635166e-06
n = 50: 1.0400000007848575e-05
n = 75: 9.999999974752427e-06

factorial Recursive
n = 10: 1.0400000007848575e-05
n = 25: 7.199999998874773e-06
n = 50: 2.2800000010647636e-05
n = 75: 9.899999980689245e-06

fibonacci Iteration
n = 10: 7.100000004811591e-06
n = 25: 5.100000009861105e-06
n = 50: 5.899999990788274e-06
n = 75: 6.2000000013995304e-06

fibonacci Recursive
n = 10: 0.030965099999988865
n = 25: 0.028777999999988424
n = 50: 0.03020519999998328
n = 75: 0.030622900000025766

"""