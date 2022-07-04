
import numpy as np

# https://www.programiz.com/dsa/shell-sort 
def shellSort(A):
    interv = len(A) // 2

    while interv >= 1:
        for i in range(interv, len(A)):
            j = i
            t = A[i]
        
            while A[j - interv] > t and j >= interv:
                A[j] = A[j - interv]
                j -= interv

            A[j] = t
        interv = interv//2

    return A

# https://www.codingeek.com/algorithms/counting-sort-explanation-pseudocode-and-implementation/
def CountingSort(A):
    minV = min(A)
    maxV = max(A)
    index = 1
    nV = 0

    sorted = np.zeros(len(A),dtype=object)
    count = np.zeros(maxV-minV+2, dtype=int)

    for i in range(minV, maxV+1, 1):
        for values in A:
            if values == i:
                nV += 1
        count[index] = nV
        index += 1

    index = len(A)-1
    for j in range(len(count)-1, 0, -1):
        diff = count[j] - count[j - 1]
        for i in range(0, diff, 1):
            sorted[index] = maxV
            index -=1
        maxV -= 1

    return(sorted)

# https://www.programiz.com/dsa/radix-sort
def CountingSort_Rad(A, dec):
    index = 1

    sorted = np.zeros(len(A),dtype=object)
    count = np.zeros(10, dtype=int)

    for values in A:
        index = (values // dec) % 10
        count[index] += 1

    for i in range(0, len(count)):
        count[i] += count[i-1]

    i = len(A)-1
    while i >= 0:
        index = (A[i]//dec)%10
        sorted[count[index]-1] = A[i]
        count[index] -= 1
        i -= 1
    
    return sorted

# https://www.programiz.com/dsa/radix-sort 
def RadixSort(A):
    k = max(A)
    ndigit = len(str(k))
    dec = 1

    for i in range(0, ndigit):
        A = CountingSort_Rad(A, dec)
        dec *= 10

    return A