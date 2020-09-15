#Date: 12/08/2019
#Class: CS5310
#Assignment: Network Flow
#Author(s): Mohammad Jaminur Islam


from graphbuilder.edge import Edge
from graphbuilder.vertex import Adjacency, Vertex
from graphbuilder.constant import BI_DIRECTIONAL_EDGE, INCOMING_EDGE, OUT_GOING_EDGE, DIRECTED_GRAPH, \
    UNDIRECTED_GRAPH


class Graph(object):

    def __init__(self,type): # type denote if the graph is directed = 1  or undirected = 0
        self.edgeList = []
        self.vertexList = []
        self.type = type
    #1
    def get_vertex_count(self): #return the number of vertices
        return len(self.vertexList)
    #2
    def get_edge_count(self):#return the number of edges
        return len(self.edgeList)
    #3
    def get_edge_list(self): #return all edges
        return self.edgeList
    #4
    def get_vertex_list(self):#return all vertices
        return self.vertexList
    #5
    def search_vertex_by_label(self,label): #if anyone wanted to search by vertex label only fine it is the process
        for vertex in self.vertexList:
            if vertex.label == label:
                return vertex
    #6
    def get_degree(self, label):  # get degree by vertex name
        vertex = self.search_vertex_by_label(label)
        degree = 0
        #outDegree = 0
        if not vertex == None:
            for adjacent in vertex.adjacentList:
                if (isinstance(adjacent, Adjacency)):
                    # if adjacent.incidentType == INCOMING_EDGE:
                    #     inDegree = inDegree + 1
                    # elif (adjacent.incidentType == OUT_GOING_EDGE):
                    #     outDegree = outDegree + 1
                    # else:
                    degree = degree + 1
                    #outDegree = outDegree + 1

        return degree
    #7
    def get_edges_on_node(self,vertex_label): #return all edges from vertex
        incidentList = [] #temp list
        # print("vertex:",vertex_label)
        for edge in self.edgeList: #check if any end vertex match with the vertex
            # print("start",edge.startNode.label," end",edge.endNode.label)
            if edge.startNode.label == vertex_label:
                incidentList.append(edge)
            elif edge.endNode.label == vertex_label:
                incidentList.append(edge)
        return incidentList
    #8
    def all_adjacent_to(self,vertex_label): #return all adjacent vertex
        vertex = self.search_vertex_by_label(vertex_label)
        adjacentVertexList = []
        for adjacent in vertex.adjacentList:
            adjacentVertexList.append(adjacent.vertex)
        return adjacentVertexList
    #9
    def get_end_nodes_of_edge(self,start,end): #return end vertices of an edge
        vertex1 = self.search_vertex_by_label(start)
        vertex2 = self.search_vertex_by_label(end)
        endNodesList = []
        endNodesList.append(vertex1)
        endNodesList.append(vertex2)
        return endNodesList
    #10
    def check_adjacency_of_nodes(self,node1,node2): #check if two vertices are adjacent
        vertex = self.search_vertex_by_label(node1)
        for adjacent in vertex.adjacentList:
            if(adjacent.vertex.label == node2):
                return True
        return False
    #11
    def check_directed(self,start,end): #check if a edge is directed or not
        vertex = self.search_vertex_by_label(start)
        for adjacent in vertex.adjacentList:
            # print("adjacent incident type: ",adjacent.incidentType)
            # print("adjacent vertex: ",adjacent.vertex.label)
            if (adjacent.vertex.label == end):
                if (adjacent.incidentType == BI_DIRECTIONAL_EDGE):
                    # print("return false")
                    return False
        return True

    #12
    def get_in_degree(self, label):  # get degree by vertex name
        vertex = self.search_vertex_by_label(label)
        inDegree = 0
        #outDegree = 0
        if not vertex == None:
            for adjacent in vertex.adjacentList:
                if (isinstance(adjacent, Adjacency)):
                    if adjacent.incidentType == INCOMING_EDGE:
                        inDegree = inDegree + 1
        return inDegree

    #13
    def get_out_degree(self, label):  # get degree by vertex name
        vertex = self.search_vertex_by_label(label)
        outDegree = 0
        if not vertex == None:
            for adjacent in vertex.adjacentList:
                if (isinstance(adjacent, Adjacency)):
                  if (adjacent.incidentType == OUT_GOING_EDGE):
                        outDegree = outDegree + 1
        return outDegree
    #14
    def get_edges_incoming(self,vertex_label): #get only incoming edges
        vertex = self.search_vertex_by_label(vertex_label)
        incomingEdgeList = []
        for adjacent in vertex.adjacentList:
            if adjacent.incidentType == INCOMING_EDGE:
                edge = self.search_edge_by_end_nodes(adjacent.vertex.label,vertex_label)
                # print("edge",edge)
                if not(edge == None):
                    incomingEdgeList.append(edge)
        return incomingEdgeList
    #15
    def get_edges_out_going(self, vertex_label):  #get only outgoing edges
        vertex = self.search_vertex_by_label(vertex_label)
        outcomingEdgeList = []
        for adjacent in vertex.adjacentList:
            if adjacent.incidentType == OUT_GOING_EDGE:
                edge = self.search_edge_by_end_nodes( vertex_label,adjacent.vertex.label)
                if not (edge == None):
                    outcomingEdgeList.append(edge)
        return outcomingEdgeList
    #16
    def get_vertices_form_incoming(self,vertex_label): #get vertices that form incoming edges
        vertex = self.search_vertex_by_label(vertex_label)
        incomingVertexList = []
        for adjacent in vertex.adjacentList:
            if adjacent.incidentType == INCOMING_EDGE:
                incomingVertexList.append(adjacent.vertex)
        return incomingVertexList
    #17
    def get_vertices_form_outgoing(self, vertex_label): #get eedges that forms outgoing edge
        vertex = self.search_vertex_by_label(vertex_label)
        outgoingVertexList = []
        for adjacent in vertex.adjacentList:
            if adjacent.incidentType == OUT_GOING_EDGE:
                outgoingVertexList.append(adjacent.vertex)
        return outgoingVertexList
    #18
    def insert_vertex(self,vertex): #insert a vertex
        if(isinstance(vertex,Vertex)):
            if not self.vertexList.__contains__(vertex):#check if the vertex is already in the list
                self.vertexList.append(vertex)
    #19
    def insert_edge_by_ends(self,startVertex,endVertex,edge_weight = 0): #insert edge
        self.insert_vertex(startVertex)
        self.insert_vertex(endVertex)
        if self.type == DIRECTED_GRAPH: #for directed graph add the vertices in their respective adjacency list
                startVertex.add_adjacent(endVertex,OUT_GOING_EDGE)
                endVertex.add_adjacent(startVertex,INCOMING_EDGE)
        else:
            startVertex.add_adjacent(endVertex,BI_DIRECTIONAL_EDGE)
            endVertex.add_adjacent(startVertex,BI_DIRECTIONAL_EDGE)


        edge = Edge(startVertex,endVertex,edge_weight,self.type) #define edge
        returnEdge = Edge(endVertex, startVertex,0,self.type)
        edge.returnEdge = returnEdge
        returnEdge.returnEdge = edge
        startVertex.edgeList.append(edge)
        endVertex.edgeList.append(returnEdge)
        if isinstance(edge,Edge):
            if not self.edgeList.__contains__(edge):#check if the edge is already in the list
                self.edgeList.append(edge)

    #19.1
    def insert_edge(self,edge): #insert edge
        if(isinstance(edge,Edge)):
            startVertex = edge.startNode
            endVertex = edge.endNode
            self.insert_vertex(startVertex)
            self.insert_vertex(endVertex)
            if self.type == DIRECTED_GRAPH: #for directed graph add the vertices in their respective adjacency list
                    startVertex.add_adjacent(endVertex,OUT_GOING_EDGE)
                    endVertex.add_adjacent(startVertex,INCOMING_EDGE)
            else:
                startVertex.add_adjacent(endVertex,BI_DIRECTIONAL_EDGE)
                endVertex.add_adjacent(startVertex,BI_DIRECTIONAL_EDGE)

            if not self.edgeList.__contains__(edge):#check if the edge is already in the list
                self.edgeList.append(edge)
    #20
    def search_edge(self,start_label,end_label):#start label and end label denoting the start and end of the edge
        for edge in self.edgeList:
            if edge.startNode.label == start_label and edge.endNode.label == end_label:
                return edge
    #21
    def remove_edge(self,start_label,end_label): #delete a edge
        edge = self.search_edge(start_label,end_label)
        self.edgeList.remove(edge)
        self.removeFromAdjacencyList(start_label,end_label)
    #21
    def remove_vertex(self,vertex_label): #delete a vertex
        vertex = self.search_vertex_by_label(vertex_label)
        self.vertexList.remove(vertex)
        for otherVertex in self.vertexList:
            for adjacent in otherVertex.adjacentList:
                tempAdj = []
                if not (adjacent.vertex.label == vertex_label):
                    tempAdj.append(adjacent)
            otherVertex.adjacentList = tempAdj

        # print("no of edge",self.get_edge_count())
        temp = [] #to keep the updated edge
        for edge in self.edgeList:
            # print("start label: ",edge.startNode.label)
            # print("end label: ",edge.endNode.label)
            if not (edge.endNode.label == vertex_label or edge.startNode.label == vertex_label ):
                temp.append(edge)
        self.edgeList = temp
    #22
    def removeFromAdjacencyList(self, start_label, end_label): #after edge delete we need to delete the vertex from adjacent list
        vertex1 = self.search_vertex_by_label(start_label)
        vertex2 =self.search_vertex_by_label(end_label)
        tempAdjVertex1 = []
        tempAdjVertex2 = []
        for adjacent in vertex1.adjacentList:
            if not (adjacent.vertex.label == end_label):
                tempAdjVertex1.append(adjacent)
        vertex1.adjacentList =tempAdjVertex1
        for adjacent in vertex2.adjacentList:
            if not (adjacent.vertex.label == start_label):
                tempAdjVertex2.append(adjacent)
        vertex2.adjacentList = tempAdjVertex2
    #23
    def print_all_vertex(self): #print all vertex
        for node in self.vertexList:
            print("Node: ",node.label)
    #24
    def print_all_edge(self): #print all edge
        for edge in self.edgeList:
            print("edge: ",edge.startNode.label," ",edge.endNode.label," weight: ",edge.weight)
    #25
    def search_edge_by_end_nodes(self, vertex_label, label): #search end nodes
        for edge in self.edgeList:
            # print("match",vertex_label," start",edge.startNode.label," match",label," end",edge.endNode.label,)
            if(edge.endNode.label == label and edge.startNode.label == vertex_label):
                # print("returnning")
                return edge
        return None


