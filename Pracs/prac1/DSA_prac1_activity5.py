from re import A
from sys import stdin
from unicodedata import name
import numpy as np

#DSA prac 1 q5
#Name: Kevin Mesquita
#ID: 20175535
#This file sorts the RandomNames7000.csv file based on student number
#using 3 types of sorting algorithms and saves them to separate files

#sorting algorithms
def bubbleSort(A):
    passed = 0
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(0, len(A)-1-passed):
            if A[i].stID>A[i+1].stID:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                sorted = False
        passed = passed + 1

    return A

def insertionSort(A):
    for n in range(1,len(A)):
        i = n
        while i>0 and A[i-1].stID > A[i].stID:
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
    return A

def selectionSort(A):
    for n in range(len(A)):
        minIdx = n
        for j in range(n+1, len(A)):
            if A[j].stID < A[minIdx].stID:
                minIdx = j
        temp = A[minIdx]
        A[minIdx] = A[n]
        A[n] = temp
    return A

#printtofile
def toFile(A, filename):
    file = open(filename, "w")
    for line in range(0,len(A)):
        file.write("%d,%s\n" % (A[line].stID, A[line].name))
    file.close()


#Student Object
class Student:
    def __init__(self, stID, name):
        self.name = name
        self.stID = int(stID)




#main
filename = "RandomNames7000.csv"
n_data = 7000
student_Array = np.ndarray(n_data, dtype=object)


student_File = open(filename, "r")

for index in range(0, n_data):
    line = student_File.readline().split(",")
    student_Array[index] = Student(line[0],line[1])
student_File.close()
bubble_Ray = student_Array.copy()
selection_Ray = student_Array.copy()
insert_Ray = student_Array.copy()

bubbleSort(bubble_Ray)
selectionSort(selection_Ray)
insertionSort(insert_Ray)
toFile(bubble_Ray,"bubble_sorted.csv")
toFile(selection_Ray, "selection_sorted.csv")
toFile(insert_Ray, "insert_sort.csv")