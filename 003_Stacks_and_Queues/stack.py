__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


class Stack:
    """Stack implementation using a linked list structure"""

    class StackNode:
        """An object that represents each item in a stack"""

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.top = None
        self._len = 0

    def push(self, value):
        """Adds a new element to the beginning of the stack"""

        new_node = self.StackNode(value)
        new_node.next = self.top
        self.top = new_node
        self._len += 1

    def peek(self):
        """Returns the value of the top most element of the stack"""

        if self.top is None:
            raise IndexError("peek from empty")
        else:
            return self.top.value

    def pop(self):
        """Returns and removes the top most element from the stack"""

        if self.top is None:
            raise IndexError("pop from empty stack")
        return_node = self.top
        self.top = self.top.next
        return_node.next = None
        self._len -= 1
        return return_node.value

    def isEmpty(self):
        """Returns whether or not the stack is empty"""
        return self._len == 0

    def __len__(self):
        return self._len

    def __str__(self):
        def loop():
            current = self.top
            while current is not None:
                yield str(current.value)
                current = current.next
        return ' -> '.join([value for value in loop()])
