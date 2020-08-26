__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mytree import TreeNode


def is_bst(root):
    if root is None:
        return False

    else:
        prev = next(in_order(root))
        for value in in_order(root):
            if value < prev:
                return False
            prev = value
        return True


def in_order(root):
    """Returns the elements in a tree using in_order traversal"""

    if root is not None:
        for item in in_order(root.left):
            yield item
        yield root.value
        for item in in_order(root.right):
            yield item


class TestIsBST(unittest.TestCase):
    def test_in_order(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        e = TreeNode('e')
        f = TreeNode('f')
        g = TreeNode('g')

        d.left = b
        d.right = f

        b.left = a
        b.right = c

        f.left = e
        f.right = g

        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                         [value for value in in_order(d)])

    def test_is_bst(self):
        tree_1 = TreeNode(2)
        tree_1.left = TreeNode(1)
        tree_1.right = TreeNode(3)
        self.assertTrue(is_bst(tree_1))
        self.assertTrue(is_bst(tree_1.left))
        self.assertTrue(is_bst(tree_1.right))

        tree_2 = TreeNode(1)
        tree_2.left = TreeNode(2)
        tree_2.right = TreeNode(3)
        self.assertFalse(is_bst(tree_2))
        self.assertTrue(is_bst(tree_2.left))
        self.assertTrue(is_bst(tree_2.right))

        tree_3 = TreeNode(1)
        tree_3.left = TreeNode(1)
        tree_3.right = TreeNode(1)
        self.assertTrue(is_bst(tree_3))
        self.assertTrue(is_bst(tree_3.left))
        self.assertTrue(is_bst(tree_3.right))

        tree_4 = TreeNode(0)
        self.assertTrue(is_bst(tree_4))

        self.assertFalse(is_bst(None))


if __name__ == '__main__':
    unittest.main()
