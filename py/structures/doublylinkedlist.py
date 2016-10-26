class Node:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self._next = None
        self._prev = None
        self.next = next
        self.prev = prev

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
        if self.tail and self.head:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = Node(value)
        
    def peek(self, index):
        if index < (self.size // 2):
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            return cursor.value
        elif index < self.size:
            cursor = self.tail
            for i in range(self.size - index):
                cursor = cursor.prev
            return cursor.value
        raise IndexError('list index out of range')

    def remove(self, index, r=False):
        if index < (self.size // 2):
            cursor = self.head
            if index != 0:
                for i in range(index - 1):
                    cursor = cursor.next
                to_delete = cursor.next
                cursor.next = cursor.next.next
            else:
                to_delete = self.head
                self.head = self.head.next
        elif index < self.size:
            reverse_index = self.size - index - 1
            cursor = self.tail
            if reverse_index != 0:
                for i in range(reverse_index):
                    cursor = cursor.prev
                to_delete = cursor.prev
                cursor.prev = cursor.prev.prev
            else:
                to_delete = self.tail
                self.tail = self.tail.prev
        else:
            raise IndexError('list index out of range')    
        self.size -= 1
        return to_delete.value if r else None
        
    def pop(self):
        if self.size > 1:
            return self.remove(self.size - 1, r=True)
        elif self.size == 1:
            popped = self.tail
            self.tail = self.head = None
            self.size = 0
            return popped.value
        else:
            raise IndexError("cannot pop from empty list")

    def insert(self, index, value):
        if index == 0:
            self.head = Node(value, self.head)
        elif index < (self.size // 2):
            cursor = self.head
            for i in range(index - 1):
                cursor = cursor.next
            cursor.next = Node(value, cursor.next)
        elif index < self.size:
            cursor = self.tail
            inverse_index = self.size - index - 1
            for i in range(inverse_index):
                cursor = cursor.prev
            cursor.prev = Node(value, None, cursor.prev)
        else:
            self.add(value)
        self.size += 1

    def change(self, index, value):
        if index < (self.size // 2):
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            cursor.value = value
        elif index < self.size:
            inverse_index = self.size - index - 1
            cursor = self.tail
            for i in range(inverse_index):
                cursor = cursor.prev
            cursor.value = value
        else:
            raise IndexError('list index out of range')
            
            
            
    