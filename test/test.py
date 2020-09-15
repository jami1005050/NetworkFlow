#Date: 12/08/2019
#Class: CS5310
#Assignment: Network Flow
#Author(s): Mohammad Jaminur Islam

import unittest

from graphbuilder.constant import DIRECTED_GRAPH
from graphbuilder.graph import Graph
from graphbuilder.vertex import Vertex
from networkflow.NetworkFlow import FlowNetwork


class MyTestCase(unittest.TestCase):
    def test_network_flow(self): #test network flow
        netwrok = FlowNetwork() #test network flow object
        self.assertIsInstance(netwrok, FlowNetwork)

    def test_directed_graph(self): #test directed graph
        graph2 = Graph(DIRECTED_GRAPH)  # directed graph
        vertex1 = Vertex(1)  # source
        vertex1.type = 's'
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)
        vertex4 = Vertex(4)
        vertex5 = Vertex(5)
        vertex6 = Vertex(6)  # destination
        vertex6.type = 't'
        graph2.insert_vertex(vertex1)  # source insert
        graph2.insert_vertex(vertex2)
        graph2.insert_vertex(vertex3)
        graph2.insert_vertex(vertex4)
        graph2.insert_vertex(vertex5)
        graph2.insert_vertex(vertex6)  # destination insert
        graph2.insert_edge_by_ends(vertex1, vertex2, 10)  # soruce to other node 2
        graph2.insert_edge_by_ends(vertex1, vertex3, 8)  # source to other node 3
        graph2.insert_edge_by_ends(vertex2, vertex3, 2)
        graph2.insert_edge_by_ends(vertex2, vertex4, 5)
        graph2.insert_edge_by_ends(vertex3, vertex5, 10)
        graph2.insert_edge_by_ends(vertex5, vertex4, 8)
        graph2.insert_edge_by_ends(vertex5, vertex6, 10)  # other node 5 to sink
        graph2.insert_edge_by_ends(vertex4, vertex6, 7)  # other node 4 to sink
        assert len(graph2.edgeList) == 8
        graph2.print_all_edge()
        self.graph = graph2

    def test_MaxFlow(self):
        networkFLow = FlowNetwork()
        graphNew = Graph(DIRECTED_GRAPH)  # directed graph
        assert isinstance(graphNew,Graph)
        vertex1 = Vertex(1)  # source
        assert isinstance(vertex1,Vertex)
        vertex1.type = 's'
        vertex2 = Vertex(2)
        vertex3 = Vertex(3)
        vertex4 = Vertex(4)
        vertex5 = Vertex(5)
        vertex6 = Vertex(6)
        vertex7 = Vertex(7)
        vertex8 = Vertex(8)  # destination
        vertex8.type = 't'
        graphNew.insert_vertex(vertex1)  # source insert
        graphNew.insert_vertex(vertex2)
        graphNew.insert_vertex(vertex3)
        graphNew.insert_vertex(vertex4)
        graphNew.insert_vertex(vertex5)
        graphNew.insert_vertex(vertex6)
        graphNew.insert_vertex(vertex7)
        graphNew.insert_vertex(vertex8)
        graphNew.insert_edge_by_ends(vertex1, vertex2, 10)  # soruce to other node 2
        graphNew.insert_edge_by_ends(vertex1, vertex3, 5)  # source to other node 3
        graphNew.insert_edge_by_ends(vertex1, vertex4, 15)  # source to other node 4
        graphNew.insert_edge_by_ends(vertex2, vertex3, 4)
        graphNew.insert_edge_by_ends(vertex2, vertex5, 9)
        graphNew.insert_edge_by_ends(vertex2, vertex6, 15)
        graphNew.insert_edge_by_ends(vertex3, vertex4, 4)
        graphNew.insert_edge_by_ends(vertex3, vertex6, 8)
        graphNew.insert_edge_by_ends(vertex4, vertex7, 30)
        graphNew.insert_edge_by_ends(vertex5, vertex6, 15)
        graphNew.insert_edge_by_ends(vertex5, vertex8, 10)  # other node 5 to sink
        graphNew.insert_edge_by_ends(vertex6, vertex8, 15)  # other node 6 to sink
        graphNew.insert_edge_by_ends(vertex6, vertex7, 10)
        graphNew.insert_edge_by_ends(vertex7, vertex3, 6)
        graphNew.insert_edge_by_ends(vertex7, vertex8, 10)  # other node 7 to sink
        networkFLow.form_Simplex(graphNew)
        value = networkFLow.calculateMaxFlow(graphNew)
        assert value is not 0

if __name__ == '__main__':
    unittest.main()
