# START TIME: 3:58pm

from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = []
#         self.pointer = 0
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def deque(self):
#         if self.size == 0:
#             return 'EMPTY'
#         res = self.queue[self.pointer]
#         self.pointer += 1
#         return res
#
#     @property
#     def size(self):
#         return len(self.queue) - self.pointer


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        try:
            return self.queue.popleft()
        except:
            return 'EMPTY'

    @property
    def size(self):
        return len(self.queue)


q = Queue()

q.enqueue(12)
q.enqueue(14)
q.enqueue(17)

print(q.size == 3)

print(q.deque() == 12)
print(q.deque() == 14)
#
q.enqueue(18)
q.enqueue(27)
#
print(q.deque() == 17)
print(q.deque() == 18)

print(q.size == 1)

print(q.deque() == 27)
print(q.deque() == 'EMPTY')
#
# print(q.size == 0)

# END TIME: 4:04 PM
