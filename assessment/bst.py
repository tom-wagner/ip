from collections import deque

# START TIME: 9:00pm


class Node:
    def __init__(self, x):
        self.v = x
        self.left = self.right = None


class BST:
    def __init__(self, array):
        self.bst = Node(array[0])

        for val in array[1:]:
            self.add(val)

    def add(self, item):
        curr = self.bst
        while True:
            if item < curr.v:
                if not curr.left:
                    curr.left = Node(item)
                    return
                curr = curr.left
            if item > curr.v:
                if not curr.right:
                    curr.right = Node(item)
                    return
                curr = curr.right
            if item == curr.v:
                raise Exception

    def largest_smaller_than_x(self, x):
        # SKIPPED --> have down cold
        pass

    def smallest_larger_than_x(self, x):
        # SKIPPED --> have down cold
        pass

    def depth_first(self, traversal_type='IN_ORDER'):
        res = []

        def recurse(bst):
            if traversal_type == 'PRE_ORDER':
                res.append(bst.v)

            if bst.left:
                recurse(bst.left)

            if traversal_type == 'IN_ORDER':
                res.append(bst.v)

            if bst.right:
                recurse(bst.right)

            if traversal_type == 'POST_ORDER':
                res.append(bst.v)

        recurse(self.bst)
        return res

    def in_order(self):
        return self.depth_first()

    def pre_order(self):
        return self.depth_first('PRE_ORDER')

    def post_order(self):
        return self.depth_first('POST_ORDER')

    def breadth_first(self):
        q = deque([self.bst])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr.v)
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

# END TIME: 9:14pm
