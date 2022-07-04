#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Name: Kevin Mesquita
# ID: 20175535
import numpy 
import random

def bubbleSort(A):
    passed = 0
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(0, len(A)-1-passed):
            if A[i]>A[i+1]:
                temp = A[i].copy()
                A[i] = A[i+1]
                A[i+1] = temp
                sorted = False
        passed = passed + 1

    return A

def insertionSort(A):
    for n in range(1,len(A)):
        i = n
        while i>0 and A[i-1] > A[i]:
            temp = A[i].copy()
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
    return A

def selectionSort(A):
    for n in range(len(A)):
        minIdx = n
        for j in range(n+1, len(A)):
            if A[j] < A[minIdx]:
                minIdx = j
        temp = A[minIdx].copy()
        A[minIdx] = A[n]
        A[n] = temp
    return A

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    mergeSortRecurse(A, 0, A.size - 1)

def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx)//2
        A = mergeSortRecurse(A, leftIdx, midIdx)
        A = mergeSortRecurse(A, midIdx + 1, rightIdx)
        A = merge(A, leftIdx, midIdx, rightIdx)
    return A

def merge(A, leftIdx, midIdx, rightIdx):
    tempArr = numpy.empty(rightIdx - leftIdx + 1, dtype=object)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0

    while (ii <= midIdx) and (jj <= rightIdx):
        if A[ii] <= A[jj]:
            tempArr[kk] = A[ii]
            ii+=1
        else:
            tempArr[kk] = A[jj]
            jj += 1
        
        kk += 1

    for i in range(ii, midIdx+1, 1):
        tempArr[kk] = A[i]
        kk += 1
    for j in range(jj, rightIdx+1, 1):
        tempArr[kk] = A[j]
        kk += 1

    for k in range(leftIdx, rightIdx + 1, 1):
        A[k] = tempArr[k-leftIdx]

    return A

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurse(A, 0, A.size -1)

def quickSortRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = (leftIdx + rightIdx)//2
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurse(A, leftIdx, newPivotIdx-1)
        quickSortRecurse(A, newPivotIdx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivIdx):
    pivotVal = A[pivIdx]
    A[pivIdx] = A[rightIdx]
    A[rightIdx] = pivotVal

    currIdx = leftIdx

    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp
            currIdx += 1
    
    newPivIdx = currIdx
    A[rightIdx] = A[newPivIdx]
    A[newPivIdx] = pivotVal

    return newPivIdx

def quickSortMed3(A):
    quickSortRecurseMed3(A, 0, A.size-1)

def quickSortRecurseMed3(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        midIdx = (leftIdx + rightIdx)//2
        pivotIdx = med3(A, leftIdx, midIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurseMed3(A, leftIdx, newPivotIdx-1)
        quickSortRecurseMed3(A, newPivotIdx + 1, rightIdx)

def med3(A, leftIdx, midIdx, rightIdx):
    if A[leftIdx] >= A[midIdx] and A[leftIdx] <= A[rightIdx] or A[leftIdx] >= A[rightIdx] and A[leftIdx] <= A[midIdx]:
        median = leftIdx
    elif A[midIdx] >= A[leftIdx] and A[midIdx] <= A[rightIdx] or A[midIdx] >= A[rightIdx] and A[midIdx] <= A[leftIdx]:
        median = midIdx
    elif A[rightIdx] >= A[leftIdx] and A[rightIdx] <= A[midIdx] or A[rightIdx] >= A[midIdx] and A[rightIdx] <= A[leftIdx]:
        median = rightIdx

    return median

def quickSortRandom(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurseRand(A, 0, A.size -1)

def quickSortRecurseRand(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        midIdx = (leftIdx + rightIdx)//2
        pivotIdx = random.choice([leftIdx, midIdx, rightIdx])
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurseRand(A, leftIdx, newPivotIdx-1)
        quickSortRecurseRand(A, newPivotIdx + 1, rightIdx)

def quickSortLeft(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurseLeft(A, 0, A.size -1)

def quickSortRecurseLeft(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = (leftIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurseLeft(A, leftIdx, newPivotIdx-1)
        quickSortRecurseLeft(A, newPivotIdx + 1, rightIdx)

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

    sorted = numpy.zeros(len(A),dtype=object)
    count = numpy.zeros(maxV-minV+2, dtype=int)

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

    A = sorted
    return A

# https://www.programiz.com/dsa/radix-sort
def CountingSort_Rad(A, dec):
    index = 1

    sorted = numpy.zeros(len(A),dtype=object)
    count = numpy.zeros(10, dtype=int)

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
