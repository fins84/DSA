import sys
import Menu

usage = ""

def printError():
    print("Error: invalid number of arguments")
    print("To run in interactive mode input 'python3 whereNow.py -i'")
    print("To run in silent mode input 'python3 whereNow.py -s mapfile journeyfile savefile'")

logic = Menu.ListMenu()
#check if interactive mode
if len(sys.argv) == 2:
    if(sys.argv[1] == "-i"):
        logic.interactiveMenu()
    else:
        printError()
#check if silent mode
elif len(sys.argv) == 5:
    if(sys.argv[1] == "-s"):
        graphFile = sys.argv[2]
        journey = sys.argv[3]
        saveFile = sys.argv[4]
        logic.readFile(graphFile)
        logic.readJourneyFile(journey)
        logic.pathFind()
        logic.saveRankedRoutes(saveFile)

    else:
        printError()
#otherwise print usage information
else:
    printError()


#whereNow.py -s Map.txt Journey.txt test
#whereNow.py -i