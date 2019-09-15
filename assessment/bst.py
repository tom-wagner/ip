# START TIME: 9:27pm

from collections import deque


class Node:
    def __init__(self, val):
        self.v = val
        self.l = None
        self.r = None


class BST:
    def __init__(self, array):
        self.bst = None
        self.init_bst(array)

    def init_bst(self, array):
        for v in array:
            self.add(v)

    def add(self, item):
        if not self.bst:
            self.bst = Node(item)
            return

        curr = self.bst
        while True:
            if item == curr.v:
                raise Exception
            if item < curr.v:
                if not curr.l:
                    curr.l = Node(item)
                    return
                curr = curr.l
            if item > curr.v:
                if not curr.r:
                    curr.r = Node(item)
                    return
                curr = curr.r

    def largest_smaller_than_x(self, y):
        return max([x for x in self.breadth_first() if x < y])

    def smallest_larger_than_x(self, y):
        return min([x for x in self.breadth_first() if x > y])

    def depth_first(self, traversal_type):
        res = []

        def recurse(bst):
            if not bst:
                return
            if traversal_type == 'PRE':
                res.append(bst.v)
            recurse(bst.l)
            if traversal_type == 'IN':
                res.append(bst.v)
            recurse(bst.r)
            if traversal_type == 'POST':
                res.append(bst.v)

        recurse(self.bst)
        return res

    def in_order(self):
        return self.depth_first('IN')

    def pre_order(self):
        return self.depth_first('PRE')

    def post_order(self):
        return self.depth_first('POST')

    def breadth_first(self):
        res = []
        q = deque([self.bst])

        while q:
            curr = q.popleft()
            res.append(curr.v)
            if curr.l:
                q.append(curr.l)
            if curr.r:
                q.append(curr.r)

        return res


arr = [63, 84, 57, 47, 50, 99, 59, 16, 39, 86, 2, 91, 12, 97]

b = BST(arr)

b.add(37)
b.add(123)
b.add(72)
b.add(87)

try:
    b.add(63)  # should be rejected
    print('ERROR -- should not get here')
except Exception:
    print('properly rejected 63')


ino = [2, 12, 16, 37, 39, 47, 50, 57, 59, 63, 72, 84, 86, 87, 91, 97, 99, 123]
pre = [63, 57, 47, 16, 2, 12, 39, 37, 50, 59, 84, 72, 99, 86, 91, 87, 97, 123]
pos = [12, 2, 37, 39, 16, 50, 47, 59, 57, 72, 87, 97, 91, 86, 123, 99, 84, 63]
bfs = [63, 57, 84, 47, 59, 72, 99, 16, 50, 86, 123, 2, 39, 91, 12, 37, 87, 97]

print('in-order correct', ino == b.in_order())
print('pre-order correct', pre == b.pre_order())
print('post-order correct', pos == b.post_order())
print('breadth first correct', bfs == b.breadth_first())

# check that it returns proper value
print('largest smaller than correct', b.largest_smaller_than_x(77) == 72)

# check that it returns proper value
print('smallest larger than correct', b.smallest_larger_than_x(43) == 47)

# END TIME: 9:38am
