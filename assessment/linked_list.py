# start time: 1:13pm


class Node:
    def __init__(self, val):
        self.v = val
        self.next = None


class LL:
    def __init__(self, arr):
        self.h = None
        self.t = None
        self.length = 0
        self.init(arr)

    def init(self, arr):
        for x in arr:
            self.add(x)

    def as_list(self):
        res = []
        curr = self.h
        while curr:
            res.append(curr.v)
            curr = curr.next

        return res

    @property
    def size(self):
        return self.length

    @property
    def head(self):
        return self.h.v

    @property
    def tail(self):
        return self.t.v

    def contains(self, x):
        return x in self.as_list()

    def add(self, x):
        self.length += 1

        if not self.h:
            self.h = self.t = Node(x)
        else:
            self.t.next = Node(x)
            self.t = self.t.next

    def remove(self, x):
        if x == self.h.v:
            self.h = self.h.next
            self.length -= 1
            return

        prev, curr = self.h, self.h.next

        while curr:
            if curr.v == x:
                prev.next = curr.next
                self.length -= 1
                return

            prev, curr = curr, curr.next


ll = LL([1, 2, 3, 4, 5])

print('ll should contain 5', ll.contains(5))
print('ll should not contain 8', not ll.contains(8))
print('ll size = 5', ll.size == 5)
print('ll head = 1', ll.head == 1)
print('ll tail = 5', ll.tail == 5)

ll.add(6)
ll.add(7)

print('ll size = 7', ll.size == 7)
print('ll tail = 5', ll.tail == 7)

ll.remove(1)
ll.remove(4)

print('ll removed should not include 1 or 4', ll.as_list())
