__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from linkedlists import *


def sum_lists_reverse(list1, list2):
    sum = SinglyLinkedList()
    current1 = list1.head
    current2 = list2.head
    carry = 0
    while current1 is not None and current2 is not None:
        partial_sum, carry = partial_sum_and_carry(current1.data,
                                                   current2.data,
                                                   carry)
        sum.addlast(partial_sum)
        current1 = current1.next
        current2 = current2.next
    while current1 is not None:
        partial_sum, carry = partial_sum_and_carry(current1.data,
                                                   0,
                                                   carry)
        sum.addlast(partial_sum)
        current1 = current1.next
    while current2 is not None:
        partial_sum, carry = partial_sum_and_carry(0,
                                                   current2.data,
                                                   carry)
        sum.addlast(partial_sum)
        current2 = current2.next
    if carry == 1:
        sum.addlast(carry)
    return sum


def partial_sum_and_carry(addend1, addend2, carry):
    if addend1 + addend2 + carry >= 10:
        return (addend1 + addend2 + carry) % 10, 1
    else:
        return addend1 + addend2 + carry, 0


class TestSumLists(unittest.TestCase):

    def test_sum_list_reverse(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()

        ll1.addlast(7)
        ll1.addlast(1)
        ll1.addlast(6)

        ll2.addlast(5)
        ll2.addlast(9)
        ll2.addlast(2)

        assert str(ll1) == '7, 1, 6'
        assert str(ll2) == '5, 9, 2'
        sum = sum_lists_reverse(ll1, ll2)
        assert str(sum) == '2, 1, 9'

    def test_sum_list_reverse_carry(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()

        ll1.addlast(9)
        ll1.addlast(9)
        ll1.addlast(9)

        ll2.addlast(9)
        ll2.addlast(9)
        ll2.addlast(9)
        ll2.addlast(9)
        ll2.addlast(9)
        ll2.addlast(9)

        assert str(ll1) == '9, 9, 9'
        assert str(ll2) == '9, 9, 9, 9, 9, 9'
        sum = sum_lists_reverse(ll1, ll2)
        assert str(sum) == '8, 9, 9, 0, 0, 0, 1'

    def test_sum_list_reverse_simple(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()

        ll1.addlast(1)
        ll1.addlast(1)
        ll1.addlast(1)

        ll2.addlast(8)
        ll2.addlast(8)
        ll2.addlast(8)

        assert str(ll1) == '1, 1, 1'
        assert str(ll2) == '8, 8, 8'
        sum = sum_lists_reverse(ll1, ll2)
        assert str(sum) == '9, 9, 9'


if __name__ == '__main__':
    unittest.main()
