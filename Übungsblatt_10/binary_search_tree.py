#!/usr/bin/python3
# import argparse


class BinarySearchTree:
    """Binary search tree"""

    def __init__(self):
        """Constructor"""
        self._length = 0

    def insert(self, key, value):
        """Insert a key value pair to the tree

        >>> tree = BinarySearchTree()
        >>> tree.insert(8, "8")
        >>> tree.insert(3, "3")
        >>> tree.insert(4, "4")
        >>> tree.insert(4, "20")
        >>> tree.insert(9, "9")
        >>> print(tree.to_string())
        [(8, 8), left: [(3, 3), left: null, right: [(4, 20), \
left: null, right: null]], right: [(9, 9), left: null, right: null]]
        >>> print(tree.lookup(3))
        3
        >>> print(tree.lookup(4))
        20
        >>> print(tree.lookup(5))
        None

"""
        elem = TreeElement(key, value)
        if(self._length == 0):
            self._root = elem
        else:
            i = self._root
            while(i):
                if(elem == i):
                    i.setValue(elem.value())
                    # decrease length so that it stays same
                    self._length -= 1
                    break
                if(elem < i):
                    if(i.leftChild() is None):
                        i.setLeftChild(elem)
                        break
                    i = i.leftChild()
                else:
                    if(i.rightChild() is None):
                        i.setRightChild(elem)
                        break
                    i = i.rightChild()
        self._length += 1

    def lookup(self, key):
        """Look up the value with the specified key
        >>> tree = BinarySearchTree()
        >>> tree.insert(8, "8")
        >>> tree.insert(3, "3")
        >>> tree.insert(4, "4")
        >>> tree.insert(4, "20")
        >>> tree.insert(9, "9")
        >>> print(tree.lookup(3))
        3
        >>> print(tree.lookup(4))
        20
        >>> print(tree.lookup(5))
        None
        """
        elem = self._root
        while(elem):
            if(elem.key() == key):
                return elem.value()
            if(key < elem.key()):
                elem = elem.leftChild()
            if(key > elem.key()):
                elem = elem.rightChild()

        return None

    def to_string(self):
        out = ""
        node = self._root
        out = node.printChildren()
        return out


class TreeElement:
    def __init__(self, key, value):
        self._k = key
        self._v = value
        self._p = None
        self._lc = None
        self._rc = None

    def __lt__(self, other):
        return self.key() < other.key()

    def __eq__(self, other):
        return self.key() == other.key()

    def printChildren(self):
        out = "[("
        out += str(self.key()) + ", " + self.value() + "), left: "
        leftChild = self.leftChild()
        if(leftChild):
            out += leftChild.printChildren()
        else:
            out += "null"
        out += ", right: "
        rightChild = self.rightChild()
        if(rightChild):
            out += rightChild.printChildren()
        else:
            out += "null"
        out += "]"
        return out

    def key(self):
        return self._k

    def value(self):
        return self._v

    def setValue(self, value):
        self._v = value

    def setParent(self, parent):
        self._p = parent

    def setLeftChild(self, leftChild):
        self._lc = leftChild

    def setRightChild(self, rightChild):
        self._rc = rightChild

    def parent(self):
        return self._p

    def leftChild(self):
        return self._lc

    def rightChild(self):
        return self._rc


if __name__ == "__main__":
    print("empty")
