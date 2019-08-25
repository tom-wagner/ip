# START TIME: 2:40pm

from collections import deque


class Node:
    def __init__(self, item):
        self.val, self.left, self.right = item, None, None


class BST:
    def __init__(self, array):
        self.tree = None
        self.init(array)

    def init(self, array):
        for x in array:
            self.add(x)

    def add(self, item, should_add: bool = True, should_return_branch: bool = False):
        if not self.tree:
            self.tree = Node(item)
            return

        curr, branch = self.tree, []

        while curr:
            branch.append(curr.val)
            if item < curr.val:
                if not curr.left:
                    if should_add:
                        curr.left = Node(item)
                    return branch if should_return_branch else None
                curr = curr.left
            elif item > curr.val:
                if not curr.right:
                    if should_add:
                        curr.right = Node(item)
                    return branch if should_return_branch else None
                curr = curr.right
            else:
                raise Exception

    def find_location_and_return_branch(self, item):
        """wrapper around add to specifically return the branch without adding"""
        return self.add(item, should_add=False, should_return_branch=True)

    def largest_smaller_than_x(self, x):
        branch = self.find_location_and_return_branch(x)
        return max([val for val in branch if val < x])

    def smallest_larger_than_x(self, x):
        branch = self.find_location_and_return_branch(x)
        return min([val for val in branch if val > x])

    def depth_first(self, traversal_type: str = 'IN_ORDER'):
        res = []

        def recurse(tree):
            nonlocal res
            if traversal_type == 'PRE_ORDER':
                res.append(tree.val)
            if tree.left:
                recurse(tree.left)
            if traversal_type == 'IN_ORDER':
                res.append(tree.val)
            if tree.right:
                recurse(tree.right)
            if traversal_type == 'POST_ORDER':
                res.append(tree.val)

        recurse(self.tree)
        return res

    def in_order(self):
        return self.depth_first(traversal_type='IN_ORDER')

    def pre_order(self):
        return self.depth_first(traversal_type='PRE_ORDER')

    def post_order(self):
        return self.depth_first(traversal_type='POST_ORDER')

    def breadth_first(self):
        res = []
        q = deque([self.tree])

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

# END TIME: 2:57pm
