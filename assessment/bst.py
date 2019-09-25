import collections

# START TIME: 7:54am


class Node:
    def __init__(self, x):
        self.v = x
        self.l = None
        self.r = None


class BST:
    def __init__(self, array):
        self.tree = None
        self.init(array)

    def init(self, array):
        for x in array:
            self.add(x)

    def add(self, item, should_add=True, should_return_branch=False):
        if not self.tree:
            self.tree = Node(item)
            return

        branch = []
        new_node = Node(item)
        curr = self.tree
        while curr:
            branch.append(curr)
            if item < curr.v:
                if curr.l:
                    curr = curr.l
                    continue
                else:
                    if should_add:
                        curr.l = new_node
                    if should_return_branch:
                        return branch
                    return
            if item > curr.v:
                if curr.r:
                    curr = curr.r
                    continue
                else:
                    if should_add:
                        curr.r = new_node
                    if should_return_branch:
                        return branch
                    return
            if item == curr.v:
                raise Exception(f'Duplicate value {item}')

    def get_branch(self, x):
        return self.add(x, should_add=False, should_return_branch=True)

    def largest_smaller_than_x(self, x):
        branch = self.get_branch(x)
        return max([node.v for node in branch if node.v < x])

    def smallest_larger_than_x(self, x):
        branch = self.get_branch(x)
        return min([node.v for node in branch if node.v > x])

    def depth_first_traversal(self, traversal_type):
        res = []

        def recurse(tree):
            if traversal_type == 'PRE':
                res.append(tree.v)

            if tree.l:
                recurse(tree.l)

            if traversal_type == 'IN':
                res.append(tree.v)

            if tree.r:
                recurse(tree.r)

            if traversal_type == 'POST':
                res.append(tree.v)

        recurse(self.tree)
        return res

    def in_order(self):
        return self.depth_first_traversal('IN')

    def pre_order(self):
        return self.depth_first_traversal('PRE')

    def post_order(self):
        return self.depth_first_traversal('POST')

    def breadth_first(self):
        res = []
        q = collections.deque([self.tree])

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

# END TIME: 8:16am
