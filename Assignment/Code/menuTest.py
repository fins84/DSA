import Menu

class menuTest():
    def __init__(self):
        pass

    def testMenu(self):
        menu = Menu.ListMenu()

        menu.readFile("testSaveData/testReadData/Map.txt")
        menu.readJourneyFile("testSaveData/testReadData/Journey.txt")
        menu.pickle("testSaveData/pickleTest")
        menu.nMatrix = menu.mapGraph.generateMatrix()
        menu.mapGraph.displayMatrix(menu.nMatrix)
        menu.matrixToCsv("testSaveData/matrixtoCsv.txt", menu.nMatrix)
        menu.worldToCsv("testSaveData/worldCsv.txt")
        menu.graphToCsv("testSaveData/graphCSV")
        menu.pathFind()
        menu.displayRankedRoutes()
        menu.saveRankedRoutes("testSaveData/RankedRoutes.txt")
        menu.generateNetwork()
        menu.displayNetwork()

        

    def testEmptyRead(self):
        menu = Menu.ListMenu()
        try:
            menu.readFile("NoFile.txt")
        except Exception as e:
            print("Exception: " + e)

        try:
            menu.readJourneyFile("Nojourney.txt")
        except Exception as e:
            print("Exception: " + e)

        try:
            menu.unpickle("NoFile.txt")
        except Exception as e:
            print("Exception: " + e)

        try:
            menu.generateNetwork()
        except Exception as e:
            print("Exception: " + e)

        try:
            menu.displayNetwork()
        except Exception as e:
            print("Exception: " + e)

        try:
            menu.displayRankedRoutes()
        except Exception as e:
            print("Exception: " + e)
    
        try:
            menu.pathFind()
        except TypeError as e:
            print("Exception: " + str(e))

        try:
            menu.sortRoutes()
        except Exception as e:
            print("Exception: " + str(e))

        try:
            menu.insertionSort()
        except Exception as e:
            print("Exception: " + str(e))

        try:
            menu.matrixToCsv()
        except Exception as e:
            print("Exception: " + str(e))

        try:
            menu.nMatrix = menu.mapGraph.generateMatrix()
        except Exception as e:
            print("Exception: " + e)
        try:
            menu.matrixToCsv("testSaveData/matToCSVNoData.txt", menu.nMatrix)
        except Exception as e:
            print("Exception: " + e) 

        try:
            menu.worldToCsv("testSaveData/worldToCsvNoData.txt")
        except Exception as e:
            print("Exception: " + e)



test = menuTest()
test.testMenu()
#test.testEmptyRead()