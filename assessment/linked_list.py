class LL:
    def __init__(self, arr):
        self.list = None

    @property
    def size(self):
        pass

    @property
    def head(self):
        pass

    @property
    def tail(self):
        pass

    def contains(self, x):
        pass

    def add(self, x):
        pass

    def remove(self, x):
        pass


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

print('ll removed should not include 1 or 4', ll.list)
