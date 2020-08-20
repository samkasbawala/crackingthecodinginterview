__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mystack import Stack


class MyQueue():
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()
        self._len = 0

    def enqueue(self, value):
        """Adds an item to the queue"""

        while not self.dequeue_stack.isEmpty():
            self.enqueue_stack.push(self.dequeue_stack.pop())
        self._len += 1
        self.enqueue_stack.push(value)

    def dequeue(self):
        """Removes and returns the item at the beginning of the queue"""

        if len(self) == 0:
            raise IndexError("dequeue from empty queue")

        while not self.enqueue_stack.isEmpty():
            self.dequeue_stack.push(self.enqueue_stack.pop())
        self._len -= 1
        return self.dequeue_stack.pop()

    def peek(self):
        """Returns the item at the beginning of the queue"""

        if len(self) == 0:
            raise IndexError("peek from empty queue")

        while not self.enqueue_stack.isEmpty():
            self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.peek()

    def isEmpty(self):
        """Returns a boolean checking on whether or not the queue is empty"""

        return len(self) == 0

    def __str__(self):
        """Returns a string that shows the queue"""

        while not self.enqueue_stack.isEmpty():
            self.dequeue_stack.push(self.enqueue_stack.pop())
        return str(self.dequeue_stack)

    def __len__(self):
        return self._len


class TestMyQueue(unittest.TestCase):
    def test_enqueue(self):
        my_queue = MyQueue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(str(my_queue), '1 -> 2 -> 3')
        self.assertEqual(len(my_queue), 3)

        my_queue.enqueue(4)
        my_queue.enqueue(5)
        self.assertEqual(str(my_queue), '1 -> 2 -> 3 -> 4 -> 5')
        self.assertEqual(len(my_queue), 5)

    def test_dequeue(self):
        my_queue = MyQueue()
        with self.assertRaises(IndexError):
            my_queue.dequeue()

        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.dequeue(), 1)
        self.assertEqual(str(my_queue), '2 -> 3')
        self.assertEqual(len(my_queue), 2)

        self.assertEqual(my_queue.dequeue(), 2)
        self.assertEqual(str(my_queue), '3')
        self.assertEqual(len(my_queue), 1)

    def test_peek(self):
        my_queue = MyQueue()
        with self.assertRaises(IndexError):
            my_queue.peek()

        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertEqual(my_queue.peek(), 1)

        my_queue.dequeue()
        self.assertEqual(my_queue.peek(), 2)

    def test_isEmpty(self):
        my_queue = MyQueue()
        self.assertTrue(my_queue.isEmpty())

        my_queue.enqueue(1)
        self.assertFalse(my_queue.isEmpty())

        my_queue.dequeue()
        self.assertTrue(my_queue.isEmpty())


if __name__ == '__main__':
    unittest.main()
