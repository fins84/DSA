import DSAGraph as Graph

class testGraph():
    def __init__(self):
        self.graph = Graph.DSAGraph()
    def testEmpty(self):
        print("\n****Testing Empty Graph Object****\n")

        try:
            print("\nGet Label Ref:")
            print(self.graph.getLabelRef("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nhasVertex:")
            print(self.graph.hasVertex("foo"))
        except Exception as e:
            print("Exception: " ,e) 

        try:
            print("\ngetEdgeCount:")
            print(self.graph.getEdgeCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertexCount:")
            print(self.graph.getVertexCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nisAdjacent:")
            print(self.graph.isAdjacent("foo","ba"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacent:")
            print(self.graph.getAdjacent("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacentArray:")
            print(self.graph.getAdjacentArray("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayAsList:")
            print(self.graph.displayAsList())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNVert:")
            print(self.graph.getNVert())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngenerateNatrix:")
            print(self.graph.generateMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayMatrix:")
            print(self.graph.displayMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nbreadthFirst search:")
            print(self.graph.beadthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndepthFirst search:")
            print(self.graph.depthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndfs path find:")
            print(self.graph.dfsPathFind("foo", "bar", True, 0))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nprintDFSFind:")
            print(self.graph.printDFSFind())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetDFSRouts:")
            print(self.graph.getDFSRoutes())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertex:")
            print(self.graph.getVertex("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdge:")
            print(self.graph.getEdge("foo","bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nlistVerts:")
            print(self.graph.listVerts())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteVert:")
            print(self.graph.deleteVert("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteEdges:")
            print(self.graph.deleteEdges("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteEdge:")
            print(self.graph.deleteEdge("foo", "bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateVertName:")
            print(self.graph.updateVertName("foo", "bar"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateEdgeDistance:")
            print(self.graph.updateEdgeDistance("foo", "bar", "hello", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateEdgeBarriers:")
            print(self.graph.updateEdgeBarriers("foo", "bar", "hello", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdgeRef:")
            print(self.graph.getEdgeRef("foo", "bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNAdjacentEdge:")
            print(self.graph.getNAdjacentEdge("foo", "bar"))
        except Exception as e:
            print("Exception: " ,e)

    def testFalseWithData(self):
        for i in range(0,8,1):
            self.graph.addVertex(str(i),str(i))
        self.graph.addEdge("0", "1", 0, 2, False)
        self.graph.addEdge("1","3", 0, 2, False)
        self.graph.addEdge("2","1", 0, 2, False)
        self.graph.addEdge("3","2", 0, 2, False)
        self.graph.addEdge("3","4", 0, 2, False)
        self.graph.addEdge("4","5", 0, 2, False)
        self.graph.addEdge("6","4", 0, 2, False)
        self.graph.addEdge("5","7", 0, 2, False)
        self.graph.addEdge("7","6", 0, 2, False)
        self.graph.addEdge("0","2", 0, 2, False)
        self.graph.addEdge("2","6", 0, 2, False)

        print("\n****Testing False Values for Graph Object with data****\n")

        try:
            print("\nGet Label Ref:")
            print(self.graph.getLabelRef("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nhasVertex:")
            print(self.graph.hasVertex("foo"))
        except Exception as e:
            print("Exception: " ,e) 

        try:
            print("\ngetEdgeCount:")
            print(self.graph.getEdgeCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertexCount:")
            print(self.graph.getVertexCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nisAdjacent:")
            print(self.graph.isAdjacent("foo","ba"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacent:")
            print(self.graph.getAdjacent("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacentArray:")
            print(self.graph.getAdjacentArray("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayAsList:")
            print(self.graph.displayAsList())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNVert:")
            print(self.graph.getNVert())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngenerateNatrix:")
            print(self.graph.generateMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayMatrix:")
            print(self.graph.displayMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nbreadthFirst search:")
            print(self.graph.beadthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndepthFirst search:")
            print(self.graph.depthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndfs path find:")
            print(self.graph.dfsPathFind("foo", "bar", True, 0))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nprintDFSFind:")
            print(self.graph.printDFSFind())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetDFSRouts:")
            print(self.graph.getDFSRoutes())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertex:")
            print(self.graph.getVertex("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdge:")
            print(self.graph.getEdge("foo","bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nlistVerts:")
            print(self.graph.listVerts())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteVert:")
            print(self.graph.deleteVert("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteEdges:")
            print(self.graph.deleteEdges("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteEdge:")
            print(self.graph.deleteEdge("foo", "bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateVertName:")
            print(self.graph.updateVertName("foo", "bar"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateEdgeDistance:")
            print(self.graph.updateEdgeDistance("foo", "bar", "hello", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateEdgeBarriers:")
            print(self.graph.updateEdgeBarriers("foo", "bar", "hello", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdgeRef:")
            print(self.graph.getEdgeRef("foo", "bar", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNAdjacentEdge:")
            print(self.graph.getNAdjacentEdge("foo", "bar"))
        except Exception as e:
            print("Exception: " ,e) 

    def testRealWithData(self):
        for i in range(0,8,1):
            self.graph.addVertex(str(i),str(i))
        self.graph.addEdge("0", "1", 0, 2, False)
        self.graph.addEdge("1","3", 0, 2, False)
        self.graph.addEdge("2","1", 0, 2, False)
        self.graph.addEdge("3","2", 0, 2, False)
        self.graph.addEdge("3","4", 0, 2, False)
        self.graph.addEdge("4","5", 0, 2, False)
        self.graph.addEdge("6","4", 0, 2, False)
        self.graph.addEdge("5","7", 0, 2, False)
        self.graph.addEdge("7","6", 0, 2, False)
        self.graph.addEdge("0","2", 0, 2, False)
        self.graph.addEdge("2","6", 0, 2, False)

        print("\n****Testing Real Values for Graph Object with data****\n")
        print("original data:")
        print(self.graph.displayAsList())

        try:
            print("\nAdd Vertex:")
            print(self.graph.addVertex("foo", "foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nAdd Edge:")
            print(self.graph.addEdge("foo","1", 0, 2,True))
        except Exception as e:
            print("Exception: " ,e)

        print(self.graph.displayAsList())

        try:
            print("\nGet Label Ref:")
            print(self.graph.getLabelRef("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nhasVertex:")
            print(self.graph.hasVertex("foo"))
        except Exception as e:
            print("Exception: " ,e) 

        try:
            print("\ngetEdgeCount:")
            print(self.graph.getEdgeCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertexCount:")
            print(self.graph.getVertexCount())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nisAdjacent:")
            print(self.graph.isAdjacent("foo","1"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacent:")
            print(self.graph.getAdjacent("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetAdjacentArray:")
            print(self.graph.getAdjacentArray("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayAsList:")
            print(self.graph.displayAsList())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNVert:")
            print(self.graph.getNVert())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngenerateNatrix:")
            print(self.graph.generateMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndisplayMatrix:")
            print(self.graph.displayMatrix())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nbreadthFirst search:")
            print(self.graph.beadthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndepthFirst search:")
            print(self.graph.depthFirst("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndfs path find:")
            print(self.graph.dfsPathFind("foo", "7", True, 0))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nprintDFSFind:")
            print(self.graph.printDFSFind())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetDFSRouts:")
            print(self.graph.getDFSRoutes())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetVertex:")
            print(self.graph.getVertex("foo"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdge:")
            print(self.graph.getEdge("foo","1", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nlistVerts:")
            print(self.graph.listVerts())
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteVert:")
            print(self.graph.deleteVert("2"))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ndeleteEdges:")
            print(self.graph.deleteEdges("1"))
        except Exception as e:
            print("Exception: " ,e)

        print(self.graph.displayAsList())

        try:
            print("\ndeleteEdge:")
            print(self.graph.deleteEdge("7", "6", 1))
        except Exception as e:
            print("Exception: " ,e)

        print(self.graph.displayAsList())

        try:
            print("\nupdateVertName:")
            print(self.graph.updateVertName("foo", "bar"))
        except Exception as e:
            print("Exception: " ,e)

        print(self.graph.displayAsList())

        try:
            print("\nupdateEdgeDistance:")
            print(self.graph.updateEdgeDistance("0", "2", 5, 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\nupdateEdgeBarriers:")
            print(self.graph.updateEdgeBarriers("0", "2", "hello", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetEdgeRef:")
            print(self.graph.getEdgeRef("0", "2", 1))
        except Exception as e:
            print("Exception: " ,e)

        try:
            print("\ngetNAdjacentEdge:")
            print(self.graph.getNAdjacentEdge("3", "2"))
        except Exception as e:
            print("Exception: " ,e) 




