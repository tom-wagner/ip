import binarytree


class BST():
    def __init__(self, arr):
        pass

    def add(self, item):
        pass

    def largest_smaller_than_x(self, x):
        pass

    def smallest_larger_than_x(self, x):
        pass


arr = [63, 84, 57, 47, 50, 99, 57, 59, 16, 39, 86, 2, 91, 12, 97]

b = BST(arr)

# check that root.inorder is correct

b.add(37)
b.add(123)
b.add(59)

# check that root.inorder is correct

# check that it returns proper value
b.largest_smaller_than_x(77)

# check that it returns proper value
b.smallest_larger_than_x(43)

