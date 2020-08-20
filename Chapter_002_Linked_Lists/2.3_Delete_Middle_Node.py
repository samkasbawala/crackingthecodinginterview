__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


from linkedlists import *
import unittest


def delete_middle_node(node):
    temp_next = node.next
    if temp_next is None:
        raise Exception('Cannot delete from tail')
    node.data = temp_next.data
    node.next = temp_next.next
    temp_next.next = None
    return


class TestDeleteMiddleNode(unittest.TestCase):
    def setUp(self):
        self.a = SinglyLinkedListNode('a')
        self.b = SinglyLinkedListNode('b')
        self.c = SinglyLinkedListNode('c')
        self.d = SinglyLinkedListNode('d')
        self.e = SinglyLinkedListNode('e')
        self.f = SinglyLinkedListNode('f')

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e
        self.e.next = self.f

    def print_list(self, head):
        return ', '.join([n for n in self.loop_list(head)])

    def loop_list(self, node):
        current = node
        while current is not None:
            yield current.data
            current = current.next

    def test_delete_middle_node(self):
        assert self.print_list(self.a) == 'a, b, c, d, e, f'
        delete_middle_node(self.c)
        assert self.print_list(self.a) == 'a, b, d, e, f'

    def test_delete_middle_node_2(self):
        assert self.print_list(self.a) == 'a, b, c, d, e, f'
        with self.assertRaises(Exception):
            delete_middle_node(self.f)
        delete_middle_node(self.e)
        assert self.print_list(self.a) == 'a, b, c, d, f'


if __name__ == '__main__':
    unittest.main()
