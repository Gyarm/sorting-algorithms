#!/usr/bin/env python3


def heapsort(inList):
    """ Sort list using the heapsort algorithm.

    >>> heapsort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> heapsort([100])
    [100]

    >>> heapsort([3,2,2,3])
    [2, 2, 3, 3]

    >>> heapsort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: inList must be a list

    """
    # Check given parameter data type.
    if not type(inList) == list:
        raise TypeError('inList must be a list')

    build_heap(inList)

    # repeat: replace root of heap by last knode and repair heap
    lengthOfHeap = len(inList)
    while lengthOfHeap > 0:
        inList[0], inList[lengthOfHeap-1] = inList[lengthOfHeap-1], inList[0]
        lengthOfHeap = lengthOfHeap - 1
        heapify(inList, 0, lengthOfHeap)
    return inList


def build_heap(inList):
    # ---build the heap---
    # we have to start at the first knode that has children
    # which is at index n/2-1
    index = (int)(len(inList)/2-1)
    while(index >= 0):
        heapify(inList, index, len(inList))
        index = index-1


def heapify(inList, i, lengthOfHeap):
    indexOfMaximum = i
    maximum = inList[i]
    indexOfLeft = i*2+1
    indexOfRight = i*2+2
    # check if index out of bounds
    if indexOfLeft < lengthOfHeap:
        if inList[indexOfLeft] > maximum:
            indexOfMaximum = indexOfLeft
            maximum = inList[indexOfMaximum]
    if indexOfRight < lengthOfHeap:
        if inList[indexOfRight] > maximum:
            indexOfMaximum = indexOfRight
    # swap
    if indexOfMaximum != i:
        inList[i], inList[indexOfMaximum] = inList[indexOfMaximum], inList[i]
        heapify(inList, indexOfMaximum, lengthOfHeap)


if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # Sort the list.
    print(heapsort(numbers))
