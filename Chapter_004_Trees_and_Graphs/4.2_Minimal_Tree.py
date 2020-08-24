__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mytree import TreeNode, in_order_traversal


def array_to_bst(array):
    """Converts a sorted array into a BST"""

    if not array:
        return None

    mid = len(array) // 2
    root = TreeNode(array[mid])
    root.left = array_to_bst(array[:mid])
    root.right = array_to_bst(array[mid+1:])

    return root


class TestArrayToBST(unittest.TestCase):
    def test_array_to_bst(self):
        root = array_to_bst([1, 2, 3])
        self.assertEqual([1, 2, 3], in_order_traversal(root))

        root = array_to_bst([1, 2, 3, 4, 5, 6])
        self.assertEqual([1, 2, 3, 4, 5, 6], in_order_traversal(root))


if __name__ == '__main__':
    unittest.main()
