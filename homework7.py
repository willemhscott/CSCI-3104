

class Graph():

    def __init__(self, adjacency_matrix):
        """ 
        Graph initialized with a weighted adjacency matrix 
        
        Attributes
        ----------
        adjacency_matrix : 2D array
            non-negative integers where adjacency_matrix[i][j] is the weight of the edge i to j,
            with 0 representing no edge

        """

        self.adjacency_matrix = adjacency_matrix

        # Add more class variables below as needed, such as n:
        # self.N = len(adjacency_matrix)


    
    def Prim(self):
        """
        Use Prim-Jarnik's algorithm to find the length of the minimum spanning tree starting from node 0

        Returns
        -------
        int
            Weighted length of tree

        """
        nodes = {i: float('inf') for i in range(len(self.adjacency_matrix)) }
        nodes[0] = 0

        cost = 0
        mst = []
        parents = {}
        while len(mst) != len(self.adjacency_matrix):
            vert = min(nodes, key=lambda x: (x in mst, nodes[x]))
            mst.append(vert)
            cost += nodes[vert]
            for j, edge in enumerate(self.adjacency_matrix[vert]):
                if edge:
                    if edge < nodes[j]:
                        nodes[j] = edge
                        parents[j] = vert

        #print(nodes, mst, parents)
        return cost
    

G = Graph([[0, 10, 11, 33, 60],
           [10, 0, 22, 14, 57],
           [11, 22, 0, 11, 17],
           [33, 14, 11, 0, 9],
           [60, 57, 17, 9, 0]])

g = G.Prim()
#print(g)
#assert g == 41

G = Graph([ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] )
#print(G.Prim())

G = Graph([[0,7,4,3,0,0],
          [7,0,8,1,0,9],
          [4,8,0,0,5,2],
          [3,1,0,0,6,-1],
          [0,0,5,6,0,10],
          [0,9,2,-1,10,0]])

#print(G.Prim())
