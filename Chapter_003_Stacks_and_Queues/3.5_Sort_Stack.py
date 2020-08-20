__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mystack import Stack


class SortStack(Stack):
    """Extends the Stack class

    Simply has a new method called sort"""

    def sort(self):
        if self.isEmpty():
            return
        temp_stack = Stack()
        while not self.isEmpty():
            value = self.pop()
            while not temp_stack.isEmpty() and temp_stack.peek() > value:
                self.push(temp_stack.pop())
            temp_stack.push(value)
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())


class TestSortStack(unittest.TestCase):
    def test_sort(self):
        my_stack = SortStack()
        self.assertEqual(str(my_stack), "")
        my_stack.sort()
        self.assertEqual(str(my_stack), "")

        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        self.assertEqual(str(my_stack), "4 -> 3 -> 2 -> 1")

        my_stack.sort()
        self.assertEqual(my_stack.peek(), 1)
        self.assertEqual(str(my_stack), "1 -> 2 -> 3 -> 4")

        my_stack.push(5)
        self.assertEqual(str(my_stack), "5 -> 1 -> 2 -> 3 -> 4")

        my_stack.sort()
        self.assertEqual(my_stack.peek(), 1)
        self.assertEqual(str(my_stack), "1 -> 2 -> 3 -> 4 -> 5")


if __name__ == '__main__':
    unittest.main()
