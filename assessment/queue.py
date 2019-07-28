# START TIME:


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        pass

    def deque(self):
        pass

    @property
    def size(self):
        pass


q = Queue()

q.enqueue(12)
q.enqueue(14)
q.enqueue(17)

print(q.size == 3)

print(q.deque() == 12)
print(q.deque() == 14)

q.enqueue(18)
q.enqueue(27)

print(q.deque() == 17)
print(q.deque() == 18)

print(q.size == 1)

print(q.deque() == 27)
print(q.deque() == 'EMPTY')

print(q.size == 0)

# END TIME:
