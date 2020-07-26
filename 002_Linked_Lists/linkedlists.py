class SinglyLinkedListNode:
    def __init__(self, data: any, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addfirst(self, value: int):
        self.head = SinglyLinkedListNode(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self.length += 1

    def addlast(self, value: int):
        if self.head is None:
            self.addfirst(value)
        else:
            self.tail.next = SinglyLinkedListNode(value)
            self.tail = self.tail.next
            self.length += 1

    def removefirst(self) -> any:
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return value

    def removelast(self) -> any:
        if self.head is self.tail:
            return self.removefirst()
        current = self.head
        while current.next is not self.tail:
            current = current.next
        value = self.tail.data
        self.length -= 1
        self.tail = current
        self.tail.next = None
        return value

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return ', '.join(items)

    def __eq__(self, value):
        return self.__str__() == value.__str__()

    def __len__(self):
        return self.length
