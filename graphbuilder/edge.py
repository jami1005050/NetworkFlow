#Date: 12/08/2019
#Class: CS5310
#Assignment: Network Flow
#Author(s): Mohammad Jaminur Islam

from graphbuilder.constant import BI_DIRECTIONAL_EDGE, OUT_GOING_EDGE, INCOMING_EDGE


from graphbuilder.vertex import Vertex


class Edge:

    def __init__(self, start = None, end = None, weight=0, type = 0, IN_COMING_EDGE=None):
        if not(start==None): #with initialization adjusting the adjacency list for that node
            if not end == None:
                self.startNode = start
                self.endNode = end
                self.weight = weight
                self.type = type
                self.flow = 0
                self.returnEdge = None

                if(type == 0):
                    if(isinstance(start,Vertex)):
                        self.startNode.add_adjacent(self.endNode,BI_DIRECTIONAL_EDGE)
                        self.endNode.add_adjacent(self.startNode,BI_DIRECTIONAL_EDGE)
                else:
                    if(isinstance(start,Vertex)):
                        self.startNode.add_adjacent(self.endNode,OUT_GOING_EDGE)
                        self.endNode.add_adjacent(self.startNode,INCOMING_EDGE)

        else:
            self.startNode = start
            self.endNode = end
            self.weight = weight
            self.type = type #directed or undirected
            self.flow = 0
            self.returnEdge = None
