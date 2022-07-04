import DSAGraph as Graph

class FileIO():
    def __init__(self):
        self.GraphObj = Graph.DSAGraph()


    def readFile(self):
        try:
            filename = input("Name of file: ")
            with open(filename, "r") as f:
                for lines in f:
                    lett = lines.split()
                    for vals in lett:
                        if self.GraphObj.hasVertex(vals) == 0:
                            self.GraphObj.addVertex(vals, vals)

                    self.GraphObj.addEdge(lett[0],lett[1])
        except Exception as e:
            print(e, "Error reading file")

    def writeFile(self):
        try:
            fileName = input("Name of file to write to: ")
            with open(fileName,"w") as dataFile:
                for vert in self.GraphObj.vertList:
                    temp = vert.getAdjacent().split()
                    for i in temp:
                        dataFile.write(vert.getLabel() + ","+ i + "\n")

        except Exception as e:
            print(e, "Error reading file")



testGraph = FileIO()

testGraph.readFile()
print(testGraph.GraphObj.displayAsList())
print(testGraph.GraphObj.displayMatrix())
print(testGraph.GraphObj.beadthFirst("A"))
print(testGraph.GraphObj.depthFirst("A"))

testGraph.writeFile()
