__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest


class MultiStack():
    def __init__(self, space, num_stacks=3):
        self.stack_list = [None] * space * num_stacks
        self.sizes = [0] * num_stacks
        self.max_size = space

    def push(self, num_stack, value):
        if self.sizes[num_stack] < self.max_size:
            self.stack_list[self.max_size * num_stack +
                            self.sizes[num_stack]] = value
            self.sizes[num_stack] += 1
        else:
            raise IndexError("stack is full")

    def peek(self, num_stack):
        if self.sizes[num_stack] > 0:
            return self.stack_list[self.max_size * num_stack +
                                   (self.sizes[num_stack] - 1)]
        else:
            raise IndexError("peek from empty stack")

    def pop(self, num_stack):
        if self.sizes[num_stack] > 0:
            value = self.stack_list[self.max_size * num_stack +
                                    (self.sizes[num_stack] - 1)]
            self.stack_list[self.max_size *
                            num_stack + (self.sizes[num_stack] - 1)] = None
            self.sizes[num_stack] -= 1
            return value
        else:
            raise IndexError("pop from empty stack")

    def isEmpty(self, num_stack):
        return self.sizes[num_stack] == 0

    def __str__(self):
        string = ''
        for stack in range(len(self.sizes)):
            sub = ' -> '.join(str(value)
                              for value in self.stack_list[stack * self.max_size:
                                                           stack * self.max_size +
                                                           self.sizes[stack]])
            sub += '\n'
            string += sub
        return string


class TestMultiStack(unittest.TestCase):
    def test_push(self):
        three_stacks = MultiStack(2, 3)
        assert str(three_stacks) == '\n\n\n'

        three_stacks.push(0, 1)
        three_stacks.push(0, 2)
        assert str(three_stacks) == '1 -> 2\n\n\n'
        with self.assertRaises(IndexError):
            three_stacks.push(0, 3)

        three_stacks.push(1, 3)
        three_stacks.push(1, 4)
        three_stacks.push(2, 5)
        three_stacks.push(2, 6)
        assert str(three_stacks) == '1 -> 2\n3 -> 4\n5 -> 6\n'

    def test_pop(self):
        three_stacks = MultiStack(2, 3)
        assert str(three_stacks) == '\n\n\n'

        with self.assertRaises(IndexError):
            three_stacks.pop(0)

        three_stacks.push(0, 1)
        three_stacks.push(0, 2)
        three_stacks.push(1, 3)
        three_stacks.push(1, 4)
        three_stacks.push(2, 5)
        three_stacks.push(2, 6)
        assert str(three_stacks) == '1 -> 2\n3 -> 4\n5 -> 6\n'

        self.assertEqual(three_stacks.pop(0), 2)
        self.assertEqual(three_stacks.pop(0), 1)
        self.assertEqual(three_stacks.pop(1), 4)
        self.assertEqual(three_stacks.pop(1), 3)
        self.assertEqual(three_stacks.pop(2), 6)
        self.assertEqual(three_stacks.pop(2), 5)

    def test_peek(self):
        three_stacks = MultiStack(2, 3)
        assert str(three_stacks) == '\n\n\n'

        with self.assertRaises(IndexError):
            three_stacks.peek(0)

        three_stacks.push(0, 1)
        three_stacks.push(0, 2)
        three_stacks.push(1, 3)
        three_stacks.push(1, 4)
        three_stacks.push(2, 5)
        three_stacks.push(2, 6)
        assert str(three_stacks) == '1 -> 2\n3 -> 4\n5 -> 6\n'

        self.assertEqual(three_stacks.peek(0), 2)
        self.assertEqual(three_stacks.peek(1), 4)
        self.assertEqual(three_stacks.peek(2), 6)

        three_stacks.pop(0)
        three_stacks.pop(1)
        three_stacks.pop(2)

        self.assertEqual(three_stacks.peek(0), 1)
        self.assertEqual(three_stacks.peek(1), 3)
        self.assertEqual(three_stacks.peek(2), 5)

    def test_isEmpty(self):
        three_stacks = MultiStack(2, 3)
        assert str(three_stacks) == '\n\n\n'
        self.assertTrue(three_stacks.isEmpty(0))
        self.assertTrue(three_stacks.isEmpty(1))
        self.assertTrue(three_stacks.isEmpty(2))

        three_stacks.push(0, 0)
        assert str(three_stacks) == '0\n\n\n'
        self.assertFalse(three_stacks.isEmpty(0))
        self.assertTrue(three_stacks.isEmpty(1))
        self.assertTrue(three_stacks.isEmpty(2))

        self.assertEqual(three_stacks.pop(0), 0)
        assert str(three_stacks) == '\n\n\n'
        self.assertTrue(three_stacks.isEmpty(0))
        self.assertTrue(three_stacks.isEmpty(1))
        self.assertTrue(three_stacks.isEmpty(2))


if __name__ == '__main__':
    unittest.main()
