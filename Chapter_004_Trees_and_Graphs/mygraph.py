__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


class Vertex():
    def __init__(self, value):
        self.value = value
        self.neighbors = set()

    def add_neighbor(self, vertex):
        self.neighbors.add(vertex)

    def del_neighbor(self, vertex):
        try:
            self.neighbors.remove(vertex)
        except KeyError:
            pass


class Graph():
    def __init__(self, directed=True):
        self.vertices = set()
        self.__directed = directed

    def add_edge(self, u, v):
        for i in [u, v]:
            self.add_vertex(i)

        u.add_neighbor(v)
        if not self.__directed:
            v.add_neighbor(u)

    def remove_edge(self, u, v):
        u.del_neighbor(v)
        if not self.__directed:
            v.del_neighbor(u)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        try:
            self.vertices.remove(vertex)
        except KeyError:
            pass
