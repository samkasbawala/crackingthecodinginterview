__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


class Queue():
    """Queue implementation using a linked list"""

    class QueueNode():
        """An object that represents each item in the queue"""

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def enqueue(self, value):
        """Adds a new element to the end of the queue"""

        new_node = self.QueueNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._len += 1

    def dequeue(self):
        """Returns and removes the element at the beginning of the queue"""

        if self.head is None:
            raise IndexError("remove from empty queue")
        return_node = self.head
        self.head = self.head.next
        return_node.next = None
        self._len -= 1
        return return_node.value

    def peek(self):
        """Returns the element at the beginning of the queue"""

        return self.head.value

    def isEmpty(self):
        """Checks if the queue is empty"""

        return self._len == 0

    def __len__(self):
        return self._len

    def __str__(self):
        def loop():
            current = self.head
            while current is not None:
                yield str(current.value)
                current = current.next
        return ' -> '.join([value for value in loop()])
