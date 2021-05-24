import sys
from time import time
import numpy as np
from timeit import timeit
import random


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def calcula_menor_tempo(array):
    ini = time()
    bubbleSort(array)
    fim = time()
    bubble_time = fim - ini

    ini = time()
    quickSort(array)
    fim = time()
    quick_time = fim - ini

    ini = time()
    mergeSort(array)
    fim = time()
    merge_time = fim - ini

    return bubble_time, quick_time, merge_time

sys.setrecursionlimit(10**8)

array_menor = np.random.randint(0, 1000, (10 ** 5))
array_medio = np.random.randint(0, 1000, (10 ** 7))
# array_maior = np.random.randint(0, 1000, (1, 10 ** 9))


bubble_menor, quick_menor, merge_menor = calcula_menor_tempo(array_menor)
bubble_medio, quick_medio, merge_medio = calcula_menor_tempo(array_medio)
# bubble_maior, quick_maior, merge_maior = calcula_menor_tempo(array_maior)

print(bubble_menor, quick_menor, merge_menor)
print(bubble_medio, quick_medio, merge_medio)
# print(bubble_maior, quick_maior, merge_maior)




# Quick sort
# Provavelmente é o mais utilizado. Possui complexidade C(n) = O(n²) no pior caso e C(n) = O(n log n) no melhor e médio caso e não é um algoritmo estável.

# Merge sort
# É um método estável e possui complexidade C(n) = O(n log n) para todos os casos.

# Bubble sort
# O(n**2)
