class Node:
    def __init__(self, val):
        self.val, self.next = val, None

    def __repr__(self):
        return str(dict(val=self.val, next=self.next))


class LinkedList:
    def __init__(self, arr):
        self.head = self.tail = None
        self.init(arr)

    def init(self, arr):
        for val in arr:
            if not self.head:
                self.head = self.tail = Node(val)
                continue
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def as_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def __repr__(self):
        return str(self.as_list())


a = [5, 2, 4, 3, 8, 9, 12]
linked_list = LinkedList(a)

# print(linked_list)
