__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from linkedlists import *


def start_of_loop_set(ll):
    """If there is a loop in the linked list, return the start of the loop.
    If there is not loop, return None"
    """

    # Set to hold seen nodes
    seen = set()

    current = ll
    while current is not None:
        if current in seen:
            return current
        else:
            seen.add(current)
            current = current.next

    # No loop in the linked list
    return None


def start_of_loop_optimized(ll):
    """If there is a loop in the linked list, return the start of the loop.
    If there is not loop, return None"
    """

    # Set up two pointers
    tortoise = ll
    hare = ll

    while hare is not None and hare.next is not None:
        # Hare moves twice as fast as tortoise
        tortoise = tortoise.next
        hare = hare.next.next

        # If they are at the same spot, that means we have a loop
        if tortoise is hare:
            hare = ll
            while tortoise is not hare:
                tortoise = tortoise.next
                hare = hare.next
            return tortoise

    # No loop in the linked list
    return None


class TestStartOfLoop(unittest.TestCase):
    def setUp(self):
        self.a = SinglyLinkedListNode('a')
        self.b = SinglyLinkedListNode('b')
        self.c = SinglyLinkedListNode('c')
        self.d = SinglyLinkedListNode('d')
        self.e = SinglyLinkedListNode('e')

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e

    def test_start_of_loop_set(self):
        assert start_of_loop_set(self.a) is None
        assert start_of_loop_set(self.e) is None
        assert start_of_loop_set(self.c) is None

        self.e.next = self.c

        assert start_of_loop_set(self.a) is self.c
        assert start_of_loop_set(self.b) is self.c
        assert start_of_loop_set(self.e) is self.e

    def test_start_of_loop_optimized(self):
        assert start_of_loop_optimized(self.a) is None
        assert start_of_loop_optimized(self.e) is None
        assert start_of_loop_optimized(self.c) is None

        self.e.next = self.c

        assert start_of_loop_optimized(self.a) is self.c
        assert start_of_loop_optimized(self.b) is self.c
        assert start_of_loop_optimized(self.e) is self.e


if __name__ == '__main__':
    unittest.main()
