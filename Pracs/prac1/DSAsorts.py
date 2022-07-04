#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Name: Kevin Mesquita
# ID: 20175535
import nntplib
from telnetlib import DO

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
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


