__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mystack import Stack


class StackMin(Stack):
    """Stack implementation using a linked list structure"""

    class StackMinNode:
        """An object that represents each item in a stack"""

        def __init__(self, value):
            self.value = value
            self.next = None
            self.min = None

    def push(self, value):
        """Adds a new element to the beginning of the stack"""

        new_node = self.StackMinNode(value)
        new_node.next = self.top
        if self.top is None:
            new_node.min = new_node.value
        else:
            new_node.min = min(self.top.min, new_node.value)
        self.top = new_node
        self._len += 1

    def min(self):
        """Returns the element with the smallest value in the stack"""

        if self.top is None:
            raise IndexError("min from empty stack")
        else:
            return self.top.min


class TestStackMin(unittest.TestCase):
    def test_min(self):
        stack = StackMin()

        with self.assertRaises(IndexError):
            stack.min()

        stack.push(4)
        self.assertEqual(stack.min(), 4)

        stack.push(5)
        self.assertEqual(stack.min(), 4)

        stack.push(2)
        self.assertEqual(stack.min(), 2)

        stack.push(0)
        self.assertEqual(stack.min(), 0)

        stack.pop()
        self.assertEqual(stack.min(), 2)

        stack.pop()
        self.assertEqual(stack.min(), 4)


if __name__ == '__main__':
    unittest.main()
