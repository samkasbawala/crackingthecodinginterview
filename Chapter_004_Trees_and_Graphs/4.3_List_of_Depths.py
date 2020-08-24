__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mytree import TreeNode
from linkedlists import SinglyLinkedList


class TreeNode(TreeNode):
    def list_of_depths(self):
        """Returns a list of linked lists of the nodes at each level"""

        # Empty list to store the linked lists
        nodes_by_level = []

        # Get the current level, which is just the root
        current_level = SinglyLinkedList()
        if self.value is not None:
            current_level.addlast(self)

        # Loop through all the levels
        while len(current_level) > 0:

            # Add the level to the list
            nodes_by_level.append(current_level)

            # The current level will be the children of the previous level
            parents = current_level
            current_level = SinglyLinkedList()

            # Loop through the children of the previous level
            current_parent = parents.head
            while current_parent is not None:
                if current_parent.data.left is not None:
                    current_level.addlast(current_parent.data.left)
                if current_parent.data.right is not None:
                    current_level.addlast(current_parent.data.right)
                current_parent = current_parent.next

        # Return the list
        return nodes_by_level

    def __str__(self):
        return str(self.value)


class TestListOfDepths(unittest.TestCase):
    def test_list_of_depths(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        b.left = a
        b.right = c
        c.right = d

        expected = ['b',
                    'a -> c',
                    'd']

        for e, r in zip(expected, b.list_of_depths()):
            self.assertEqual(e, str(r))

    def test_list_of_depths_2(self):
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

        expected = ['d',
                    'b -> f',
                    'a -> c -> e -> g']

        for e, r in zip(expected, d.list_of_depths()):
            self.assertEqual(e, str(r))


if __name__ == '__main__':
    unittest.main()
