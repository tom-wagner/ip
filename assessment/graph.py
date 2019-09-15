import collections

# START TIME: 9:43pm


class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    @property
    def size(self):
        return len(self.vertices)

    def add_vertex(self, v):
        self.vertices.add(v)
        self.edges[v] = set()

    def remove_vertex(self, v):
        edges = self.edges[v]

        for e in edges:
            self.edges[e].remove(v)

        del self.edges[v]
        self.vertices.remove(v)

    def add_edge(self, f, t):
        self.edges[f].add(t)
        self.edges[t].add(f)

    def contains(self, val):
        return val in self.vertices

    def get_neighbors(self, val):
        return self.edges[val]

    def common_neighbors(self, val_one, val_two):
        return self.edges[val_one] & self.edges[val_two] - {val_one, val_two}

    def unique_neighbors(self, val_one, val_two):
        return (self.edges[val_one] ^ self.edges[val_two]) - {val_one, val_two}

    def shortest_path(self, val_one, val_two):
        already_visited = set()
        # (value, current_path
        q = collections.deque([(val_one, [val_one])])

        while q:
            val, curr_path = q.popleft()
            already_visited.add(val)
            if val == val_two:
                return curr_path
            for edge in self.edges[val]:
                if edge not in already_visited:
                    q.append((edge, curr_path + [edge]))

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

# END TIME: 10:03pm
