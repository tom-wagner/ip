class Stack:
    def __init__(self, items=None):
        self.s = items if items else []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    @property
    def size(self):
        return len(self.s)


class StackOfStacks:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks = [Stack()]

    def get_last_stack(self):
        current_last_index = len(self.stacks) - 1
        return self.stacks[current_last_index]

    def push(self, val):
        last_stack = self.get_last_stack()

        if last_stack.size == self.max_size:
            self.stacks.append(Stack([val]))
        else:
            last_stack.push(val)

    def pop(self):
        last_stack = self.get_last_stack()
        if last_stack.size == 1:
            last_stack = self.stacks.pop()
        return last_stack.pop()
