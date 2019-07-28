# START TIME: 3:06pm

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, a):
        self.bst = Node(None)
        self.init_from_arr(a)

    def init_from_arr(self, a):
        for val in a:
            self.add(val)

    def add(self, item):
        if not self.bst.val:
            self.bst = Node(item)
            return

        curr = self.bst

        while True:
            if item < curr.val:
                if not curr.left:
                    curr.left = Node(item)
                    return
                curr = curr.left
            elif item > curr.val:
                if not curr.right:
                    curr.right = Node(item)
                    return
                curr = curr.right
            else:
                raise Exception

    def largest_smaller_than_x(self, x):
        min_diff = None
        largest_smaller_than = None

        def recurse(bst):
            nonlocal min_diff, largest_smaller_than
            if bst.left and x < bst.val:
                recurse(bst.left)
            if bst.right and x > bst.val:
                recurse(bst.right)

            if (not min_diff and bst.val < x) or (bst.val < x and x - bst.val < min_diff):
                largest_smaller_than = bst.val
                min_diff = x - bst.val

        recurse(self.bst)
        return largest_smaller_than

    def smallest_larger_than_x(self, x):
        min_diff = None
        smallest_larger_than = None

        def recurse(bst):
            nonlocal min_diff, smallest_larger_than
            if bst.left and x < bst.val:
                recurse(bst.left)
            if bst.right and x > bst.val:
                recurse(bst.right)

            if (not min_diff and bst.val > x) or (bst.val > x and bst.val - x < min_diff):
                smallest_larger_than = bst.val
                min_diff = bst.val - x

        recurse(self.bst)
        return smallest_larger_than

    def in_order(self):
        res = []

        def recurse(subtree):
            if subtree.left:
                recurse(subtree.left)

            res.append(subtree.val)

            if subtree.right:
                recurse(subtree.right)

        recurse(self.bst)
        return res

    def pre_order(self):
        res = []

        def recurse(subtree):
            res.append(subtree.val)
            if subtree.left:
                recurse(subtree.left)
            if subtree.right:
                recurse(subtree.right)

        recurse(self.bst)
        return res

    def post_order(self):
        res = []

        def recurse(subtree):
            if subtree.left:
                recurse(subtree.left)
            if subtree.right:
                recurse(subtree.right)
            res.append(subtree.val)

        recurse(self.bst)
        return res

    def breadth_first(self):
        res = []

        q = deque()
        q.append(self.bst)
        while q:
            curr = q.popleft()
            res.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return res


arr = [63, 84, 57, 47, 50, 99, 59, 16, 39, 86, 2, 91, 12, 97]

b = BST(arr)

b.add(37)
b.add(123)
b.add(72)
b.add(77)

print(b.bst.right.val)

try:
    b.add(63)  # should be rejected
    print('ERROR -- should not get here')
except Exception:
    print('properly rejected 63')

ino = [2, 12, 16, 37, 39, 47, 50, 57, 59, 63, 72, 77, 84, 86, 91, 97, 99, 123]
pre = [63, 57, 47, 16, 2, 12, 39, 37, 50, 59, 84, 72, 77, 99, 86, 91, 97, 123]
pos = [12, 2, 37, 39, 16, 50, 47, 59, 57, 77, 72, 97, 91, 86, 123, 99, 84, 63]
bfs = [63, 57, 84, 47, 59, 72, 99, 16, 50, 77, 86, 123, 2, 39, 91, 12, 37, 97]

print('in-order correct', ino == b.in_order())
print('pre-order correct', pre == b.pre_order())
print('post-order correct', pos == b.post_order())
print('breadth first correct', bfs == b.breadth_first())

# check that it returns proper value
print('largest smaller than correct', b.largest_smaller_than_x(76) == 72)

# check that it returns proper value
print('smallest larger than correct', b.smallest_larger_than_x(43) == 47)

# END TIME: 3:57 PM
