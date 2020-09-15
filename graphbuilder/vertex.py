#Date: 12/08/2019
#Class: CS5310
#Assignment: Network Flow
#Author(s): Mohammad Jaminur Islam
from collections import defaultdict


class Vertex:

    def __init__(self,label,weight = 0):
        self.label = label
        self.weight = weight
        self.adjacentList = [] #to keep the neighbour node
        self.type = None
        self.edgeList = []



    def exist_in_adjacency_list(self,vertex,type):#check if the vertex is already in the adjacency list
        flag = False
        for adjacentNode in self.adjacentList:
            if(isinstance(adjacentNode,Adjacency)): #check if it is type  of adjacent listn
                # print("adjacent node label: ",adjacentNode.vertex.label," incidentType: ",adjacentNode.incidentType," assigned type: ",type)
                if(adjacentNode.vertex.label == vertex.label and adjacentNode.incidentType == type):
                    flag = True
                    break
        return flag

    def add_adjacent(self,vertex,type = 0): #adding one adjacent vertex
        if(isinstance(vertex,Vertex)):
            if not self.exist_in_adjacency_list(vertex,type):#check if it is already in the adjacent list
                    adjacentNode = Adjacency(vertex,type)
                    self.adjacentList.append(adjacentNode)

    # def add_adjacent_list(self,adjacent_list): a list of vertex need to add

class Adjacency:
    def __init__(self,vertex,incidentType=0):# keep track of the incident type of the edges
        self.vertex = vertex
        self.incidentType = incidentType