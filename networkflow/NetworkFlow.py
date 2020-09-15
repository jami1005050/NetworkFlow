#Date: 12/08/2019
#Class: CS5310
#Assignment: Network Flow
#Author(s): Mohammad Jaminur Islam

from graphbuilder.constant import DIRECTED_GRAPH
from graphbuilder.edge import Edge
from graphbuilder.graph import Graph
from graphbuilder.vertex import Vertex
from linearprogramSolver.Simplex import Simplex


class FlowNetwork:
    def __init__(self):
        self.simplex = None

    def getPath(self, graph,start, end, path):
        if start == end:
            return path
        vertex1 = graph.search_vertex_by_label(start)
        for edge in vertex1.edgeList:
            residualCapacity = edge.weight - edge.flow
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(graph, edge.endNode.label, end, path + [(edge, residualCapacity)])
                if result != None:
                    return result

    def calculateMaxFlow(self,graph):
        source = None
        sink = None
        if not (isinstance(graph,Graph)): #check if it is instance of max flow
            return
        for vertex in graph.vertexList: #iterrate to vertex list to get the vertex source and sink
            if vertex.type == 's':
                source = vertex
            if vertex.type == 't':
                sink = vertex

        if source == None or sink == None:
            return "Network does not have source and sink"
        path = self.getPath(graph,source.label, sink.label, [])  # take one path
        while path != None:   #calculate flow for each path
            flow = min(edge[1] for edge in path)
            for edge, res in path: # residual graph and flow calculation
                print("edge: ", edge.startNode.label, " ", edge.endNode.label)

                edge.flow += flow
                edge.returnEdge.flow -= flow
            path = self.getPath(graph,source.label, sink.label, [])
        vertex1 = graph.search_vertex_by_label(source.label)
        return sum(edge.flow for edge in vertex1.edgeList) #return the cumulative sum of the values

    def form_Simplex(self,graph):
        if not (isinstance(graph,Graph)):  #if the passed instance is not graph return 0
            return
        edgeCount = graph.get_edge_count() #took edge count for free variable manipulation
        vertexCount = graph.get_vertex_count() # for calculating the inner node constraint apart from source and destination
        numberOfConstraints = vertexCount + edgeCount - 2
        edgeList = graph.get_edge_list() #taking edgelist to map them as variables
        new_map = {new_list: [] for new_list in range(edgeCount)}
        i = 0
        for edge in edgeList:
            new_map[edge] = i #mapping for edge
            i = i + 1
        # print(new_map)
        rowIndex = 0
        constantMatrix = [[0 for i in range(edgeCount)] for j in range(numberOfConstraints)]
        sinkVertex = None
        for vertex in graph.vertexList:
            if(vertex.type == 's'):
                continue
            if(vertex.type == 't'):
                sinkVertex = vertex
                continue
            incomingEdge = graph.get_edges_incoming(vertex.label) #for incoming setting values 1
            outGoingEdge = graph.get_edges_out_going(vertex.label) #for outgoing setting values -1
            for edge in incomingEdge:
                index = new_map.get(edge)
                constantMatrix [rowIndex] [index] = 1
            for edge in outGoingEdge:
                index = new_map.get(edge)
                constantMatrix [rowIndex] [index] = -1
            rowIndex = rowIndex + 1
        for edge in edgeList: #setting constraint equation for edges
            index = new_map.get(edge)
            # print("index", index," rowIndex",rowIndex)
            constantMatrix [rowIndex] [index] = -1
            rowIndex  = rowIndex + 1
        right_side_constants = [0 for i in range(numberOfConstraints)]
        rightSideIndex = 0
        for i in range(vertexCount-2):  #setting right side 0 for inner node constraint
            right_side_constants[rightSideIndex] = 0
            rightSideIndex = rightSideIndex + 1

        for j in range (edgeCount): #setting right side constraint for edges
            right_side_constants[rightSideIndex] = edgeList [j].weight
            rightSideIndex = rightSideIndex + 1
        # right_side_constants[19] = right_side_constants[19]
        co_efficient = [0 for i in range(edgeCount)]

        sinkEdges = graph.get_edges_on_node(sinkVertex.label) #sink node incident edges for calculating objective function
        # graph.print_all_edge()
        for edge in edgeList:
            index = new_map.get(edge)
            print("Index: ",index," edge ",edge.startNode.label," ",edge.endNode.label)

        for edge in sinkEdges:
            index = new_map.get(edge)
            # print("Index: ",index," edge ",edge.startNode.label," ",edge.endNode.label)
            co_efficient [index] = 1
        print ("constantMatrix" ,constantMatrix)
        print("right SI: ",right_side_constants)
        print("coefficient Matrix",co_efficient)
        simplex = Simplex(constantMatrix, right_side_constants, co_efficient, numberOfConstraints, edgeCount) #call simplex
        self.simplex = simplex
        ret = self.simplex.simplex_main()

    def formSimplexFromGraph(self):
        numberOfCols = 8
        numberOfRows = 12
        constantMatrix = [[0 for i in range(numberOfCols)] for j in range(numberOfRows)]
        #region matrix
        constantMatrix[0][0] = 1
        constantMatrix[0][1] = 0
        constantMatrix[0][2] = -1
        constantMatrix[0][3] = -1
        constantMatrix[0][4] = 0
        constantMatrix[0][5] = 0
        constantMatrix[0][6] = 0
        constantMatrix[0][7] = 0
        constantMatrix[1][0] = 0
        constantMatrix[1][1] = -1
        constantMatrix[1][2] = -1
        constantMatrix[1][3] = 0
        constantMatrix[1][4] = 1
        constantMatrix[1][5] = 0
        constantMatrix[1][6] = 0
        constantMatrix[1][7] = 0
        constantMatrix[2][0] = 0
        constantMatrix[2][1] = 0
        constantMatrix[2][2] = 0
        constantMatrix[2][3] = 0
        constantMatrix[2][4] = 1
        constantMatrix[2][5] = -1
        constantMatrix[2][6] = 0
        constantMatrix[2][7] = -1
        constantMatrix[3][0] = 0
        constantMatrix[3][1] = 0
        constantMatrix[3][2] = 0
        constantMatrix[3][3] = -1
        constantMatrix[3][4] = 0
        constantMatrix[3][5] = 0
        constantMatrix[3][6] = 1
        constantMatrix[3][7] = -1
        constantMatrix[4][0] = -1
        constantMatrix[4][1] = 0
        constantMatrix[4][2] = 0
        constantMatrix[4][3] = 0
        constantMatrix[4][4] = 0
        constantMatrix[4][5] = 0
        constantMatrix[4][6] = 0
        constantMatrix[4][7] = 0
        constantMatrix[5][0] = 0
        constantMatrix[5][1] = -1
        constantMatrix[5][2] = 0
        constantMatrix[5][3] = 0
        constantMatrix[5][4] = 0
        constantMatrix[5][5] = 0
        constantMatrix[5][6] = 0
        constantMatrix[5][7] = 0
        constantMatrix[6][0] = 0
        constantMatrix[6][1] = 0
        constantMatrix[6][2] = -1
        constantMatrix[6][3] = 0
        constantMatrix[6][4] = 0
        constantMatrix[6][5] = 0
        constantMatrix[6][6] = 0
        constantMatrix[6][7] = 0
        constantMatrix[7][0] = 0
        constantMatrix[7][1] = 0
        constantMatrix[7][2] = 0
        constantMatrix[7][3] = -1
        constantMatrix[7][4] = 0
        constantMatrix[7][5] = 0
        constantMatrix[7][6] = 0
        constantMatrix[7][7] = 0
        constantMatrix[8][0] = 0
        constantMatrix[8][1] = 0
        constantMatrix[8][2] = 0
        constantMatrix[8][3] = 0
        constantMatrix[8][4] = -1
        constantMatrix[8][5] = 0
        constantMatrix[8][6] = 0
        constantMatrix[8][7] = 0
        constantMatrix[9][0] = 0
        constantMatrix[9][1] = 0
        constantMatrix[9][2] = 0
        constantMatrix[9][3] = 0
        constantMatrix[9][4] = 0
        constantMatrix[9][5] = -1
        constantMatrix[9][6] = 0
        constantMatrix[9][7] = 0
        constantMatrix[10][0] = 0
        constantMatrix[10][1] = 0
        constantMatrix[10][2] = 0
        constantMatrix[10][3] = 0
        constantMatrix[10][4] = 0
        constantMatrix[10][5] = 0
        constantMatrix[10][6] = -1
        constantMatrix[10][7] = 0
        constantMatrix[11][0] = 0
        constantMatrix[11][1] = 0
        constantMatrix[11][2] = 0
        constantMatrix[11][3] = 0
        constantMatrix[11][4] = 0
        constantMatrix[11][5] = 0
        constantMatrix[11][6] = 0
        constantMatrix[11][7] = -1
        #endregion

        ##region Right SIde
        right_side_constants = [0 for i in range(numberOfRows)]
        right_side_constants[0] = 0
        right_side_constants[1] = 0
        right_side_constants[2] = 0
        right_side_constants[3] = 0
        right_side_constants[4] = 10
        right_side_constants[5] = 2
        right_side_constants[6] = 10
        right_side_constants[7] = 7
        right_side_constants[8] = 8
        right_side_constants[9] = 5
        right_side_constants[10] = 10
        right_side_constants[11] = 8
        #endregion

        #region Coefficient
        co_efficient = [0 for i in range(numberOfCols)]
        co_efficient[0] = 0
        co_efficient[1] = 0
        co_efficient[2] = 0
        co_efficient[3] = 0
        co_efficient[4] = 0
        co_efficient[5] = 1
        co_efficient[6] = 1
        co_efficient[7] = 0
        #endregion

        #region 2nd Matrix
        constantMatrix2 = [
            [1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, -1, -1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, -1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, -1, 0, -1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 1, 0, 0, -1],
            [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]]
        #endregion
        rightSI = [0, 0, 0, 0, 0, 0, 10, 9, 15, 4, 5, 15, 8, 4, 16, 6, 15, 15, 10, 10, 10]
        coefficientMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        simplex = Simplex(constantMatrix2, rightSI, coefficientMatrix, 21, 15)
        ret = simplex.simplex_main()
        print("it is returning ",ret)
