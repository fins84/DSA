import linkedLists as List
import numpy as NP
import DSAQueue as Queue
import DSAStack as Stack

#
# DSA Graph Code taken and adapted from my DSA prac 6
#

"""
Name: DSAVertex
Input: str label, str value
Return: None
Function: Stores vertice label and adjacent edges
"""
class DSAVertex():
    def __init__(self, value, label):
        self.visited = False
        self.value = value
        self.links = List.DSALinkedList()
        self.label = label

    """
    Name: getLabel
    Input: None
    Return: str label
    Function: getter function for vertex label
    """
    def getLabel(self):
        return self.label

    """
    Name: getValue
    Input: None
    Return: str value
    Function: getter function for vertex value
    """
    def getValue(self):
        return self.value

    """
    Name: getAdjacent
    Input: None
    Return: str return_val - string split by ',' of all adjacent vertices
    Function: returns string of all adjacent vertices
    """
    def getAdjacent(self):
        #return linked list values of edges split by spaces
        return_val = ""
        for values in self.links:
            if return_val == "":
                return_val = return_val + values.getLabel()
            else:
                return_val = return_val + " " + values.getLabel()
        return return_val

    """
    Name: getAdjacentList
    Input: None
    Return: array List - list of all adjacent vertices
    Function: Return a list of all adjacent vertices
    """
    def getAdjacentList(self):
        list = NP.empty(self.getEdgeCount(), dtype=object)
        count = 0
        for values in self.links:
            list[count] = values
            count += 1
        return list

    """
    Name: addEdgeV
    Input: str vertex - name of dest vertex, int distance - edge distance, int security - security val, bool barrer, label - name of edge
    Return: None
    Function: add edge
    """
    def addEdgeV(self, vertex, distance, security, barriers, label):
        self.links.insertLast(DSAEdge(distance, security, barriers, label, vertex))

    """
    Name: isEdge
    Input: str label - label to lookup
    Return: int return_val - 0 false/ 1 true
    Function: checks if edge is in vertice by destination label
    """
    def isEdge(self, label):
        return_val = 0
        for edges in self.links:
            if edges.getLabel() == label:
                return_val = 1
        return return_val

    """
    Name: setValue
    Input: str value
    Return: None
    Function: setter function for value
    """
    def setValue(self, value):
        self.value = value

    """
    Name: setVisited
    Input: None
    Return: None
    Function: Sets visited to True
    """
    def setVisited(self):
        self.visited = True

    """
    Name: clearVisited
    Input: None
    Return: None
    Function: sets visited to false
    """
    def clearVisited(self):
        self.visited = False

    """
    Name: setLabel
    Input: str Label
    Return: None
    Function: sets label of vertice
    """
    def setLabel(self, label):
        self.label = label

    """
    Name: getVisited
    Input: None
    Return: bool visited
    Function: getter function for visited
    """
    def getVisited(self):
        return self.visited

    """
    Name: getEdgeCount
    Input: None
    Return: int count
    Function: gets number of edges
    """
    def getEdgeCount(self):
        count = 0
        for items in self.links:
            count += 1
        return count

    """
    Name: toStirng
    Input: None
    Return: str return_val
    Function: returns edge label, and all edges (and their parameters)
    """
    def toString(self):
        return_val = ("Label: " + self.label + " Connected to: ")
        for edges in self.links:
            return_val += (edges.getLabel() + " d: " + str(edges.getDistance()) + " s: " + str(edges.getSecurity()) + " b: " + str(edges.getBarriers()) + "; ")

        return return_val

