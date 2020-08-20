__author__ = "Sam Kasbawala"
__credits__ = "Sam Kasbawala"


import unittest
from linkedlists import *


def is_intersection(ll1, ll2):
    """Checks if two linked lists intersect and returns the intersecting
    node. Returns None if there is no intersecting node.
    """

    ll1_len = 0
    ll1_tail = None
    ll1_current = ll1

    ll2_len = 0
    ll2_tail = None
    ll2_current = ll2

    # Get length of first linked list
    while ll1_current is not None:
        ll1_len += 1
        ll1_tail = ll1_current
        ll1_current = ll1_current.next

    # Get length of second linked list
    while ll2_current is not None:
        ll2_len += 1
        ll2_tail = ll2_current
        ll2_current = ll2_current.next

    # If the ends of the tails are not t
    if ll1_tail is not ll2_tail:
        return None

    # Get the difference between their lengths
    diff = abs(ll1_len - ll2_len)

    # Loop through difference, where the lists intersect should be the same
    # for the rest of the list
    ll1_current = ll1
    ll2_current = ll2
    if ll1_len > ll2_len:
        for _ in range(diff):
            ll1_current = ll1_current.next
    else:
        for _ in range(diff):
            ll2_current = ll2_current.next

    while ll1_current is not ll2_current:
        ll1_current = ll1_current.next
        ll2_current = ll2_current.next

    return ll1_current


class TestIsIntersection(unittest.TestCase):
    def test_is_intersection(self):
        a = SinglyLinkedListNode("a")
        b = SinglyLinkedListNode("b")
        c = SinglyLinkedListNode("c")
        d = SinglyLinkedListNode("d")
        e = SinglyLinkedListNode("e")
        y = SinglyLinkedListNode("y")
        z = SinglyLinkedListNode("z")

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        y.next = z

        assert is_intersection(a, a) is a
        assert is_intersection(a, b) is b
        assert is_intersection(a, c) is c
        assert is_intersection(a, d) is d
        assert is_intersection(a, e) is e
        assert is_intersection(b, c) is c

        assert is_intersection(y, a) is None
        assert is_intersection(y, b) is None
        assert is_intersection(y, c) is None
        assert is_intersection(y, d) is None
        assert is_intersection(y, e) is None

        z.next = a
        assert is_intersection(y, a) is a
        assert is_intersection(z, a) is a
        assert is_intersection(y, c) is c
        assert is_intersection(z, e) is e


if __name__ == "__main__":
    unittest.main()
