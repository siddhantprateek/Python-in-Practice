class Vertex:
    def __init__(self):
        self.nbrs = {} # i.e. for vertex "A" contains the neighbours of A (the no. of neighbours)
        """
        here integer contains the weight
        """
        # [string, integer]
class Pair:
    def __init__(sel, vname, psf):
        self.vname = vname
        # path so far
        self.psf = psf



class Graph:
    def __init__(self):
        self.vtces = {} # Graph all vertex are maintained
        # key: vertexName String, value: reference

    def numVertex(self):
        # no. of key set the number of vertex
        return len(self.vtces)

    def containsVertex(self, vname):
        return vname in self.vtces

    def addVertex(self, value):
        vertex = Vertex()
        self.vtces[value] = vertex

    def removeVertex(self, vname):
        vertex = self.vtces[vname]
        # gets the object
        # we have to remove its neighbours
        keyS = list(vertex.nbrs.key())

        for key in keyS:
            neighbour = vtces.get(key)
            del neighbour.nbrs[vname]
        del self.vtces[vname]

    def display(self):
        keyS = list(self.vtces.key())

        # a: b, c display
        for key in keyS:
            vertex = slef.vtces[key]
            print(key, "->", vertex.nbrs)

    def numEdges(self):
        keyS = list(self.vtces.key())
        # check wheather it is not counted twice
        count = 0
        for key in keyS:
            vertex = self.vtces[key]
            count += len(vertex.nbrs)
        return count // 2

    def containsEdges(self, A, B):
        f = self.vtces[A}
        s = self.vtces[B]

        if f == None or s == None or B not in f.nbrs:
            return False

        return True

    def addEdge(self, first, second, weight):

        f = self.vtces[first]
        s = self.vtces[second]

        if f == None or s == None or or second in f.nbrs:
            return

        # assigning neighbours and their weight
        f.nbrs[second] = weight
        # if upadated in f then s ke mein bhi update karna hai
        s.nbrs[first] = weight


    def hasPath(self, first, second, visited):

        # map
        visted[first] = True

        if self.containsEdge(first, second):
            return True

        vertex = self.vtces[first]
        keyS = list(vertex.nbrs.keys())
        for key in keyS:
            if key not in visited and self.hasPath(key, secind, visited)
                return True

        return False

    def bfs(self, source, destination):

        processed = {}
        queue = Queue() # this is the one we created, please update code accordongly

        sp = Pair()
        sp.vname = source
        sp.psf = source

        queue.insert(sp)

        while not queue.isEmpty():

            if rp.vname in processed:
                continue

            rp = queue.remove()
            processed[rp.vname] = True

            if self.containsEdge(rp.vname, destination):
                print(rp.psf, destination)
                return True

            # neighbours
            rpvtx = self.vtces[rp.vname]
            nbrs =list(rpvtx.nbrs.key()) # list of string

            # path so far os romoved pair ka path so far and the current path
            for nbr in nbrs:
                if nbr not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    queue.insert(np)

            # when graph is not connected the it will return False
        return False
    def dfs(self, source, destination):
        # hashmap
        processed = {}

        stack = stack()
        sp = Pair(source, source)

        stack.insert(sp)
        while not stack.isEmpty():
            rp = stack.remove()

            if rp.vname in processed:
                continue

            processed[rp.vname] = True
            if self.containsEdge(rp.vname, destination):
                print(rp.psf, destination)
                return True

            # neighbour
            rpvtx = self.vtces[rp.vname]
            nbrs = list(rpvtx.nbrs.keys())
            for nbr in nbrs:
                # process only unporcessed neighbours
                if nbt not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    stack.insert(np)
            return False
    def isCyclic(self):
        # queue mein entry wapas ah jaye or processed mein wapas ah jayes

        processed = {}
        queue = Queue()
        keyS = list(self.vtces.keys())

        if key in KeyS:
            if key in processed:
                continue
            sp =Pair(key, Key)
            queue.insert(sp)
            while not queue.isEmpty():
                rp = queue.remove()

                if rp.vname in processed:
                    return True
            # neighbours
            rpvtx = self.vtces[rp.vname]
            nbrs =list(rpvtx.nbrs.key()) # list of string

            # path so far os romoved pair ka path so far and the current path
            for nbr in nbrs:
                if nbr not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    queue.insert(np)

        # when graph is not connected the it will return False
        return False

    def isConnected(self):

        processed = {}
        queue = Queue()
        keyS = list(self.vtces.keys())

        if key in KeyS:
            if key in processed:
                continue
            flag += 1
            sp =Pair(key, Key)
            queue.insert(sp)
            while not queue.isEmpty():
                rp = queue.remove()

                if rp.vname in processed:
                    continue
            # neighbours
            rpvtx = self.vtces[rp.vname]
            nbrs =list(rpvtx.nbrs.key()) # list of string

            # path so far os romoved pair ka path so far and the current path
            for nbr in nbrs:
                if nbr not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    queue.insert(np)

        # when graph is not connected the it will return False
        if flag >= 2:
            return False
        return True


    def isTree(self):
        return not self.isCyclic() and self.isConnected()


    class PrimsPair:
        def __init__(self, vname, acqvname, cost):
            self.vname = vname
            self.acqvname = acqvname
            self.cost = cost

        def __lt__(self, other):
            return other.cost - self.cost

        def prims(self):
            mst = Graph()

            map = {}
            heap = Heap()
            for key in self.vtces.keys():
                np = PrimsPair(key, None, math.inf)
                # np : new pair
                heap.add(np)
                hashMap[key] = np

            while not heap.isEmpty():
                rp = heap.remove()
                del HashMap[rp.vname]

                if rp.acqvname == None:
                    mst.addVertex(rp.vname)
                else:
                    mst.addVertex(rp.vname)
                    # aquired vname
                    mst.addEdge(rp.vname, rp.aqvname, rp.cost)

                # check neighbours  of rp
                for nbr in self.vtces[rp.vname].nbrs.keys():

                    # work for nbrs which are in Map
                    if nbr in hashMap:
                        oc = hashMap[nbr].cost
                        nc = self.vtces[rp.vname].nbrs[nbr]

                        if nc < oc:
                            gp = haspMap[nbr]

                            # this is sanme object as in heap, hence updating this will update heap too.
                            # this is why we are using hashMaps

                            gp.acqvname = rp.vname
                            gp.cost = nc

                            heap.updatePriority(gp) # custom one: you just need to fo UPHEAP now

            return mst


        def Dijsktra(self, src):
            ans = {} #<string, integer>
            haspMap = {}
            heap = Heap()

            for key in self.vtces.keys():
                np = PrimsPair(key, "", math.inf)

                if key == src:
                    np.cost = 0
                    np.psf = key

                heap.add(np)
                hashMap[key] = np

            while not heap,isEmpty():
                # remove a pair
                rp = heap.remove()
                del hashMap[rp.vname]

                ans.put(rp.vname, rp.cost)

                # check neighbours
                for nbr in self.vtces[rp.vname].nbrs.keys():
                    if nbr in hashMap:
                        oc = hashMap[nbr].cost
                        nc = rp.cost + self.vtces[rp.vname].nbrs[nbr]

                        if nc < oc:
                            gp = hashMap[nbr]
                            gp,psf = rp.psf + nbr
                            gp.cost = nc

                            # do upheap
                            heap.updatePriority(gp) # this is just update

            return ans



    # class DijsktraPair:
    #     def __init__(self, vname, psf, cost):
    #         self.vname = vname
    #         self.acqvname = acqvname
    #         self.cost = cost
    #
    #
