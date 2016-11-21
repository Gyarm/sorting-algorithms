#!/usr/bin/python3


def inssort(inList):
    """ Sort list using the insertion algorithm.

    >>> inssort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> inssort([])
    []

    >>> inssort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: inList must be a list

    """
    # Check given parameter data type.
    if not type(inList) == list:
        raise TypeError('inList must be a list')

    outList = []
    j = 0
    n = len(inList)
    for i in range(n):
        # Take elemt at index i.
        elemToBeInserted = inList[i]

        for j in range(len(outList)):
            # check if element fits here
            if elemToBeInserted < outList[j]:
                # if yes break; j will be used to identify the index in outList
                break
        else:
            j += 1

        outList = outList[:j] + [elemToBeInserted] + outList[j:]

    return outList

if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # Sort the list.
    print(inssort(numbers))
