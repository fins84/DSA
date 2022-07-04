import DSAGraph as Graph
import re
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle

"""
ToDo
9. test harness for all functions
10. UML diagram
11. report
"""

"""
Class: ListMenu()
Function: Allows for graphs to be made into maps for the assignment performing functions on them
Constructor Arguments: None
"""
class ListMenu():
    def __init__(self):
        self.mapGraph = Graph.DSAGraph()
        self.netGraph = nx.DiGraph()
        self.start = None
        self.end = None
        self.nMatrix = None
        self.pSec = 0
        self.pStair = False

    """
    Name: readFile
    Inputs: str fileName - Name of file to read from
    Returns: None
    Function: reads in a map file and creates a graph from it (directional graph)
    """
    def readFile(self, fileName):
        try:
            with open(fileName, "r") as file:
                for line in file:
                    #doesn't look at lines starting with comment hashtag
                    if re.search("(#.*)", line) ==  None:
                        data = line.split("|")
                        #checking direction of edge <>
                        if re.search(".*\<\>.*", data[0]):
                            #add vertex and node
                            location = data[0].split("<>")
                            loc1 = location[0]
                            loc2 = location[1]
                            d, s, b = self.getParameters(data)
                            if self.mapGraph.hasVertex(loc1) == 0:
                                self.mapGraph.addVertex(loc1, loc1)
                            if self.mapGraph.hasVertex(loc2) == 0:
                                self.mapGraph.addVertex(loc2, loc2)

                            self.mapGraph.addEdge(loc1, loc2, d, s, b)
                            self.mapGraph.addEdge(loc2, loc1, d, s, b)
                        #checking direction of edge <
                        elif re.search(".*\<[^\>].*", data[0]):
                            #add vertex and node
                            location = data[0].split("<")
                            loc1 = location[0]
                            loc2 = location[1]
                            d, s, b = self.getParameters(data)
                            if self.mapGraph.hasVertex(loc1) == 0:
                                self.mapGraph.addVertex(loc1, loc1)
                            if self.mapGraph.hasVertex(loc2) == 0:
                                self.mapGraph.addVertex(loc2, loc2)
                            self.mapGraph.addEdge(loc2, loc1, d, s, b)
                        #checking direction of edge <
                        elif re.search(".*[^\<]\>.*", data[0]):
                            #add vertex and node
                            location = data[0].split(">")
                            loc1 = location[0]
                            loc2 = location[1]
                            d, s, b = self.getParameters(data)
                            if self.mapGraph.hasVertex(loc1) == 0:
                                self.mapGraph.addVertex(loc1, loc1)
                            if self.mapGraph.hasVertex(loc2) == 0:
                                self.mapGraph.addVertex(loc2, loc2)
                            self.mapGraph.addEdge(loc1, loc2, d, s, b)
        except Exception as e:
            print(e, "Error reading file")

    """
    Name: readJourneyFile
    Inputs: str fileName - Name of file to read from
    Returns: None
    Function: reads in a journey file, sets parameters for getting from two nodes in graph
    """
    def readJourneyFile(self, fileName):
        try:
            with open(fileName, "r") as file:
                for line in file:
                    lineSplit = line.split(" ")
                    #checks for starting destination
                    if lineSplit[0] == "From":
                        #check if starting node exists in graph
                        if self.mapGraph.getLabelRef(lineSplit[1]) != None:
                            self.start = lineSplit[1]
                        else:
                            raise ValueError("Start node doesn't exist")
                    #check for destination node
                    elif lineSplit[0] == "To":
                        #check if destination node exists in graph
                        if self.mapGraph.getLabelRef(lineSplit[1]) != None:
                            self.end = lineSplit[1]
                        else:
                            raise ValueError("End node doesn't exist")
                    #check for stair needs
                    elif lineSplit[0] == "Avoid":
                        self.pStair = True
                    #check for security needs
                    elif lineSplit[0] == "Security":
                        if lineSplit[1].isdigit() == True:
                            self.pSec = int(lineSplit[1])
        except Exception as e:
            print(e)
        
    """
    Name: pickle
    Inputs: str fileName - Name of file to write to
    Returns: None
    Function: serialises the graph object and saves it as fileName
    """
    def pickle(self, fileName):
        try:
            with open(fileName, "wb") as dataFile:
                pickle.dump(self.mapGraph, dataFile)
        except:
            print("Error: problem pickling object")

    """
    Name: unpickle
    Inputs: str fileName - Name of file to read from
    Returns: None
    Function: reads in a serialised graph object and sets class graph to it
    """
    def unpickle(self, fileName):
        try:
            with open(fileName,"rb") as dataFile:
                newMapGraph = pickle.load(dataFile)
                #check if unpickled file is a Graph object
                if isinstance(newMapGraph, Graph.DSAGraph):
                    self.mapGraph = newMapGraph
                else:
                    raise TypeError("Unpickled object is not of Graph Type")
        except Exception as e:
            print(e)

    """
    Name: matrixToCsv
    Inputs: str fileName - name of file, 2d array matrix - adjacency matrix of graph
    Returns: None
    Function: Saves the generated adjacency matrix to a file
    """
    def matrixToCsv(self, fileName, matrix):
        nVert = self.mapGraph.getNVert()
        n = 0
        try:
            with open(fileName, "w") as file:
                #for columns
                for i in range(0, nVert, 1):
                    n = 0
                    #for row
                    for j in range(0, nVert, 1):
                        n+= 1
                        file.write(str(matrix[i][j]))
                        #check if there are values after (can't csv line on ',')
                        if n < nVert:
                            file.write(",")
                    file.write("\n")
        except Exception as e:
            print("Error writing to file " + fileName + " " + e)

    """
    Name: worldToCsv
    Inputs: str fileName - name of file to save to
    Returns: None
    Function: saves list of each vertex and their edges to a file
    """
    def worldToCsv(self, fileName):
        try:
            with open(fileName, "w") as file:
                for verts in self.mapGraph.vertList:
                    #save vertices and all adjacent edges
                    file.write(verts.toString() + "\n")
        except Exception as e:
            print("Error writing to file " + fileName + " " + e)

    """
    Name: graphToCsv
    Inputs: str fileName - name of file to save to
    Returns: None
    Function: Saves graph into a map input style file (can use readFile on it)
    """
    def graphToCsv(self, fileName):
        try:
            with open(fileName, "w") as file:
                for verts in self.mapGraph.vertList:
                    for edges in verts.links:
                        stair = ""
                        if edges.getBarriers() == True:
                            stair = "stairs"
                        #format a map file you can read from after
                        file.write(verts.getLabel() + ">" + edges.getLabel() + "|" + "D:" + str(edges.getDistance()) + "|" + "S:" + str(edges.getSecurity()) + "|" + "B:" + stair + "\n")
        except Exception as e:
            print("Error writing to file", e)

    """
    Name: getParameters
    Inputs: list data - .split() of readFile line
    Returns: list data - individual edge parameters
    Function: converts .split() readfile line data into usable edge parameters
    """
    # Note this function is used in file io
    def getParameters(self, data):
        ray = np.empty(3, dtype=object)
        b = False
        d = self.stringNumber(data[1])
        s = self.stringNumber(data[2])
        
        #looks for stairs string and returns number in the string
        if re.search("stairs", data[3]):
            b = True

        ray[0] = d
        ray[1] = s
        ray[2] = b

        return ray

    """
    Name: stringNumber
    Inputs: str string - string containing an integer
    Returns: int number
    Function: extracts the integer from the string ignoring all characters (using regex)
    """
    def stringNumber(self, string):
        number = None

        #finds all numbers in string
        n = re.findall("\d+", string)
        if n: 
            #get last number
            number = int(n[-1])
        else:
            number = 0
        return number

    """
    Name: interactiveMenu
    Inputs: None
    Returns: None
    Function: provides a user interface to perform tasks on the graph (save/plan journey/display/node and edge functions)
    """
    def interactiveMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3" and usrInput != "4" and usrInput != "5" and usrInput != "6" and usrInput != "7" and usrInput != "8" and usrInput != "9" and usrInput != "10" and usrInput != "11":
                usrInput = input("########\n(1)Load input file\n(2)Node Operations\n(3)Edge Operations\n(4)Parameter Tweaks\n(5)Generate Matrix\n(6)Display World\n(7)Enter Journey Details\n(8)Generate Routes\n(9)Display Routes\n(10)Save\n(11)Exit\n########\n")
            if usrInput == "1":
                self.loadFile()
            elif usrInput == "2":
                self.nodeOperations()
            elif usrInput == "3":
                self.edgeOperations()
            elif usrInput == "4":
                self.parameterTweaks()
            elif usrInput == "5":
                self.nMatrix = self.mapGraph.generateMatrix()
                self.GraphMenu()
            elif usrInput == "6":
                self.displayWorldMenu()
            elif usrInput == "7":
                self.journeyDetail()
            elif usrInput == "8":
                #check if user has set a starting and ending destination
                if self.start == None and self.end == None:
                    print("Please enter the starting and ending destination first")
                else:
                    print("Generating journey...")
                    self.pathFind()
                    print(self.mapGraph.fPath.count)
            elif usrInput == "9":
                self.displayRoute()
            elif usrInput == "10":
                self.SaveFileMenu()
            elif usrInput == "11":
                exitLoop = True

    """
    Name: displayWorldMenu
    Inputs: None
    Returns: None
    Function: provides a user interface to allow user to generate and display the graph in a readable format
    """
    def displayWorldMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nDisplay World\n(1)Display Graph\n(2)Display Nodes and their Edges\n(3)Exit\n########\n")
            if usrInput == "1":
                self.generateNetwork()
                self.displayNetwork()
            elif usrInput == "2":
                #display vertices and their edges
                for verts in self.mapGraph.vertList:
                    print(verts.toString())
                inputChoice = ""
                while inputChoice != "y" and inputChoice != "n":
                    inputChoice = input("Save to file (y/n)")
                if inputChoice == "y":
                    fileName = input("Enter a filename: ")
                    self.worldToCsv(fileName)
            elif usrInput == "3":
                exitLoop = True

    """
    Name: nodeOperations
    Inputs: None
    Returns: None
    Function: provides a user interface to allow user to perform operations/edit vertices/nodes of the graph
    """
    def nodeOperations(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3" and usrInput != "4" and usrInput != "5":
                usrInput = input("########\nNode Operations\n(1)find\n(2)insert\n(3)delete\n(4)update\n(5)Exit\n########\n")
            if usrInput == "1":
                print(self.mapGraph.listVerts())
                choice = input("Name of vertex to find: ")
                print(self.mapGraph.getVertex(choice))
            elif usrInput == "2":
                label = input("Name of vertex: ")
                self.mapGraph.addVertex(label, label)
            elif usrInput == "3":
                print(self.mapGraph.listVerts())
                choice = input("Name of vertex to delete: ")
                self.mapGraph.deleteVert(choice)
                self.mapGraph.deleteEdges(choice)
            elif usrInput == "4":
                print(self.mapGraph.listVerts())
                choice = input("Which vertex name do you want to update: ")
                newLabel = input("What do you want the new name to be: ")
                if self.mapGraph.getVertex(choice) == ("Vertex not in graph"):
                    print("Vertex not in graph")
                else:
                    self.mapGraph.updateVertName(choice, newLabel)
            elif usrInput == "5":
                exitLoop = True

    """
    Name: edgeOperations
    Inputs: None
    Returns: None
    Function: provides a user interface to allow user to perform operations on edge in the graph
    """
    def edgeOperations(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3" and usrInput != "4" and usrInput != "5":
                usrInput = input("########\nEdge Operations:\n(1)find\n(2)insert\n(3)delete\n(4)update\n(5)Exit\n########\n")
            if usrInput == "1":
                #give user list of start and vertices to choose from
                print(self.mapGraph.listVerts())
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                n = self.mapGraph.getNAdjacentEdge(start, end)
                #print all edges in direction
                print("There are: ", n , " edges")
                try:
                    for i in range(1, n+1, 1):
                        print(self.mapGraph.getEdge(start, end, i))
                except Exception as e:
                    print(e)
            elif usrInput == "2":
                security = ""
                distance = ""
                stairs = False
                print(self.mapGraph.listVerts())
                #choose direction of edge
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                #choose security 
                while not security.isdigit():
                    security = input("N of security: ")
                if int(security) <= 0:
                    security = 0
                #choose distance
                while not distance.isdigit():
                    distance = input("distance: ")
                #set stairs
                while stairs != "y" and stairs != "n":
                    stairs = input("Any stairs? (y/n): ")
                if stairs == "y":
                    stairs = True
                else:
                    stairs = False
                try:
                    self.mapGraph.addEdge(start, end, distance, int(security), stairs)
                except Exception as e:
                    print(e)

            elif usrInput == "3":
                print(self.mapGraph.listVerts())
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                #choose direction of edge
                n = self.mapGraph.getNAdjacentEdge(start, end)
                #print number of edges
                print("There are: ", n , " edges")
                try:
                    #print all edges
                    for i in range(1, n+1, 1):
                        print(self.mapGraph.getEdge(start, end, i))
                except Exception as e:
                    print(e)
                #if more than one edge, give user option to select edge for deletion
                if n>=2:
                    inpChoice = 0
                    while inpChoice > n or inpChoice <= 0:
                        inpChoice = int(input("Which edge would you like to delete (1-"+str(n)+"): "))
                    self.mapGraph.deleteEdge(start, end, int(inpChoice))
                else:
                    self.mapGraph.deleteEdge(start, end, 1)

            elif usrInput == "4":
                self.edgeUpdate()
            elif usrInput == "5":
                exitLoop = True

    """
    Name: parameterTweaks 
    Inputs: None
    Returns: None
    Function: provides user interface to user to adjust parameters in the journey
    """
    def parameterTweaks(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nParameter Tweaks:\n(1)Change Stair Requirements\n(2)Change Security Requirements\n(3)Exit\n########\n")
            if usrInput == "1":
                stairs = ""
                #input needs to be y/n, doesn't compare to set value when changing
                while stairs != "y" and stairs != "n":
                    stairs = input("Avoid stairs (y/n): ")
                #convert to boolean
                if stairs == "y":
                    stairs = True
                else:
                    stairs = False
                self.pStair = stairs
            elif usrInput == "2":
                security = ""
                #input needs to be int
                while not security.isdigit():
                    security = input("N of security: ")
                security = int(security)
                #security > 0 no upper bounds
                if security <= 0:
                    security = 0
                self.pSec = security
            elif usrInput == "3":
                exitLoop = True

    """
    Name: journeyDetail
    Inputs: None
    Returns: None
    Function: provides a user interface for user to set start and end desination of journey
    """
    def journeyDetail(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nJourney Details:\n(1)Starting Node\n(2)Destination Node\n(3)Exit\n########\n")
            if usrInput == "1":
                #check if there is more than 1 vert (for start and end destination)
                if self.mapGraph.getNVert() >= 1:
                    #user must choose a vert in graph
                    inChoice = ""
                    while self.mapGraph.getVertex(inChoice) == "No such vertex":
                        print(self.mapGraph.listVerts())
                        inChoice = input("Enter starting Node: ")
                    self.start = inChoice
                else:
                    print("No nodes")
            elif usrInput == "2":
                #check if there is more than 1 vert (for start and end destination)
                if self.mapGraph.getNVert() >= 1:
                    inChoice = ""
                    #user must choose a vert in graph
                    while self.mapGraph.getVertex(inChoice) == "No such vertex":
                        print(self.mapGraph.listVerts())
                        inChoice = input("Enter Ending Node: ")
                    self.end = inChoice
                else:
                    print("No Nodes")
            elif usrInput == "3":
                exitLoop = True

    """
    Name: GraphMenu
    Inputs: None
    Returns: None
    Function: provides a user interface for a user to generate/display/save an adjacency matrix of the graph
    """
    def GraphMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nJourney Details:\n(1)Display Graph\n(2)Save Graph\n(3)Exit\n########\n")
            if usrInput == "1":
                self.mapGraph.displayMatrix(self.nMatrix)
            elif usrInput == "2":
                fileName = input("Enter name of map file: ")
                self.matrixToCsv(fileName, self.nMatrix)
            elif usrInput == "3":
                exitLoop = True

    """
    Name: saveFileMenu
    Inputs: None
    Returns: None
    Function: provides a user interface to save the graph object to a csv or serialised file
    """
    def SaveFileMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nSave File:\n(1)To File\n(2)Pickle\n(3)Exit\n########\n")
            if usrInput == "1":
                fileName = input("Enter name of map file: ")
                self.graphToCsv(fileName)
            elif usrInput == "2":
                fileName = input("Enter name of map file: ")
                self.pickle(fileName)
            elif usrInput == "3":
                exitLoop = True

    """
    Name: edgeUpdate
    Inputs: None
    Returns: None
    Function: provides a user interface for the user to change parameters in edges
    """
    def edgeUpdate(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3" and usrInput != "4":
                usrInput = input("########\nEdge Value Update:\n(1)Stairs\n(2)Security\n(3)Distance\n(4)Exit\n########\n")
            if usrInput == "1":
                newStair = ""
                #choosing edge from verts
                print(self.mapGraph.listVerts())
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                #can be more than one edge
                n = self.mapGraph.getNAdjacentEdge(start, end)
                print("There are: ", n , " edges")
                try:
                    for i in range(1, n+1, 1):
                        print(self.mapGraph.getEdge(start, end, i))
                except Exception as e:
                    print(e)
                #choose edge to update
                if n>=2:
                    inpChoice = 0
                    while inpChoice > n or inpChoice <= 0:
                        inpChoice = int(input("Which edge would you like to update(1-"+str(n)+"): "))
                else:
                    inpChoice = 1

                try:
                    #update edge stair parameter
                    print(self.mapGraph.getEdge(start, end, inpChoice))
                    while(newStair != "y" and newStair != "n"):
                        newStair = input("Is there stairs in edge? (y/n): ")
                    if newStair == "y":
                        newStair = True
                    else:
                        newStair = False
                    self.mapGraph.updateEdgeBarriers(start, end, newStair, inpChoice)
                except Exception as e:
                    print(e)
            elif usrInput == "2":
                newSecurity = ""
                #choosing edge from verts
                print(self.mapGraph.listVerts())
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                #can be more than one edge
                n = self.mapGraph.getNAdjacentEdge(start, end)
                print("There are: ", n , " edges")
                try:
                    for i in range(1, n+1, 1):
                        print(self.mapGraph.getEdge(start, end, i))
                except Exception as e:
                    print(e)
                #choose edge
                if n>=2:
                    inpChoice = 0
                    while inpChoice > n or inpChoice <= 0:
                        inpChoice = int(input("Which edge would you like to update (1-"+str(n)+"): "))
                else:
                    inpChoice = 1

                try:
                    #update security parameter
                    print(self.mapGraph.getEdge(start, end, inpChoice))
                    while(not newSecurity.isnumeric()):
                        newSecurity = input("How much security: (number)")

                    self.mapGraph.updateEdgeSecurity(start, end, newSecurity, inpChoice)
                except Exception as e:
                    print(e)
            elif usrInput == "3":
                newDistance = ""
                #choosing edge from verts
                print(self.mapGraph.listVerts())
                start = input("Starting vertex: ")
                end = input("Destination vertex: ")
                #can be more than one edge in same direction
                n = self.mapGraph.getNAdjacentEdge(start, end)
                print("There are: ", n , " edges")
                try:
                    for i in range(1, n+1, 1):
                        print(self.mapGraph.getEdge(start, end, i))
                except Exception as e:
                    print(e)
                #choosing edge
                if n>=2:
                    inpChoice = 0
                    while inpChoice > n or inpChoice <= 0:
                        inpChoice = int(input("Which edge would you like to update (1-"+str(n)+"): "))
                else:
                    inpChoice = 1

                try:
                    #updating distance parameter
                    print(self.mapGraph.getEdge(start, end, inpChoice))
                    while(not newDistance.isnumeric()):
                        newDistance = input("How long is distance: (number)")
                    self.mapGraph.updateEdgeDistance(start, end, newDistance, inpChoice)
                except Exception as e:
                    print(e)
            elif usrInput == "4":
                exitLoop = True

    """
    Name: generateNetwork
    Inputs: none
    Returns: DiGraph newNetwork - networkx graph of graph object
    Function: converts map graph into a displayable graph
    """
    def generateNetwork(self):
        #create new newtorkx graph
        self.netGraph = newNetwork = nx.DiGraph()

        #iterate through all vertices adding all edges
        for nodes in self.mapGraph.vertList:
            for edges in nodes.links:
                n = nodes.getLabel()
                e = edges.getLabel()
                newNetwork.add_edge(n, e, nEdges=self.mapGraph.getNAdjacentEdge(n, e))
        return newNetwork

    """
    Name: displayNetwork
    Inputs: None
    Returns: None
    Function: displays generated networkx graph to user (has functionality to save)
    """
    def displayNetwork(self):
        #generate specific layout
        pos = nx.spring_layout(self.netGraph)
        #axis to draw on
        ax = plt.gca()
        #draw graph on axis, with labels
        nx.draw_networkx(self.netGraph, pos, ax=ax, with_labels=True, font_color="#4B6587", font_size=8, node_size=1500, node_color="#F0E5CF", connectionstyle = ("Arc3, rad=0.2"))
        plt.show()

    """
    Name: displayRoute
    Inputs: None
    Returns: None
    Function: provides a user interface to allow user to display and save generated journey routes
    """
    def displayRoute(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3" and usrInput != "4":
                usrInput = input("########\nDisaplay Route:\n(1)Display Routes\n(2)Display Ranked Routes\n(3)Save\n(4)Exit\n########\n")
            if usrInput == "1":
                self.mapGraph.printDFSFind()
            elif usrInput == "2":
               self.displayRankedRoutes()
            elif usrInput == "3":
               fileName = input("Enter a filename: ")
               self.saveRankedRoutes(fileName)
            elif usrInput == "4":
                exitLoop = True

    """
    Name: loadFile
    Inputs: None
    Returns: None
    Function: provides a user interface to allow user to choose between reading in a serialised file and a csv file
    """
    def loadFile(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "1" and usrInput != "2" and usrInput != "3":
                usrInput = input("########\nLoad File:\n(1)Read File\n(2)Unpickle Object\n(3)Exit\n########\n")
            if usrInput == "1":
                fileName = input("Enter name of map file: ")
                self.readFile(fileName)
            elif usrInput == "2":
                fileName = input("Enter name of file: ")
                #checking if right instance done in unpickle method
                self.unpickle(fileName)
            elif usrInput == "3":
                exitLoop = True

    """
    Name: pathFind
    Inputs: None
    Returns: None
    Function: Accesses graph object pathfinding function to generate path then saves path to class variables
    """
    def pathFind(self):
        #search based on start and end nodes and preset/set parameters
        self.mapGraph.dfsPathFind(self.start, self.end, self.pStair, self.pSec)

    """
    Name: displayRankedRoutes
    Inputs: None
    Returns: None
    Function: displays generated routes in order of distance needed to travel from start to finish
    """
    def displayRankedRoutes(self):
        sortedRay = self.sortRoutes(self.mapGraph.getDFSRoutes())
        for rows in sortedRay:
            print("Distance: " + str(rows[1]), end = " Journey: ")
            count = 0
            for values in rows[0]:
                #print each edge in journey one after the other
                if count == 0 or isinstance(values, Graph.DSAVertex):
                    print(values.getLabel(), end = "; ")
                else:
                    print(values.getLabel() + "  D:" + str(values.getDistance()) + " Sec:"+str(values.getSecurity()) + " Stairs:" + str(values.getBarriers()) , end= "; ")
                count += 1
            print("") #newline for next longer journey

    """
    Name: saveRankedRoutes
    Inputs: str fileName - name of file to save to
    Returns: None
    Function: saves generated routes in order of distance to a file
    """
    def saveRankedRoutes(self, fileName):
        #sort routes before save
        sortedRay = self.sortRoutes(self.mapGraph.getDFSRoutes())
        try:
            with open(fileName, "w") as dataFile:
                for rows in sortedRay:
                    dataFile.write("Distance: " + str(rows[1]) +  " Journey: ")
                    count = 0
                    for values in rows[0]:
                        if count == 0 or isinstance(values, Graph.DSAVertex):
                            #start of journey list is vertice
                            dataFile.write(values.getLabel() + " ")
                        else:
                            #other nodes are edges
                            dataFile.write(values.getLabel() + "  D:" + str(values.getDistance()) + " Sec:"+str(values.getSecurity()) + " Stairs:" + str(values.getBarriers()) + "; ")
                        count += 1
                    dataFile.write("\n") #next slower journey
        except Exception as e:
            print("Error reading file " + e)
                

    """
    Name: sortRoutes
    Inputs: linkedList routeList - linked list containing all generated routes (each linked list index is a route)
    Returns: 2d array sortedRay - 2d array containing routes and their distances (sorted smallest to largest)
    Function:
    """
    def sortRoutes(self, routeList):
        nVals = routeList.getCount()
        sortedRay = np.empty([nVals, 2], dtype=object)

        count = 0
        #for each route
        for values in routeList:
            #save route to array
            sortedRay[count][0] = values
            dist = 0
            #sum of distances
            for i in range(0, len(values)):
                if i != 0 and isinstance(values[i], Graph.DSAEdge):
                    dist += values[i].getDistance()
            sortedRay[count][1] = dist
            count += 1

        #sort array on distances
        sortedRay = self.insertionSort(sortedRay, nVals)
        return sortedRay

    """
    Name: insertionSort
    Inputs: 2d array routeList - linked list of all routes and their distances, int length - number of routes generated
    Returns: 2d array routeList - sorted array based on route distances 
    Function: Sorts a 2d array of routes from smallest to largest based on the distance of journey
    """
    def insertionSort(self, routeList, length):
        #for each index
        for n in range(1,length):
            i = n
            #check if i is smaller than n index and swap if true
            while i>0 and routeList[i-1][1] > routeList[i][1]:
                temp = routeList[i].copy()
                routeList[i] = routeList[i-1]
                routeList[i-1] = temp
                i -= 1
        return routeList

    #Insertion sort code taken and adapted from my prac 1 submission

        

#test function for interactive menu
if __name__ == "__main__":
    test = ListMenu()
    test.interactiveMenu()


