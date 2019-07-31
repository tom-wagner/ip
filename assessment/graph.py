import collections

# START TIME: 7pm


class Vertex:
    def __init__(self, val):
        self.val = val
        self.edges = set()


class Graph:
    def __init__(self):
        self.vertices = {}

    @property
    def size(self):
        return len(self.vertices)

    def add_vertex(self, v):
        self.vertices[v] = Vertex(v)

    def remove_vertex(self, v):
        for edge in self.get_neighbors(v):
            self.vertices[edge].edges.remove(v)
        del self.vertices[v]

    def add_edge(self, f, t):
        self.vertices[f].edges.add(t)
        self.vertices[t].edges.add(f)

    def contains(self, val):
        return val in self.vertices

    def get_neighbors(self, val):
        return self.vertices[val].edges

    def common_neighbors(self, val_one, val_two):
        return self.vertices[val_one].edges & self.vertices[val_two].edges

    def unique_neighbors(self, val_one, val_two):
        val_one_neighbors, val_two_neighbors = (self.vertices[v].edges for v in (val_one, val_two))
        return (val_one_neighbors ^ val_two_neighbors) - {val_one, val_two}

    def shortest_path(self, val_one, val_two):
        already_visited = {val_one}
        q = collections.deque([dict(v=self.vertices[val_one], path=[])])
        while q:
            curr = q.popleft()
            curr_val, curr_edges, curr_path = curr['v'].val, curr['v'].edges, curr['path']
            if curr_val == val_two:
                res = curr_path + [val_two]
                return res

            already_visited.add(curr_val)

            for v in curr_edges:
                if v not in already_visited:
                    q.append(dict(v=self.vertices[v], path=curr_path + [curr_val]))

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

# END TIME: 7:56pm
