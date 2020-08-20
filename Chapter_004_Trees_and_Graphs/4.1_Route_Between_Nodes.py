__author__ = 'Sam Kasbawala'
__credits__ = 'Sam Kasbawala'


import unittest
from mygraph import Vertex, Graph
from myqueue import Queue


class Graph(Graph):
    def is_path(self, u, v):
        """Use BFS in order to see if there is a path between two vertices"""
        seen = set()
        seen.add(u)
        queue = Queue()
        queue.enqueue(u)

        while not queue.isEmpty():
            vertex = queue.dequeue()
            for neighbor in vertex.neighbors:
                if neighbor == v:
                    return True
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.enqueue(neighbor)

        return False


class TestGraph(unittest.TestCase):
    def test_is_path(self):
        vertex_a = Vertex('a')
        vertex_b = Vertex('b')
        vertex_c = Vertex('c')

        graph = Graph()
        graph.add_edge(vertex_a, vertex_b)
        graph.add_edge(vertex_b, vertex_c)

        self.assertTrue(graph.is_path(vertex_a, vertex_b))
        self.assertTrue(graph.is_path(vertex_b, vertex_c))
        self.assertTrue(graph.is_path(vertex_a, vertex_c))

        self.assertFalse(graph.is_path(vertex_c, vertex_a))
        self.assertFalse(graph.is_path(vertex_c, vertex_b))

        graph.add_edge(vertex_c, vertex_b)
        graph.add_edge(vertex_c, vertex_a)
        self.assertTrue(graph.is_path(vertex_c, vertex_a))
        self.assertTrue(graph.is_path(vertex_c, vertex_b))


if __name__ == '__main__':
    unittest.main()
