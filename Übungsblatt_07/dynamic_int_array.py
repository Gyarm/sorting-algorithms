#!/usr/bin/python3

# import argparse
import numpy as np
import argparse
import timeit


class DynamicIntArray:
    """Dynamic integer array class implemented with fixed-size numpy array."""

    def __init__(self):
        """Create empty array with length 0 and capacity 1."""
        self._n = 0  # Number of elements in array
        self._c = 1  # Capacity
        self._a = self._create_array(self._c)

    def __len__(self):
        """Return number of elements in the array."""
        return self._n

    def __getitem__(self, i):
        """Return element at index i."""
        # Check for index out of bounds error.
        if not 0 <= i < self._n:
            raise IndexError('index out of bounds')
        return self._a[i]

    def append(self, value):
        """Add integer value to end of array."""
        # Check if given value is of integer type.
        if not isinstance(value, int):
            raise TypeError('value is not integer')
        if self._n == self._c:  # time to resize
            self._resize(2 * self._c)
        self._a[self._n] = value
        self._n += 1

    def remove(self):
        """Remove last item from list"""
        if self._n > 0:
            self._n -= 1
            if self._n < self._c/3:
                self._resize(int(self._c/2))
        else:
            raise IndexError('index out of bounds')

    def _resize(self, new_c):
        """Resize array to capacity new_c."""
        b = self._create_array(new_c)
        for i in range(self._n):
            b[i] = self._a[i]
        # Assign old array reference to new array.
        self._a = b
        self._c = new_c

    def _create_array(self, new_c):
        """Return new array with capacity new_c."""
        return np.empty(new_c, dtype=int)  # data type = integer


def test_1():
    a1 = DynamicIntArray()
    startTime = timeit.default_timer()
    for i in range(int(10e6)):
        a1.append(12345)
        print(i, "\t", timeit.default_timer() - startTime)


def test_2():
    a1 = DynamicIntArray()
    for i in range(int(10e6)):
        a1.append(12345)
    startTime = timeit.default_timer()
    for i in range(int(10e6)):
        a1.remove()
        print(i, "\t", timeit.default_timer() - startTime)


def test_3():
    a1 = DynamicIntArray()
    for i in range(int(1e6)):
        a1.append(12345)

    runs = int(10e6)
    i = 0
    startTime = timeit.default_timer()
    while i < runs:
        tempCap = a1._c
        while a1._c == tempCap and i < runs:
            a1.append(12345)
            print(i, "\t", timeit.default_timer() - startTime)
            i += 1
        tempCap = a1._c
        while a1._c == tempCap and i < runs:
            a1.remove()
            print(i, "\t", timeit.default_timer() - startTime)
            i += 1


def test_4():
    a1 = DynamicIntArray()
    for i in range(int(1e6)):
        a1.append(12345)

    runs = int(10e6)
    i = 0
    startTime = timeit.default_timer()
    while i < runs:
        tempCap = a1._c
        while a1._c == tempCap and i < runs:
            a1.remove()
            print(i, "\t", timeit.default_timer() - startTime)
            i += 1
        tempCap = a1._c
        while a1._c == tempCap and i < runs:
            a1.append(12345)
            print(i, "\t", timeit.default_timer() - startTime)
            i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-t", "--test", type=int, required=True,
        help="Output runtime of specified test:\n" +
        "TEST = 1: A sequence of 10 million append operations starting" +
        "with an empty array.\n" +
        "TEST = 2: A sequence of 10 million remove operations starting" +
        " with an array containing 10 million elements.\n" +
        "TEST = 3: A sequence of 10 million operations starting with " +
        "an array containing 1 million elements.\n" +
        "The operations should start with append and then alternate " +
        "after each reallocation between append and remove.\n" +
        "TEST = 4: Same as Test 3, but this time starting with remove.")
    args = parser.parse_args()
    if args.test == 1:
        test_1()
    elif args.test == 2:
        test_2()
    elif args.test == 3:
        test_3()
    elif args.test == 4:
        test_4()
    else:
        print("Please enter valid TEST number")
