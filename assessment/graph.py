import collections

# START TIME: 8:16am


class Graph:
    def __init__(self):
        pass

    @property
    def size(self):
        return ''

    def add_vertex(self, v):
        pass

    def remove_vertex(self, v):
        pass

    def add_edge(self, f, t):
        pass

    def contains(self, val):
        pass

    def get_neighbors(self, val):
        pass

    def common_neighbors(self, val_one, val_two):
        pass

    def unique_neighbors(self, val_one, val_two):
        pass

    def shortest_path(self, val_one, val_two):
        pass


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

# END TIME:
