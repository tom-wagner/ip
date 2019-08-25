# start time: 4:31pm


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class LL:
    def __init__(self, arr):
        self.list = None
        self.tail = None
        self.size = 0
        self.init(arr)

    def init(self, arr):
        for x in arr:
            self.add(x)

    def as_list(self):
        res = []
        curr = self.list

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res

    @property
    def head(self):
        return self.list.val

    def contains(self, x):
        return x in set(self.as_list())

    def add(self, x):
        self.size += 1
        if not self.list:
            self.list = self.tail = Node(x)
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def remove(self, x):
        if self.list.val == x:
            self.size -= 1
            self.list = self.list.next

        curr, prev = self.list.next, self.list

        while curr:
            if curr.val == x:
                self.size -= 1
                prev.next = curr.next
            prev = curr
            curr = curr.next


ll = LL([1, 2, 3, 4, 5])

print('ll should contain 5', ll.contains(5))
print('ll should not contain 8', not ll.contains(8))
print('ll size = 5', ll.size == 5)
print('ll head = 1', ll.head == 1)
print('ll tail = 5', ll.tail.val == 5)

ll.add(6)
ll.add(7)

print('ll size = 7', ll.size == 7)
print('ll tail = 5', ll.tail.val == 7)

ll.remove(1)
ll.remove(4)

print('ll removed should not include 1 or 4', ll.as_list())

# end time: 4:45pm
