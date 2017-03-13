#!/usr/bin/python3


class PriorityQueueItem:
    """ Provides a handle for a queue item.
    A simple class implementing a key-value pair,
    where the key is an integer, and the value can
    be an arbitrary object. Index is the heap array
    index of the item.
    """
    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __lt__(self, other):
        """ Enables us to compare two items with a < b.
        The __lt__ method defines the behavior of the
        < (less than) operator when applied to two
        objects of this class. When using the code a < b,
        a.__lt__(b) gets evaluated.
        There are many other such special methods in Python.
        See "python operator overloading" for more details.
        """
        return self._key < other._key

    def get_heap_index(self):
        """ Return heap index of item."""
        return self._index

    def set_heap_index(self, index):
        """ Update heap index of item."""
        self._index = index


class PriorityQueueMinHeap:
    """Priority queue implemented as min heap."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._list = []

    def _parent(self, item):
        return self._list[int((item.get_heap_index()-1)/2)]

    def _left_child(self, item):
        try:
            return self._list[item.get_heap_index()*2+1]
        except:
            return None

    def _right_child(self, item):
        try:
            return self._list[item.get_heap_index()*2+2]
        except:
            return None

    def _repair_heap_up(self, item):
        if self._parent(item) > item:
            self._swap_items(item, self._parent(item))
            self._repair_heap_up(item)

    def _repair_heap_down(self, item):
        leftChild = self._left_child(item)
        minimum = item
        try:
            if leftChild < minimum:
                minimum = leftChild
        except:
            # if left child is None, there is
            # no right child either -> method ends
            return
        try:
            rightChild = self._right_child(item)
            if rightChild < minimum:
                minimum = rightChild
        except:
            pass
            # there is no right child
            # -> simply go on

        if item != minimum:
            self._swap_items(minimum, item)
            self._repair_heap_down(item)

    def _swap_items(self, i, j):
        # Swap items with indices i,j (also swap their indices!)
        oldIndexOfI = i.get_heap_index()
        oldIndexOfJ = j.get_heap_index()

        j.set_heap_index(oldIndexOfI)
        self._list[oldIndexOfI] = j
        i.set_heap_index(oldIndexOfJ)
        self._list[oldIndexOfJ] = i

    def insert(self, key, value):
        """ Inserts the specified key value pair in the heap.

        >>> h = PriorityQueueMinHeap()
        >>> _ = h.insert(6, "G")
        >>> _ = h.insert(2, "A")
        >>> _ = h.insert(7, "O")
        >>> _ = h.insert(3, "L")
        >>> _ = h.insert(1, '.')
        >>> print(h.insert(0, 1).get_heap_index())
        0
        """
        # insert new PriorityQueueItem at end of heap
        item = PriorityQueueItem(key, value, self.size())
        self._list.append(item)
        # repair heap
        self._repair_heap_up(item)
        return item

    def get_min(self):
        """ Returns the smalles element in heap.

        >>> h = PriorityQueueMinHeap()
        >>> _ = h.insert(6, "G")
        >>> _ = h.insert(2, "A")
        >>> _ = h.insert(7, "O")
        >>> _ = h.insert(3, "L")
        >>> _ = h.insert(1, '.')
        >>> _ = h.insert(0, 1)
        >>> h.get_min()
        (0, 1)
        """
        retElem = self._list[0]
        return (retElem._key, retElem._value)

    def delete_min(self):
        """ Deletes root element of the heap and
        returns it.

        >>> h = PriorityQueueMinHeap()
        >>> _ = h.insert(6, "G")
        >>> _ = h.insert(2, "A")
        >>> _ = h.insert(7, "O")
        >>> _ = h.insert(3, "L")
        >>> _ = h.insert(1, '.')
        >>> _ = h.insert(0, 1)
        >>> h.delete_min()
        (0, 1)
        >>> h.delete_min()
        (1, '.')
        >>> h.delete_min()
        (2, 'A')
        >>> h.delete_min()
        (3, 'L')
        >>> h.delete_min()
        (6, 'G')
        >>> h.delete_min()
        (7, 'O')
        >>> h.delete_min()
        """
        if self.size() > 0:
            self._swap_items(self._list[self.size()-1],
                             self._list[0])
            # get former root item - will be returned
            retElem = self._list.pop()
            if self.size() > 0:
                self._repair_heap_down(self._list[0])
            return (retElem._key, retElem._value)
        else:
            return None

    def change_key(self, item, new_key):
        """ Assigns a new key to the specified item.

        >>> h = PriorityQueueMinHeap()
        >>> _ = h.insert(6, "G")
        >>> _ = h.insert(2, "A")
        >>> _ = h.insert(7, "O")
        >>> _ = h.insert(3, "L")
        >>> _ = h.insert(1, '.')
        >>> _ = h.insert(0, 1)
        >>> h.change_key(_, 4)
        >>> h.delete_min()
        (1, '.')
        >>> h.delete_min()
        (2, 'A')
        >>> h.delete_min()
        (3, 'L')
        >>> h.delete_min()
        (4, 1)
        >>> h.delete_min()
        (6, 'G')
        >>> h.delete_min()
        (7, 'O')
        >>> h.delete_min()
        """

        item._key = new_key
        # repair heap
        # we don't know if the newly assigned key is
        # bigger or smaller -> check that:
        if self._parent(item) > item:
            self._repair_heap_up(item)
        else:
            self._repair_heap_down(item)

    def size(self):
        return len(self._list)


if __name__ == "__main__":
    # Create priority queue object.
    pq1 = PriorityQueueMinHeap()
    # Insert some flights into queue.
    pq1_item1 = pq1.insert(1, "Airforce One")
    pq1_item2 = pq1.insert(45, "Bermuda Triangle Blues (Flight 45)")
    pq1_item3 = pq1.insert(666, "Flight 666")
