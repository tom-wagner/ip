from collections import deque

# START TIME: 1:37pm


class Tree:
    def __init__(self, tree):
        self.tree = tree

    def breadth_first_traversal(self):
        q = deque([self.tree])
        res = []

        while q:
            curr = q.popleft()
            res.append(curr['v'])
            for child in curr['children']:
                q.append(child)

        return res

    # BROKEN TEST
    def depth_first_traversal(self):
        res = []

        def recurse(tree):
            for child in tree['children']:
                recurse(child)

            res.append(tree['v'])

        recurse(self.tree)
        return res

    def has(self, x):
        return x in set(self.breadth_first_traversal())


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

depth_first = [0, 8, 1, 6, 9, 5, 7, 0, 4, 1]

breadth_first = [5, 9, 1, 8, 6, 4, 0, 1, 7, 0]

print('DFS', my_tree.depth_first_traversal() == depth_first)
print('BFS', my_tree.breadth_first_traversal() == breadth_first)
print('has returns true correctly', my_tree.has(7))
print('has returns true correctly', my_tree.has(8))
print('has returns false correctly', my_tree.has('BILL'))

# END TIME:
