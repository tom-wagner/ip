# START TIME:


class Graph:
    def __init__(self):
        pass

    def add_vertex(self):
        pass

    def add_edge(self):
        pass

    def contains(self):
        pass

    def get_neighbors(self):
        pass

    def common_neighbors(self):
        pass

    def shortest_path(self):
        pass

    @property
    def size(self):
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

print('g contains 1', g.contains(1))
print('g does not contain 7', not g.contains(7))
print('1 neighbors 2 and 4 and 5', g.get_neighbors(1) == {2, 4, 5})
print('1 has 2 and 4 as common neighbors with 3', g.common_neighbors(1, 3))
print('path from 5 to 3 should go through 1 -> 4 or 1 -> 2', g.shortest_path(5, 3) == [5, 1, 4, 3] or [5, 1, 2, 3])

# END TIME:
