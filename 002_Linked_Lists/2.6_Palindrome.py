__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from linkedlists import *


def is_palindrome(ll):
    ll_reversed = reverse_ll(ll)
    current = ll.head
    current_rev = ll_reversed.head
    while current is not None and current_rev is not None:
        if current.data != current_rev.data:
            return False
        current = current.next
        current_rev = current_rev.next
    return True


def reverse_ll(ll):
    reversed = SinglyLinkedList()
    current = ll.head
    while current is not None:
        reversed.addfirst(current.data)
        current = current.next
    return reversed


class TestIsPalindrome(unittest.TestCase):
    def test_reverse_ll(self):
        l1 = SinglyLinkedList()
        l1.addlast('s')
        l1.addlast('a')
        l1.addlast('m')

        assert str(l1) == 's, a, m'
        assert str(reverse_ll(l1)) == 'm, a, s'

    def test_is_palindrome(self):
        l1 = SinglyLinkedList()
        l1.addlast('s')
        l1.addlast('a')
        l1.addlast('m')
        assert str(l1) == 's, a, m'
        assert is_palindrome(l1) is False

        l2 = SinglyLinkedList()
        l2.addlast('m')
        l2.addlast('o')
        l2.addlast('m')
        assert str(l2) == 'm, o, m'
        assert is_palindrome(l2) is True


if __name__ == '__main__':
    unittest.main()
