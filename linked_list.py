class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(dict(val=self.val, next=self.next))


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return str(self.head)

    def add_node(self, val):
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


LL = LinkedList()

LL.add_node(3)
LL.add_node(4)
LL.add_node(5)
LL.add_node(6)

print(LL)
