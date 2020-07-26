__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


from linkedlists import *
import unittest


def return_kth_to_last(ll: SinglyLinkedList, k: int) -> any:
    assert k >= 1, "K must be greater than 0"
    ptr1 = ll.head
    ptr2 = ll.head
    for i in range(k):
        if ptr2 is None:
            return None
        ptr2 = ptr2.next
    while ptr2 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1.data


class TestReturnKthToLast(unittest.TestCase):
    def test_return_kth_to_last(self):
        ll = SinglyLinkedList()
        ll.addlast(1)
        ll.addlast(2)
        ll.addlast(3)
        ll.addlast(4)
        ll.addlast(5)
        ll.addlast(6)
        self.assertEqual(str(ll), '1, 2, 3, 4, 5, 6')
        self.assertEqual(return_kth_to_last(ll, 1), 6)
        self.assertEqual(return_kth_to_last(ll, 2), 5)
        self.assertEqual(return_kth_to_last(ll, 6), 1)
        with self.assertRaises(AssertionError):
            return_kth_to_last(ll, 0)


if __name__ == '__main__':
    unittest.main()
