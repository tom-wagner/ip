from collections import deque

# START TIME: 8:09am


class Tree:
    def __init__(self, tree):
        self.tree = tree

    def breadth_first_traversal(self):
        res = []
        q = deque([self.tree])

        while q:
            curr = q.popleft()
            res.append(curr['v'])
            for child_node in curr['children']:
                q.append(child_node)

        return res

    def depth_first_traversal(self):
        res = []

        def recurse(tree):
            for child_node in tree['children']:
                recurse(child_node)
            res.append(tree['v'])

        recurse(self.tree)
        print(res)
        return res

    def has(self, item):
        def search(tree, looking_for):
            print(tree, looking_for)
            if looking_for == tree['v']:
                return True

            for node in tree['children']:
                if search(node, looking_for):
                    return True

            return False

        return search(self.tree, item)


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

my_tree = Tree(t)

depth_first = [0, 8, 1, 6, 9, 7, 0, 4, 1, 5]

breadth_first = [5, 9, 1, 8, 6, 4, 0, 1, 7, 0]

print('DFS', my_tree.depth_first_traversal() == depth_first)
print('BFS', my_tree.breadth_first_traversal() == breadth_first)
print('has returns true correctly', my_tree.has(7))
print('has returns true correctly', my_tree.has(8))
print('has returns false correctly', my_tree.has('BILL') is False)

# END TIME: 8:20am
