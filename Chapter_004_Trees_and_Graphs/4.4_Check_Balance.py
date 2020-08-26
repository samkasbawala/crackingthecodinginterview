__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mytree import TreeNode


# Method 1: Most intuitive method of solving this question for me
# Takes O(n log n)
def height(root):
    """Return the height of a tree, given it's root"""

    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def balanced(root):
    """Determine if a tree is balanced given it's root

    Check if the left and right subtrees are balanced
    """

    if root is None:
        return True

    if abs(height(root.left) - height(root.right)) <= 1:
        return balanced(root.left) and balanced(root.right)
    else:
        return False


# Method 2: Time optimized
# Takes O(n)
def is_balanced(root):
    def check(root):
        if root is None:
            return 0
        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return check(root) != -1


class TestBalanced(unittest.TestCase):
    def test_height(self):
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

        self.assertEqual(height(d), 3)
        self.assertEqual(height(b), 2)
        self.assertEqual(height(a), 1)
        self.assertEqual(height(None), 0)

    def test_balanced(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        e = TreeNode('e')
        f = TreeNode('f')
        g = TreeNode('g')

        d.left = b
        b.left = a

        self.assertFalse(balanced(d))
        self.assertTrue(balanced(a))

        d.right = f

        self.assertTrue(balanced(d))

        b.right = c

        f.left = e
        f.right = g

        self.assertTrue(balanced(d))
        self.assertTrue(balanced(b))
        self.assertTrue(balanced(a))
        self.assertTrue(balanced(None))

    def test_is_balanced(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        e = TreeNode('e')
        f = TreeNode('f')
        g = TreeNode('g')

        d.left = b
        b.left = a

        self.assertFalse(is_balanced(d))
        self.assertTrue(balanced(a))

        d.right = f

        self.assertTrue(is_balanced(d))

        b.right = c

        f.left = e
        f.right = g

        self.assertTrue(is_balanced(d))
        self.assertTrue(is_balanced(b))
        self.assertTrue(is_balanced(a))
        self.assertTrue(is_balanced(None))


if __name__ == '__main__':
    unittest.main()