if __name__ =='__main__':
    #region Graph
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
    graph2.insert_edge_by_ends(vertex1, vertex2, 10)
    graph2.insert_edge_by_ends(vertex1, vertex3, 8)  # source to other node 3
    graph2.insert_edge_by_ends(vertex2, vertex3, 2)
    graph2.insert_edge_by_ends(vertex2, vertex4, 5)
    graph2.insert_edge_by_ends(vertex3, vertex5, 10)
    graph2.insert_edge_by_ends(vertex5, vertex4, 8)
    graph2.insert_edge_by_ends(vertex5, vertex6, 10)  # other node 5 to sink
    graph2.insert_edge_by_ends(vertex4, vertex6, 7)  # other node 4 to sink
    # graph2.print_all_edge()

    networkFLow = FlowNetwork()
    # networkFLow.form_Simplex(graph2)

    graphNew = Graph(DIRECTED_GRAPH)  # directed graph
    vertex1 = Vertex(1)  # source
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
    graphNew.insert_edge_by_ends(vertex6, vertex8, 15)# other node 6 to sink
    graphNew.insert_edge_by_ends(vertex6, vertex7, 10)
    graphNew.insert_edge_by_ends(vertex7, vertex3, 6)
    graphNew.insert_edge_by_ends(vertex7, vertex8, 10)# other node 7 to sink
    #endregion
    networkFLow.form_Simplex(graphNew) #call to simplex

    #
    #networkFLow.formSimplexFromGraph()
    # networkFLow.form_Simplex(graph2)
    maxflow = networkFLow.calculateMaxFlow(graphNew) # call to ford fulkerson method
    print("Max Flow: ",maxflow)
    print ("Simplex flow: ", networkFLow.simplex.objectiveValue,"  general ford fulkerson flow: ",maxflow)