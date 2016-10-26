class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:

    def __init__(self, value=None):
        self.size = 0
        if value:
            self.head = Node(value)
            self.size += 1
        else:
            self.head = None

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.peek(index)

    def __setitem__(self, index, value):
        self.change(index, value)

    def __add__(self, value):
        if type(value) == type(self):
            new_list = SinglyLinkedList()
            new_list.head = self.head
            cursor = new_list.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = value.head
            new_list.size = self.size + value.size
            return new_list
        else:
            raise TypeError("can only concatenate SinglyLinkedList (not \"{}\") to SinglyLinkedList".format(type(value)))

    def add(self, value):
        self.size += 1
        if self.head:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = Node(value)
        else:
            self.head = Node(value)

    def peek(self, start):
        if start < self.size:
            cursor = self.head
            for i in range(start):
                cursor = cursor.next
            return cursor.value
        raise IndexError("list index out of range")

    def remove(self, index, r=False):
        if index < self.size:
            self.size -= 1
            cursor = self.head
            if index != 0:
                for i in range(index - 1):
                    print(cursor.value)
                    cursor = cursor.next
                to_delete = cursor.next
                cursor.next = cursor.next.next
            else:
                to_delete = self.head
                self.head = self.head.next
            return to_delete.value if r else None
        else:
            raise IndexError("list index out of range")

    def pop(self):
        if self.size > 1:
            return self.remove(self.size - 1, r=True)
        elif self.size == 1:
            popped, self.head, self.size = self.head, None, 0
            return popped.value
        else:
            raise IndexError("cannot pop from empty list")

    def insert(self, index, value):
        if index == 0:
            new_node = Node(value, self.head)
            self.head = new_node
            self.size += 1
        elif self.size > index:
            cursor = self.head
            for i in range(index - 1):
                cursor = cursor.next
            cursor.next = Node(value, cursor.next)
            self.size += 1
        else:
            self.add(value)
            
    def change(self, index, value):
        if index < self.size:
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            cursor.value = value
        else:
            raise IndexError('list index out of range')

    def reverse(self):
        if self.head:
            cursor = self.head
            prev = None
            while cursor:
                cursor.next, next = prev, cursor.next
                prev, cursor = cursor, next
            self.head = prev
    
    def copy(self):
        if self.head:
            new_list = SinglyLinkedList(self.head.value)
            while cursor:
                new_list.add(cursor.value)
                cursor = cursor.next
            return new_list
        else:
            return SinglyLinkedList()

    def __slice__(self, start=None, end=None, step=None):
        raise NotImplementedError()

    def __str__(self):
        return super().__str__(self)

def tests():
    new_list = SinglyLinkedList()
    assert len(new_list) == 0
    new_list = SinglyLinkedList(1)
    assert len(new_list) == 1
    assert new_list[0] == 1
    new_list.add("a value")
    new_list.add(0.34)
    assert new_list[1] == "a value"
    assert new_list[2] == 0.34
    try:
        new_list[3]
        assert False
    except IndexError:
        pass
    new_list.remove(0)
    assert new_list.head.value == "a value"
    assert new_list.head.next.value == 0.34
    assert new_list[0] == "a value", new_list[0]
    assert new_list[1] == 0.34
    result = new_list.remove(1)
    assert result is None
    assert new_list.head.value == "a value"
    assert new_list.head.next == None
    assert len(new_list) == 1
    assert new_list.size == 1
    new_list.add(0.34)
    assert len(new_list) == 2
    result = new_list.pop()
    assert result == 0.34, result
    new_list = SinglyLinkedList("Norton")
    assert new_list.pop() == "Norton"
    assert new_list.head == None
    new_list.insert(0, 'Norton')
    assert new_list.head.value == 'Norton', new_list.head.value
    new_list.add('Oliver')
    new_list.add('James')
    new_list.insert(2, 'Collins')
    assert new_list[0] == 'Norton' == new_list.head.value
    assert new_list[1] == 'Oliver' == new_list.head.next.value
    assert new_list[2] == 'Collins' == new_list.head.next.next.value
    assert new_list[3] == 'James' == new_list.head.next.next.next.value, new_list.head.next.next.next.value 
    new_list[2] = "Jackson"
    assert new_list[2] == "Jackson"
    list_a = SinglyLinkedList('A')
    list_a.add('B')
    list_b = SinglyLinkedList('C')
    list_all = list_a + list_b
    assert list_all.head.value == 'A'
    assert len(list_all) == 3, len(list_all)
    assert list_all[0] == 'A'
    assert list_all[1] == 'B'
    assert list_all[2] == 'C'
    list_all.reverse()
    assert list_all[0] == 'C'
    assert list_all[1] == 'B'
    assert list_all[2] == 'A'
    


tests()