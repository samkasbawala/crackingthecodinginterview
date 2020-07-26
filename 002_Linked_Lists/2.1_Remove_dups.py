__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'

from linkedlists import *
import unittest


def remove_dups(ll: SinglyLinkedList):
    """This function deletes duplicate values from a singly linked list"""
    seen = set()
    current = ll.head
    prev = None
    while current is not None:
        if current.data in seen:
            prev.next = current.next
            temp = current
            current = current.next
            temp.next = None
        else:
            seen.add(current.data)
            prev = current
            current = current.next


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups_1(self):
        ll = SinglyLinkedList()
        ll.addlast(1)
        ll.addlast(2)
        ll.addlast(3)
        ll.addlast(4)
        ll.addlast(5)
        ll.addlast(5)
        self.assertEqual(str(ll), '1, 2, 3, 4, 5, 5')
        remove_dups(ll)
        self.assertEqual(str(ll), '1, 2, 3, 4, 5')

    def test_remove_dups_2(self):
        ll = SinglyLinkedList()
        ll.addlast(1)
        ll.addlast(1)
        ll.addlast(2)
        ll.addlast(3)
        ll.addlast(4)
        ll.addlast(4)
        ll.addlast(5)
        ll.addlast(5)
        self.assertEqual(str(ll), '1, 1, 2, 3, 4, 4, 5, 5')
        remove_dups(ll)
        self.assertEqual(str(ll), '1, 2, 3, 4, 5')


if __name__ == '__main__':
    unittest.main()
