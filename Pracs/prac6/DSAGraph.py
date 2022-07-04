import linkedLists as List
import numpy as NP
import DSAQueue as Queue
import DSAStack as Stack

class DSAVertex():
    def __init__(self, value, label):
        self.visited = False
        self.value = value
        self.links = List.DSALinkedList()
        self.label = label

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        #return linked list values of edges split by spaces
        return_val = ""
        for values in self.links:
            if return_val == "":
                return_val = return_val + values.getLabel()
            else:
                return_val = return_val + " " + values.getLabel()
        return return_val

    def addEdgeV(self, vertex):
        self.links.insertLast(vertex)
        pass

    def isEdge(self, label):
        return_val = 0
        for edges in self.links:
            if edges.getLabel() == label:
                return_val = 1
        return return_val

    def setValue(self, value):
        self.value = value

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited

    def getEdgeCount(self):
        count = 0
        for items in self.links:
            count += 1
        return count

    def toString(self):
        #do this last
        pass

class DSAGraph():
    def __init__(self):
        self.vertList = List.DSALinkedList()
        self.matrix = NP.empty((20,20),dtype=object)
        self.sQueue = Queue.DSARollingQueue()
        self.sStack = Stack.DSAStack()

    #Assuming labels are from A-Z
    def addVertex(self, label, value):        
        if self.hasVertex(label) == 0:
            value = DSAVertex(value, label)
            self.vertList.insertLast(value)

    def addEdge(self, label1, label2):
        ref1 = self.getLabelRef(label1)
        ref2 = self.getLabelRef(label2)
        for item in self.vertList:
            if item.getLabel() == label1 and not item.isEdge(label2):
                item.addEdgeV(ref2)
            elif item.getLabel() == label2 and not item.isEdge(label1):
                item.addEdgeV(ref1)

    def getLabelRef(self, label):
        return_val = ""
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = item
        return return_val

    def hasVertex(self, label):
        return_val = 0
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = 1

        return return_val

    def getEdgeCount(self):
        count = 0
        for item in self.vertList:
            count += item.getEdgeCount()
        count = count/2
        return count

    def getVertexCount(self):
        count = 0
        for item in self.vertList:
            count += 1
        return count

    def isAdjacent(self, label1, label2):
        return_val = 0
        for i in self.vertList:
            if i.getLabel() == label1:
                if i.isEdge(label2):
                    return_val = 1
        return return_val

    def getAdjacent(self, label):
        return_val = None
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = item.getAdjacent()
        return return_val

    def displayAsList(self):
        return_val = ""
        for vert in self.vertList:
            return_val += vert.getLabel() + ": " + self.getAdjacent(vert.getLabel()) + "\n"
        return return_val

    def getNVert(self):
        counter = 0
        for vert in self.vertList:
            counter+=1
        return counter

    def displayMatrix(self):
        self.matrix.fill(0)
        size = self.getNVert()
        row = 1
        column = 0
        for vertexes in self.vertList:
            column = 0
            self.matrix[0][row] = vertexes.getLabel()
            self.matrix[row][0] = vertexes.getLabel()
            for adjacencies in self.vertList:
                column +=1
                if self.isAdjacent(vertexes.getLabel(), adjacencies.getLabel()) == 1:
                    self.matrix[column][row] = 1
            row +=1

        for i in range(0, size+1, 1):
            for j in range(0, size+1, 1):
                print(self.matrix[i][j], end = "")
            print("\n", end = "")

    def beadthFirst(self, label):
        for vertex in self.vertList:
            vertex.clearVisited()
        string = ""
        vertex = self.getLabelRef(label)
        self.sQueue.enqueue(vertex)
        vertex.setVisited()

        while self.sQueue.isEmpty() == False:
            v = self.sQueue.dequeue()
            vAdjacent = v.getAdjacent()
            for vertex in vAdjacent.split():
                vertex = self.getLabelRef(vertex)
                if vertex.getVisited() == False:
                    vertex.setVisited()
                    self.sQueue.enqueue(vertex)
            string += v.getLabel()

        return string
            
    #Not Working Properly
    def depthFirst(self, label):
        for vertex in self.vertList:
            vertex.clearVisited()
        
        string = ""
        self.sStack.push(label)
        self.depthFirstRec(label)

        while self.sStack.isEmpty() == False:
            string = self.sStack.pop() + string
        
        return string

    def depthFirstRec(self, label):
        v = self.getLabelRef(label)
        v.setVisited()

        vAdjacent = v.getAdjacent()
        for vert in vAdjacent.split():
            vertex = self.getLabelRef(vert)
            if vertex.getVisited() == False:
                self.sStack.push(vert)
                self.depthFirstRec(vert)





if __name__ == "__main__":
    test = DSAGraph()
    test.addVertex("A","Hi")
    test.addVertex("B", "Ho")
    test.addVertex("C", "He")
    test.addEdge("A","B")
    test.addEdge("C","A")
    print(test.getEdgeCount())
    print(test.displayAsList())
    test.displayMatrix()

    print("\nBreadth First Search: ")
    print(test.beadthFirst("A"))
    print("\nDepth First Search: ")
    print(test.depthFirst("A"))