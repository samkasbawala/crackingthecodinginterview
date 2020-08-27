__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def next_node(node):
    """Returns the next node in the in-order sequence given the current node"""

    # If the node is None, then there is no next node
    if node is None:
        return None

    # In-order traversal goes: left -> current -> right
    # If at current, then the next node is the left most of the right tree
    if node.right is not None:
        current_node = node.right
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # If there is no right sub-tree, and we are on the left side of the parent
    # node, the next node is the parent node. If we are on the right side of
    # the parent node, we need to traverse up until we find a node that hasn't
    # been traversed. We know a node hasn't been traversed if we move from
    # it's left child to the parent
    child = node
    parent = node.parent

    while (parent is not None and parent.right is child):
        child = child.parent
        parent = parent.parent
    return parent


class TestNextNode(unittest.TestCase):
    def test_next_node(self):
        tree_1 = TreeNode(2)
        tree_1.left = TreeNode(1)
        tree_1.left.parent = tree_1
        tree_1.right = TreeNode(3)
        tree_1.right.parent = tree_1

        self.assertTrue(next_node(tree_1), tree_1.right)
        self.assertTrue(next_node(tree_1.left), tree_1)
        self.assertIsNone(next_node(tree_1.right))

        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        e = TreeNode('e')
        f = TreeNode('f')
        g = TreeNode('g')

        d.left = b
        b.parent = d
        d.right = f
        f.parent = d

        b.left = a
        a.parent = b
        b.right = c
        c.parent = b

        f.left = e
        e.parent = f
        f.right = g
        g.parent = f

        self.assertTrue(next_node(d), e)
        self.assertTrue(next_node(a), b)
        self.assertTrue(next_node(e), f)
        self.assertTrue(next_node(f), g)
        self.assertIsNone(next_node(g))

        self.assertIsNone(next_node(None))


if __name__ == '__main__':
    unittest.main()
