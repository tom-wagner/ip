# start time: 7:37pm


class Node:
    def __init__(self, val):
        self.val, self.next = val, None


class LL:
    def __init__(self, arr):
        self.h = self.t = None
        self.init(arr)

    def init(self, arr):
        for x in arr:
            self.add(x)

    def as_list(self):
        res = []
        curr = self.h

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res

    @property
    def size(self):
        return len(self.as_list())

    @property
    def head(self):
        return self.h.val

    @property
    def tail(self):
        return self.t.val

    def contains(self, x):
        return x in set(self.as_list())

    def add(self, x):
        if not self.h:
            self.h = self.t = Node(x)
            return
        self.t.next = Node(x)
        self.t = self.t.next

    def remove(self, x):
        head = self.h
        if head.val == x:
            self.h = self.h.next

        curr, prev = head.next, head
        while curr:
            print(curr.val, prev.val)
            if curr.val == x:
                prev.next = curr.next
                break
            curr, prev = curr.next, prev.next


ll = LL([1, 2, 3, 4, 5])

print(ll.as_list())

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

# end time: 7:48pm
