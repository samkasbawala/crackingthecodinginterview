__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def in_order_traversal(root):

    def traverse(root):
        if root is not None:
            traverse(root.left)
            array.append(root.value)
            traverse(root.right)
    array = []
    traverse(root)
    return array
