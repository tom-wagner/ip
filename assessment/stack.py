class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        pass

    def pop(self):
        pass

    @property
    def size(self):
        pass


s = Stack()

s.push(12)
s.push(14)
s.push(17)

print(s.size == 3)

print(s.pop() == 17)
print(s.pop() == 14)

s.push(18)
s.push(27)

print(s.pop() == 27)
print(s.pop() == 18)

print(s.size == 1)

print(s.pop() == 12)
print(s.pop() == 'EMPTY')

print(s.size == 0)
