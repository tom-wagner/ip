
# START TIME:


class Heap:
    def __init__(self, arr):
        pass

    def contains(self, x):
        pass

    def add(self, x):
        pass

    def pop(self):
        pass


h = Heap([5, 6, 1, 2, 12, 17, 9, 4, 8, 23, 16, 7, 19, 21])

h.add(26)
h.add(15)
h.add(-16)

print('h contains 8', h.contains(8))
print('h does not contain 923', not h.contains(923))
print('h should pop 26', h.pop() == 26)
print('h should pop 23', h.pop() == 23)
print('h should pop 21', h.pop() == 21)

# END TIME:
