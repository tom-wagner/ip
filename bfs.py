import random
from collections import deque
import binarytree


def bfs(tree, val):
    """return True if the value is found in the tree. utilizes a breadth-first search using a queue"""
    q = deque()
    q.append(tree)

    while q:
        curr = q.popleft()
        if curr['v'] == val:
            return True
        for child_tree in curr['children']:
            q.append(child_tree)

    return False


def random_tree(max_children, max_depth):
    if max_depth == 0:
        return {'v': random.randint(0, 10), 'children': []}
    children = [random_tree(max_children, max_depth - 1) for _ in list(range(random.randint(1, max_children)))]
    return {'v': random.randint(0, 10), 'children': children}


rt = random_tree(2, 3)
randint = random.randint(0, 10)

print(rt)
print(randint)
print(bfs(rt, randint))