"""
Name: DSAGraph
Input: None
Return: None
Function: Store/create/perform operations on graph, edges and vertices
"""
class DSAGraph():
    def __init__(self):
        self.vertList = List.DSALinkedList()
        self.sQueue = Queue.DSARollingQueue(10000)
        self.sStack = Stack.DSAStack(10000)
        self.fPath = List.DSALinkedList()

    """
    Name: addVertex
    Input: str label, str value
    Return: None
    Function: Adds a vertex to graph
    """
    #Assuming labels are from A-Z
    def addVertex(self, label, value):        
        if self.hasVertex(label) == 0:
            value = DSAVertex(value, label)
            self.vertList.insertLast(value)

    """
    Name: addEdge
    Input: str label1, str label2, int distance, int security, bool barriers
    Return: None
    Function: adds an edge from label1 to label2
    """
    def addEdge(self, label1, label2, distance, security, barriers):
        ref2 = self.getLabelRef(label2)
        for item in self.vertList:
            if item.getLabel() == label1:
                item.addEdgeV(ref2, distance, security, barriers, label2)
            """if item.getLabel() == label1 and not item.isEdge(label2):
                item.addEdgeV(ref2, distance, security, barriers, label2)"""

    """
    Name: getLabelRef
    Input: label
    Return: DSAVertex Object return_val
    Function: returns the object to the user, so they can edit it without needing to find it again (store as variable)
    """
    def getLabelRef(self, label):
        return_val = None
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = item

        if return_val == None:
            raise ValueError("No such vertex: " + label)
        return return_val

    """
    Name: hasVertex
    Input: label
    Return: int return_val
    Function: returns 0 if no vertices match label and 1 if true
    """
    def hasVertex(self, label):
        return_val = 0
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = 1

        return return_val

    """
    Name: getEdgeCount
    Input: None
    Return: int count
    Function: get total number of edges in graph
    """
    def getEdgeCount(self):
        count = 0
        for item in self.vertList:
            count += item.getEdgeCount()
        return count

    """
    Name: getVertexCount
    Input: None
    Return: int count
    Function: gets total number of vertices in graph
    """
    def getVertexCount(self):
        count = 0
        for item in self.vertList:
            count += 1
        return count

    """
    Name: isAdjacent
    Input: str label1, str label2
    Return: int return_val
    Function: return 1 if label1 adjacent has edge to label2, 0 otherwise
    """
    def isAdjacent(self, label1, label2):
        return_val = 0
        for i in self.vertList:
            if i.getLabel() == label1:
                if i.isEdge(label2):
                    return_val = 1
        return return_val

    """
    Name: getAdjacent
    Input: label
    Return: string return_val
    Function: calls vertice named label and gets all adjacent vertices
    """
    def getAdjacent(self, label):
        return_val = None
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = item.getAdjacent()
        return return_val

    """
    Name: getAdjacentArray
    Input: label
    Return: array return_val
    Function: calls vertice name label and gets all adjacent vertices in list
    """
    def getAdjacentArray(self, label):
        return_val = None
        for item in self.vertList:
            if item.getLabel() == label:
                return_val = item.getAdjacentList()

        return return_val

    """
    Name: displayAsList
    Input: None
    Return: str return_val
    Function: displays all vertices and their adjacent edges
    """
    def displayAsList(self):
        return_val = ""
        for vert in self.vertList:
            return_val += vert.getLabel() + ": " + self.getAdjacent(vert.getLabel()) + "\n"
        return return_val

    """
    Name: getNVert
    Input: None
    Return: int count
    Function: returns number of vertices in graph
    """
    def getNVert(self):
        counter = 0
        for vert in self.vertList:
            counter+=1
        return counter

    """
    Name: generateMatrix
    Input: None
    Return: 2d array matrix
    Function: creates a adjacency matrix from graph
    """
    def generateMatrix(self):
        nVert = self.getNVert() + 1
        matrix = NP.empty((nVert,nVert),dtype=object)
        label = NP.empty((nVert), dtype=object)
        matrix.fill(0)
        size = self.getNVert()
        row = 1
        column = 0
        for vertexes in self.vertList:
            column = 0
            matrix[0][row] = vertexes.getLabel()
            matrix[row][0] = vertexes.getLabel()
            for adjacencies in self.vertList:
                column +=1
                if self.isAdjacent(vertexes.getLabel(), adjacencies.getLabel()) == 1:
                    matrix[column][row] = self.getNAdjacentEdge(vertexes.getLabel(), adjacencies.getLabel())
            row +=1

        return(matrix)

    """
    Name: displayMatrix
    Input: 2d Array matrix
    Return: None
    Function: prints adjacency matrix
    """
    def displayMatrix(self, matrix):
        maxLen = 1
        nVert = self.getNVert() + 1

        for i in range(0, nVert, 1):
            if len(str(matrix[0][i])) > maxLen:
                maxLen = len(str(matrix[0][i])) + 2

        for i in range(0, nVert, 1):
            for j in range(0, nVert, 1):
                val = matrix[i][j]
                for k in range(0, maxLen - len(str(val))):
                    print(" ", end = "")
                print(val, end = "")
            print("")

    """
    Name: breadthFirst
    Input: str label
    Return: str string
    Function: performs a breadth first search from label
    """
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
            string += (" " + v.getLabel())

        return string

    """
    Name: depthFirst
    Input: label
    Return: str string
    Function: performs a depth first search from label
    """   
    def depthFirst(self, label):
        for vertex in self.vertList:
            vertex.clearVisited()
        
        string = ""
        self.sStack.push(label)
        self.depthFirstRec(label)

        while self.sStack.isEmpty() == False:
            string = self.sStack.pop() + " " + string
        
        return string

    """
    Name: depthFirstRec
    Input: label
    Return: None
    Function: Recursive method to go through whole list when performing depth first search
    """
    def depthFirstRec(self, label):
        v = self.getLabelRef(label)
        v.setVisited()

        vAdjacent = v.getAdjacent()
        for vert in vAdjacent.split():
            vertex = self.getLabelRef(vert)
            if vertex.getVisited() == False:
                self.sStack.push(vert)
                self.depthFirstRec(vert)


    #
    # Pathfinding pseudocode adapted from:
    # Elgabry, Omar. "Path Finding Algorithms", OmarElgabry's Blog, October, 11, 2016. https://medium.com/omarelgabrys-blog/path-finding-algorithms-f65a8902eb40
    #

    """
    Name: dfsPathFind
    Input: str start, str end, bool stairs, int security
    Return: None
    Function: performs a depth first search to find all paths from start to end satisfying paramets inputed
    """
    def dfsPathFind(self, start, end, stairs, security):
        #self.sStack = Stack.DSAStack()
        self.fPath = List.DSALinkedList() #Making sure empty for new dfs
        for vertex in self.vertList:
            vertex.clearVisited()
        if start != end:
            self.sStack.push(self.getLabelRef(start))
        self.dfsPathFindRec(start, end, stairs, security)

    """
    Name: dfsPathFindRec
    Input: str start, str end,bool aStairs,int security
    Return: None
    Function: recursive method for dfsPathFind to recurse through graph finding all paths
    """
    def dfsPathFindRec(self, start, end, aStairs, security):
        v = self.getLabelRef(start)
        if start == end:
            self.fPath.insertLast(self.sStack.getStackList())
        else:
            vAdjacent = v.getAdjacentList()
            for edges in vAdjacent:
                vertex = edges.getLabelRef()
                if aStairs == True:
                    if vertex.getVisited() == False and aStairs != edges.getBarriers() and edges.getSecurity() <= security:
                        self.sStack.push(edges)
                        vertex.setVisited()
                        self.dfsPathFindRec(vertex.getLabel(), end, aStairs, security)
                        vertex.clearVisited()
                        self.sStack.pop()
                else:
                    if vertex.getVisited() == False and edges.getSecurity() <= security:
                        self.sStack.push(edges)
                        vertex.setVisited()
                        self.dfsPathFindRec(vertex.getLabel(), end, aStairs, security)
                        vertex.clearVisited()
                        self.sStack.pop()

    """
    Name: printDFSFind
    Input: None
    Return: None
    Function: print all paths generated in dfsPathFind
    """
    def printDFSFind(self):
        for paths in self.fPath:
            for nodes in paths:
                print(nodes.getLabel(), end=" ")
            print("")
    
    """
    Name: getDFSRoutes
    Input: None
    Return: DSALinkedList fPath
    Function: getter function for fPath (list of all paths generated in dfsPathFind)
    """
    def getDFSRoutes(self):
        return self.fPath

    """
    Name: getVertex
    Input: Str label
    Return: str return_val
    Function: gets vertex label and return is toString function
    """
    def getVertex(self, label):
        return_val = "No such vertex"
        for verts in self.vertList:
            if verts.getLabel() == label:
                return_val = verts.toString()
        return return_val

    """
    Name: getEdge
    Input: str label1, str label2, int n
    Return: str return_val
    Function: gets nth edge from label1 to label2 (n is the nth edge from the two)
    """
    def getEdge(self, label1, label2, n):
        return_val = None
        edge = self.getEdgeRef(label1, label2, n)
        if edge != None:
            return_val = edge.toString()
        else:
            raise ValueError("No such edge, "+ label1 + " " + label2) 

        return_val = ("From: " + label1 + " " + return_val)
        return return_val

    """
    Name: listVerts
    Input: None
    Return: str returnVal
    Function: gets list of vertices and return it as a string
    """ 
    def listVerts(self):
        return_val = ""

        for verts in self.vertList:
            return_val += verts.getLabel() + "\n"

        return return_val

    """
    Name: deleteVert
    Input: str label
    Return: None
    Function: deletes vert of name label
    """ 
    def deleteVert(self, label):
        #delete vertex and all edges leading to it
        currNd = self.vertList.start
        while currNd.getNext() != None and currNd.data.getLabel() != label:
            currNd = currNd.getNext()

        if currNd.data.getLabel() == label:
            n = currNd.getIndex()
            self.vertList.removeNode(n)
        else:
            print("Vertex not in graph")

    """
    Name: deleteEdges
    Input: str label
    Return: None
    Function: deletes all edges that lead to vertice called label
    """ 
    def deleteEdges(self, label):
        currVertNd = self.vertList.start
        while currVertNd != None:
            currNd = currVertNd.data.links.start
            while currNd != None:
                if currNd.data.getLabel() == label:
                    n = currNd.getIndex()
                    currVertNd.data.links.removeNode(n)
                currNd = currNd.getNext()

            currVertNd = currVertNd.getNext()

    """
    Name: deleteEdge
    Input: str label1, str label2, int n
    Return: None
    Function: deletes specific label from label1 to label2 (nth repeat)
    """ 
    def deleteEdge(self, label1, label2, n):
        count = 0
        currVertNd = self.vertList.start
        while currVertNd != None:
            if currVertNd.data.getLabel() == label1:
                currNd = currVertNd.data.links.start
                while currNd != None:
                    if currNd.data.getLabel() == label2:
                        count += 1
                        if n == count:
                            g = currNd.getIndex()
                            currVertNd.data.links.removeNode(g)
                    currNd = currNd.getNext()
            currVertNd = currVertNd.getNext()

    """
    Name: updateVertName
    Input: str label, labelnew
    Return: None
    Function: updates vertice name
    """ 
    def updateVertName(self, label, labelNew):
        currVertNd = self.vertList.start
        while currVertNd != None:
            currNd = currVertNd.data.links.start
            while currNd != None:
                if currNd.data.getLabel() == label:
                    currNd.data.setLabel(labelNew)
                currNd = currNd.getNext()

            if currVertNd.data.getLabel() == label:
                currVertNd.data.setLabel(labelNew)
            currVertNd = currVertNd.getNext()

    """
    Name: updateEdgeDistance
    Input: str label1, str label2, int update, int n
    Return: None
    Function: updates the nth edge between label1 and label2 with distance update
    """ 
    def updateEdgeDistance(self, label1, label2, update, n):
        return_val = None
        edge = self.getEdgeRef(label1, label2, n)
        if edge != None:
            edge.setDistance(update)
        else:
            raise ValueError("No such edge, "+ label1 + " " + label2) 

    """
    Name: updateEdgeSecurity
    Input: str label1, str label2, in update, int n
    Return: None
    Function: updates the nth edge between label1 and label2 with security update
    """ 
    def updateEdgeSecurity(self, label1, label2, update, n):
        return_val = None
        edge = self.getEdgeRef(label1, label2, n)
        if edge != None:
            edge.setSecurity(update)
        else:
            raise ValueError("No such edge, "+ label1 + " " + label2) 

    """
    Name: updateEdgeBarriers
    Input: str label1, str label2, int update, int n
    Return: None
    Function: updates the nth edge between label1 and label2 with barriers update
    """ 
    def updateEdgeBarriers(self, label1, label2, update, n):
        return_val = None
        edge = self.getEdgeRef(label1, label2, n)
        if edge != None:
            edge.setBarriers(update)
        else:
            raise ValueError("No such edge, "+ label1 + " " + label2) 

    """
    Name: getEdgeRef
    Input: str label1, str label2, int n
    Return: DSAEdge return_val
    Function: gets the reference to the nth edge between label1 and label2
    """ 
    def getEdgeRef(self, label1, label2, n):
        count = 0
        return_val = None
        for verts in self.vertList:
            if verts.getLabel() == label1:
                for edge in verts.links:
                    if edge.getLabel() == label2:
                        count += 1
                        if count == n:
                            return_val = edge

        if return_val == None:
            raise ValueError("Error getting edge reference")
        return return_val

    """
    Name: getNAdjacentEdge
    Input: str label1, str label2
    Return: int ount
    Function: gets number of adjacent edges between label1 and label2
    """ 
    def getNAdjacentEdge(self, label1, label2):
        count = 0
        for verts in self.vertList:
            if verts.getLabel() == label1:
                for edge in verts.links:
                    if edge.getLabel() == label2:
                        count += 1

        return count



