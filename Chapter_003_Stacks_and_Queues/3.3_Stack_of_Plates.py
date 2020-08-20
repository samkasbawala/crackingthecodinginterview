__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mystack import Stack


class SetOfStacks():
    class StackWithCap(Stack):
        def __init__(self):
            self.next = None
            super().__init__()

    def __init__(self, capacity):
        self.top_stack = self.StackWithCap()
        self.capacity = capacity
        self.num_stacks = 1

    def push(self, value):
        if len(self.top_stack) >= self.capacity:
            new_stack = self.StackWithCap()
            new_stack.next = self.top_stack
            self.top_stack = new_stack
            self.num_stacks += 1
        self.top_stack.push(value)

    def pop(self):
        if len(self.top_stack) == 1 and self.num_stacks > 1:
            top_stack = self.top_stack
            self.top_stack = self.top_stack.next
            top_stack.next = None
            self.num_stacks -= 1
            return top_stack.pop()
        return self.top_stack.pop()

    def peek(self):
        return self.top_stack.peek()

    def isEmpty(self):
        return self.num_stacks == 1 and self.top_stack.isEmpty()

    def __str__(self):
        def loop():
            current_stack = self.top_stack
            while current_stack is not None:
                yield str(current_stack)
                current_stack = current_stack.next
        return ' -> '.join([value for value in loop()])


class TestSetOfStacks(unittest.TestCase):
    def test_push(self):
        stacks = SetOfStacks(2)
        stacks.push(1)
        stacks.push(2)
        self.assertEqual(stacks.num_stacks, 1)
        self.assertEqual(str(stacks), "2 -> 1")

        stacks.push(3)
        self.assertEqual(stacks.num_stacks, 2)
        self.assertEqual(str(stacks), "3 -> 2 -> 1")

        stacks.push(4)
        self.assertEqual(stacks.num_stacks, 2)
        self.assertEqual(str(stacks), "4 -> 3 -> 2 -> 1")

        stacks.push(5)
        self.assertEqual(stacks.num_stacks, 3)
        self.assertEqual(str(stacks), "5 -> 4 -> 3 -> 2 -> 1")

    def test_pop(self):
        stacks = SetOfStacks(2)
        with self.assertRaises(IndexError):
            stacks.pop()

        stacks.push(1)
        self.assertEqual(stacks.pop(), 1)

        stacks.push(1)
        stacks.push(2)
        stacks.push(3)
        stacks.push(4)
        stacks.push(5)
        self.assertEqual(stacks.num_stacks, 3)
        self.assertEqual(str(stacks), "5 -> 4 -> 3 -> 2 -> 1")

        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(str(stacks), "4 -> 3 -> 2 -> 1")
        self.assertEqual(stacks.num_stacks, 2)

        self.assertEqual(stacks.pop(), 4)
        self.assertEqual(str(stacks), "3 -> 2 -> 1")
        self.assertEqual(stacks.num_stacks, 2)

        self.assertEqual(stacks.pop(), 3)
        self.assertEqual(str(stacks), "2 -> 1")
        self.assertEqual(stacks.num_stacks, 1)

        stacks.push(3)
        self.assertEqual(str(stacks), "3 -> 2 -> 1")
        self.assertEqual(stacks.num_stacks, 2)

    def test_peek(self):
        stacks = SetOfStacks(2)
        with self.assertRaises(IndexError):
            stacks.peek()

        stacks.push(1)
        self.assertEqual(stacks.peek(), 1)
        stacks.push(2)
        self.assertEqual(stacks.peek(), 2)
        stacks.push(3)
        self.assertEqual(stacks.peek(), 3)

        stacks.pop()
        self.assertEqual(stacks.peek(), 2)

    def test_isEmpty(self):
        stacks = SetOfStacks(2)
        self.assertTrue(stacks.isEmpty())

        stacks.push(1)
        stacks.push(2)
        self.assertEqual(str(stacks), "2 -> 1")
        self.assertFalse(stacks.isEmpty())

        self.assertEqual(stacks.pop(), 2)
        self.assertEqual(str(stacks), "1")
        self.assertFalse(stacks.isEmpty())

        stacks.pop()
        self.assertTrue(stacks.isEmpty())


if __name__ == '__main__':
    unittest.main()
