from collections import deque

# START TIME: 5:08PM


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, arr):
        self.tree = None
        self.init_bst(arr)

    def init_bst(self, arr):
        for x in arr:
            self.find_location_for_item_and_invoke_func(x, self.add)

    @staticmethod
    def add(item, current_node, _):
            if item < current_node.val:
                current_node.left = Node(item)
            if item > current_node.val:
                current_node.right = Node(item)

    def find_location_for_item_and_invoke_func(self, item, func):
        if not self.tree:
            self.tree = Node(item)
            return

        curr = self.tree
        branch = []
        while True:
            if item < curr.val:
                branch.append(curr)
                if not curr.left:
                    return func(item, curr, branch)
                curr = curr.left
            elif item > curr.val:
                branch.append(curr)
                if not curr.right:
                    return func(item, curr, branch)
                curr = curr.right
            else:
                raise Exception('No duplicate values!')

    @staticmethod
    def largest_smaller_than_helper(item, _, branch):
        differences = [item - node.val for node in branch if item - node.val > 0]
        return item - min(differences) if len(differences) > 0 else f'All nodes larger than {item}'

    def largest_smaller_than_x(self, x):
        return self.find_location_for_item_and_invoke_func(x, self.largest_smaller_than_helper)

    @staticmethod
    def smallest_larger_than_helper(item, _, branch):
        differences = [node.val - item for node in branch if node.val - item > 0]
        return min(differences) + item if len(differences) > 0 else f'All nodes larger than {item}'

    def smallest_larger_than_x(self, x):
        return self.find_location_for_item_and_invoke_func(x, self.smallest_larger_than_helper)

    def depth_first(self, type: str):
        res = []

        def recurse(tree):
            if type == 'PRE_ORDER':
                res.append(tree.val)

            if tree.left:
                recurse(tree.left)

            if type == 'IN_ORDER':
                res.append(tree.val)

            if tree.right:
                recurse(tree.right)

            if type == 'POST_ORDER':
                res.append(tree.val)

        recurse(self.tree)
        return res

    def in_order(self):
        return self.depth_first('IN_ORDER')

    def pre_order(self):
        return self.depth_first('PRE_ORDER')

    def post_order(self):
        return self.depth_first('POST_ORDER')

    def breadth_first(self):
        res = []

        q = deque()
        q.append(self.tree)
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

b.find_location_for_item_and_invoke_func(37, b.add)
b.find_location_for_item_and_invoke_func(123, b.add)
b.find_location_for_item_and_invoke_func(72, b.add)
b.find_location_for_item_and_invoke_func(87, b.add)

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

# END TIME: 7:57am