"""
Name: DSAEdge
Input: int distance, int security, bool barriers, str label, DSAVertex labelRef
Return: None
Function: Store all data to an edge between two vertexes
"""
class DSAEdge():
    def __init__(self, distance, security, barriers, label, labelRef):
        self.distance = distance
        self.security = security
        self.barriers = barriers
        self.label = label
        self.labelRef = labelRef

    """
    Name: setDistance
    Input: int distance
    Return: None
    Function: setter for distance variable
    """
    def setDistance(self, distance):
        self.distance = distance

    """
    Name: setSecurity
    Input: int security
    Return: None
    Function: setter for security variable
    """
    def setSecurity(self, security):
        self.security = security

    """
    Name: setBarriers
    Input: bool barriers
    Return: None
    Function: setter for barriers variable
    """
    def setBarriers(self, barriers):
        self.barriers = barriers

    """
    Name: setlabel
    Input: str label
    Return: None
    Function: setter for label variable
    """
    def setLabel(self, label):
        self.label = label

    """
    Name: setlabelRef
    Input: DSAVertex labelRef
    Return: None
    Function: setter for labelRef
    """
    def setLabelRef(self, labelRef):
        self.labelRef = labelRef

    """
    Name: getDistance
    Input: None
    Return: int distance
    Function: getter for distance variable
    """
    def getDistance(self):
        return self.distance

    """
    Name: getSecurity
    Input: None
    Return: int security
    Function: getter for security variable
    """
    def getSecurity(self):
        return self.security

    """
    Name: getBarriers
    Input: None
    Return: bool barriers
    Function: getter for barriers variable
    """
    def getBarriers(self):
        return self.barriers
    
    """
    Name: getlabel
    Input: None
    Return: str label
    Function: getter for label Variable
    """
    def getLabel(self):
        return self.label

    """
    Name: getLabelRef
    Input: None
    Return: DSAVertex labelRef
    Function: getter for labelRef variable
    """
    def getLabelRef(self):
        return self.labelRef

    """
    Name: toString
    Input: None
    Return: str return_val
    Function: returns overview of edge, name and parameters
    """
    def toString(self):
        return_val = ("Destination: " + self.label + " Security: " + str(self.security) + " Stairs: " + str(self.barriers) + " Distance: " + str(self.distance))
        return return_val



if __name__ == "__main__":
    test = DSAGraph()
    for i in range(0,8,1):
        test.addVertex(str(i),str(i))
    test.addEdge("0", "1", 0, 2, False)
    test.addEdge("1","3", 0, 2, False)
    test.addEdge("2","1", 0, 2, False)
    test.addEdge("3","2", 0, 2, False)
    test.addEdge("3","4", 0, 2, False)
    test.addEdge("4","5", 0, 2, False)
    test.addEdge("6","4", 0, 2, False)
    test.addEdge("5","7", 0, 2, False)
    test.addEdge("7","6", 0, 2, False)
    test.addEdge("0","2", 0, 2, False)
    test.addEdge("2","6", 0, 2, False)

    print(test.getEdgeCount())
    print(test.displayAsList())
    test.displayMatrix(test.generateMatrix())

    print("\nBreadth First Search: ")
    print(test.beadthFirst("0"))
    print("\nDepth First Search: ")
    print(test.depthFirst("0"))

    test.dfsPathFind("0", "7", False, 2)
    test.printDFSFind()