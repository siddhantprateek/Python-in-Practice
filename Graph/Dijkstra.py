import sys

class Graph():
    def __init__(self, vertices):
        self.vertex = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def printSolution(self, distance):
        print("Vertex Distance from Source")
        for node in range(self.vertex):
            print(node, "->" ,distance[node])

    def minDistance(self, distance, sptSet):

        min = sys.maxsize

        for vert in range(self.vertex):
            if distance[vert] < min  and sptSet[vert] == False:
                min = distance[vert]
                min_index = vert
        return min_index

    def Dijsktra(self, source):

        distance = [sys.maxsize] * self.vertex
        distance[source] = 0
        sptSet = [False]*self.vertex

        for i in range(self.vertex):

            temp = self.minDistance(distance, sptSet)
            sptSet[temp] = True 
            for v in range(self.vertex):
                if self.graph[temp][v] > 0 and sptSet[v] == False and distance[v] > distance[temp] + self.graph[temp][v]:
                    distance[v] = distance[temp] + self.graph[temp][v]

        self.printSolution(distance)



    # def isEmpty(self):
    #     return self.vertex == None

    # def Dijsktra(self, src):
    #     ans = {} #<string, integer>
    #     haspMap = {}
    #     heap = Heap()

    #     for key in self.vtces.keys():
    #         np = PrimsPair(key, "", math.inf)

    #         if key == src:
    #             np.cost = 0
    #             np.psf = key

    #         heap.add(np)
    #         hashMap[key] = np

    #     while not heap.isEmpty():
    #             # remove a pair
    #         rp = heap.remove()
    #         del hashMap[rp.vname]

    #         ans.put(rp.vname, rp.cost)

    #             # check neighbours
    #         for nbr in self.vtces[rp.vname].nbrs.keys():
    #             if nbr in hashMap:
    #                 oc = hashMap[nbr].cost
    #                 nc = rp.cost + self.vtces[rp.vname].nbrs[nbr]

    #                 if nc < oc:
    #                     gp = hashMap[nbr]
    #                     gp,psf = rp.psf + nbr
    #                     gp.cost = nc

    #                         # do upheap
    #                     heap.updatePriority(gp) # this is just update

    #     return ans


gph = Graph(9)
gph.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ];

gph.Dijsktra(0)