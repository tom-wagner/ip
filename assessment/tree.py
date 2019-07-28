# START TIME: 4:19pm

from collections import deque


class Tree:
    def __init__(self, tree):
        self.tree = tree

    def breadth_first_traversal(self):
        res = []

        q = deque()
        q.append(self.tree)

        while q:
            curr = q.popleft()
            res.append(curr['v'])
            for child in curr['children']:
                q.append(child)

        return res

    def depth_first_traversal(self):
        res = []

        def recurse(tree):
            nonlocal res
            res.append(tree['v'])

            for child in tree['children']:
                recurse(child)

        recurse(self.tree)
        return res

    def has(self, x):
        def recurse(tree):
            if tree['v'] == x:
                return True
            for child in tree['children']:
                if recurse(child):
                    return True
            return False

        return recurse(self.tree)


t = {
    'v': 5,
    'children': [
        {'v': 9,
         'children': [
             {'v': 8,
              'children': [
                    {'v': 0,
                     'children': []}
              ]},
             {'v': 6,
              'children': [
                  {'v': 1,
                   'children': []}
              ]}
         ]},
        {'v': 1,
         'children': [
             {'v': 4,
              'children': [
                  {'v': 7,
                   'children': []},
                  {'v': 0,
                   'children': []}
              ]}
         ]}
    ]
}

# TREE:

#         5
#     9         1
#  8    6          4
#  0    1        7   0

print(t)

my_tree = Tree(t)

depth_first_pre = [5, 9, 8, 0, 6, 1, 1, 4, 7, 0]

breadth_first = [5, 9, 1, 8, 6, 4, 0, 1, 7, 0]

print('DFS', my_tree.depth_first_traversal() == depth_first_pre)
print('BFS', my_tree.breadth_first_traversal() == breadth_first)
print('has returns true correctly', my_tree.has(7))
print('has returns true correctly', my_tree.has(8))
print('has returns false correctly', my_tree.has('BILL') is False)

# END TIME: 4:28pm
