class Node:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self, value=None):
        if value is None:
            self.head = self.tail = None
        