class Node:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next_setter(self, value):
        self._next = value
        value._prev = self

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev_setter(self, value):
        self._prev = value
        value._next = self



class DoublyLinkedList:

    def __init__(self, value=None):
        self.size = 0
        if value is None:
            self.head = self.tail = None
        else:
            self.head = self.tail = Node(value)
            self.size += 1

    def add(self, value):
        self.size += 1
        if self.head:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = Node(value)
        else:
            self.head = Node(value)
        
    