if __name__ == '__main__':
    graph1 = Graph(UNDIRECTED_GRAPH) #create an undirected edge
    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    vertex3 = Vertex(3)
    vertex4 = Vertex(4)
    vertex5 = Vertex(5)
    vertex6 = Vertex(6)
    graph1.insert_vertex(vertex1)
    graph1.insert_vertex(vertex2)
    graph1.insert_vertex(vertex3)
    graph1.insert_vertex(vertex4)
    graph1.insert_vertex(vertex5)
    graph1.insert_vertex(vertex6)
    graph1.insert_edge_by_ends(vertex1,vertex2)
    graph1.insert_edge_by_ends(vertex1,vertex3)
    graph1.insert_edge_by_ends(vertex1,vertex4)
    graph1.insert_edge_by_ends(vertex2,vertex4)
    graph1.insert_edge_by_ends(vertex3,vertex5)
    graph1.insert_edge_by_ends(vertex4,vertex6)
    graph1.insert_edge_by_ends(vertex5,vertex6)
    graph1.get_degree(4)
    print('vertex count: ',graph1.get_vertex_count())
    print('edge count: ',graph1.get_edge_count())
    graph1.remove_edge(1,4)
    print("*****After edge remove*****")
    graph1.get_degree(4)
    print('vertex count after edge delete: ', graph1.get_vertex_count())
    print('edge count after edge delete: ', graph1.get_edge_count())
    print("****after vertex remove****")
    graph1.remove_vertex(1)
    print('vertex count after edge delete: ', graph1.get_vertex_count())
    print('edge count after edge delete: ', graph1.get_edge_count())

    graph1.print_all_edge()
    print("******Directed graph******")
    graph2 = Graph(DIRECTED_GRAPH) #directed graph
    vertex1 = Vertex(1,1)
    vertex2 = Vertex(2,2)
    vertex3 = Vertex(3,3)
    vertex4 = Vertex(4,4)
    vertex5 = Vertex(5,5)
    vertex6 = Vertex(6,6)
    vertex7 = Vertex(7,7)

    graph2.insert_vertex(vertex1)
    graph2.insert_vertex(vertex2)
    graph2.insert_vertex(vertex3)
    graph2.insert_vertex(vertex4)
    graph2.insert_vertex(vertex5)
    graph2.insert_vertex(vertex6)
    graph2.insert_edge_by_ends(vertex1, vertex2)
    graph2.insert_edge_by_ends(vertex1, vertex3)
    graph2.insert_edge_by_ends(vertex2, vertex7)
    graph2.insert_edge_by_ends(vertex3, vertex2)
    graph2.insert_edge_by_ends(vertex4, vertex3)
    graph2.insert_edge_by_ends(vertex4, vertex1)
    graph2.insert_edge_by_ends(vertex4, vertex5)
    graph2.insert_edge_by_ends(vertex5, vertex1)
    graph2.insert_edge_by_ends(vertex5, vertex6)
    graph2.insert_edge_by_ends(vertex6, vertex1)
    graph2.insert_edge_by_ends(vertex6, vertex7)
    graph2.insert_edge_by_ends(vertex7, vertex1)
    indegree = graph2.get_in_degree(1) #indegree check
    outdegree = graph2.get_out_degree(1) #outdegree check

    # for node in graph2.vertexList:
    #     for adjacent in node.adjacentList:
    #         print("For Node", node.label, " adjacent Node: ", adjacent.vertex.label, " indidentType: ",
    #               adjacent.incidentType)
    print("indegree: ",indegree," outdegree: ",outdegree)
    print('vertex count: ', graph2.get_vertex_count())
    print('edge count: ', graph2.get_edge_count())
    graph2.remove_edge(4, 1)
    print("*****After edge remove*****")
    indegree_after_rm = graph2.get_in_degree(4)
    outdegree_after_rm = graph2.get_out_degree(4)
    print("indegree: ",indegree_after_rm," outdegree: ",outdegree_after_rm)

    print('vertex count after edge delete: ', graph2.get_vertex_count())
    print('edge count after edge delete: ', graph2.get_edge_count())
    print("****after vertex remove****")
    graph2.remove_vertex(1)
    print('vertex count after edge delete: ', graph2.get_vertex_count())
    print('edge count after edge delete: ', graph2.get_edge_count())

    graph2.print_all_edge()