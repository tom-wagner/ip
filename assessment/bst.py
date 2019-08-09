from collections import deque

# START TIME: 7:16am


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, array):
        self.tree = None
        self.init(array)

    def init(self, array):
        for val in array:
            self.add(val)

    def add(self, item, should_add_to_tree: bool = True, should_return_branch: bool = False):
        if not self.tree:
            self.tree = Node(item)
            return
        branch = []
        curr = self.tree
        while curr:
            curr_val, left, right = curr.val, curr.left, curr.right
            branch.append(curr_val)
            if item < curr_val:
                if not curr.left:
                    if should_add_to_tree:
                        curr.left = Node(item)
                    return branch if should_return_branch else None
                curr = left
            elif item > curr_val:
                if not curr.right:
                    if should_add_to_tree:
                        curr.right = Node(item)
                    return branch if should_return_branch else None
                curr = right
            else:
                raise Exception

    def largest_smaller_than_x(self, x):
        branch = self.add(x, should_return_branch=True)
        return max([val for val in branch if val < x])

    def smallest_larger_than_x(self, x):
        branch = self.add(x, should_return_branch=True)
        return min([val for val in branch if val > x])

    def depth_first_traversal(self, traversal_type):
        res = []

        def recurse(tree):
            if not tree:
                return

            if traversal_type == 'PRE_ORDER':
                res.append(tree.val)

            recurse(tree.left)

            if traversal_type == 'IN_ORDER':
                res.append(tree.val)

            recurse(tree.right)

            if traversal_type == 'POST_ORDER':
                res.append(tree.val)

        recurse(self.tree)
        return res

    def in_order(self):
        return self.depth_first_traversal('IN_ORDER')

    def pre_order(self):
        return self.depth_first_traversal('PRE_ORDER')

    def post_order(self):
        return self.depth_first_traversal('POST_ORDER')

    def breadth_first(self):
        q = deque([self.tree])
        res = []

        while q:
            curr = q.popleft()
            val, left, right = curr.val, curr.left, curr.right
            res.append(val)
            if left:
                q.append(left)
            if right:
                q.append(right)

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

# END TIME: 7:37am
