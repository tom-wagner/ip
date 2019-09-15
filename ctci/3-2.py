import math


class S:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if len(self.stack) > 0:
            current_min = self.stack[len(self.stack) - 1][1]
        else:
            current_min = math.inf
        self.stack.append([item, min(item, current_min)])

    def pop(self):
        item, _ = self.stack.pop()
        return item

    def min(self):
        if not len(self.stack):
            return None
        return self.stack[len(self.stack) - 1][1]
