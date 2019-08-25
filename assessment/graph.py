import collections

# START TIME: 3:40pm


class Graph:
    def __init__(self):
        self.v = set()
        self.e = {}

    @property
    def size(self):
        return len(self.v)

    def add_vertex(self, v):
        self.v.add(v)
        self.e[v] = set()

    def remove_vertex(self, v):
        neighbors = self.e[v]
        for neighbor in neighbors:
            self.e[neighbor].remove(v)

        self.v.remove(v)
        del self.e[v]

    def add_edge(self, f, t):
        self.e[f].add(t)
        self.e[t].add(f)

    def contains(self, val):
        return val in self.v

    def get_neighbors(self, val):
        return self.e[val]

    def common_neighbors(self, val_one, val_two):
        return (self.e[val_one] & self.e[val_two]) - {val_one, val_two}

    def unique_neighbors(self, val_one, val_two):
        return (self.e[val_one] ^ self.e[val_two]) - {val_one, val_two}

    def shortest_path(self, val_one, val_two):
        q = collections.deque([dict(v=val_one, path=[val_one], already_visited=set())])

        while q:
            curr = q.popleft()
            path = curr['path']
            already_visited = curr['already_visited']
            val = curr['v']

            if val == val_two:
                return path

            already_visited.add(val)
            for edge in self.e[curr['v']]:
                if edge not in already_visited:
                    q.append(dict(v=edge, already_visited=already_visited, path=path + [edge]))

        return 'No path'


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(1, 5)

print('g.size == 5', g.size == 5)
print('g contains 1', g.contains(1))
print('g does not contain 7', not g.contains(7))
print('1 neighbors 2 and 4 and 5', g.get_neighbors(1) == {2, 4, 5})
print('1 has 2 and 4 as common neighbors with 3', g.common_neighbors(1, 3) == {2, 4})
print('path from 5 to 3 should go through 1 -> 4 or 1 -> 2', g.shortest_path(5, 3) == [5, 1, 4, 3] or g.shortest_path(5, 3) == [5, 1, 2, 3])
print('unique neighbors of 1 and 4 is {5, 2, 3}', g.unique_neighbors(1, 4) == {5, 2, 3})

g.remove_vertex(3)

print('3 no longer neighbor of 2', g.get_neighbors(2) == {1})
print('3 no longer neighbor of 1', g.get_neighbors(4) == {1})
print('no path anymore', g.shortest_path(5, 3) == 'No path')

# END TIME: 4:00pm
