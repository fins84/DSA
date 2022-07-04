import linkedLists as List
import pickle

class ListMenu():
    def __init__(self):
        self.link_L = List.DSALinkedList()

    def neworOldList(self):
        type_choice = ""
        while(type_choice != "o" and type_choice != "n"):
            type_choice = input("Add to list (o) or New (n) linked list?")
        return type_choice

    def unPickle(self):
        exitLoop = False

        while exitLoop == False:
            fileName = input("Exit (x) or Enter a filename: ")
            if fileName == "x":
                exitLoop = True
            else:
                try:
                    with open(fileName,"rb") as dataFile:
                        inObject = pickle.load(dataFile)
                    for items in inObject:
                        self.link_L.insertLast(items)
                    exitLoop = True
                except:
                    print("Error: Object file does not exist")

    def pickle(self, fileName):
        try:
            with open(fileName, "wb") as dataFile:
                pickle.dump(self.link_L,dataFile)
        except:
            print("Error: problem pickling object")

    def dispayList(self):
        print("Displaying List... \n")
        for items in self.link_L:
            print(items)
        print("\n ...Display Complete \n")

    def insertFirst(self):
        data = input("\nWhat data would you like to input: ")
        self.link_L.insertFirst(data)

    def insertLast(self):
        data = input("\nWhat data would you like to input: ")
        self.link_L.insertLast(data)

    def removeFirst(self):
        data = self.link_L.removeFirst()
        print("\nremoved: ", data, "\n")

    def removeLast(self):
        data = self.link_L.removeLast()
        print("\nremoved: ", data, "\n")

    def interactiveMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "r" and usrInput != "w" and usrInput != "d" and usrInput != "rf" and usrInput != "rl" and usrInput != "if" and usrInput != "il" and usrInput != "x":
                usrInput = input("#####\nRead Serialised fiel (r)\nWrite SerialisedFile(w) \nDisplay the list(d)\nRemoveFirst(rf)\nRmoveLast(rl)\nInsertFirst(if)\nInsertLast(il)\nExit Program(x)\n#####\n")
            if usrInput == "x":
                exitLoop = True
            elif usrInput == "w":
                fileName = input("Enter filename: ")
                self.pickle(fileName)
            elif usrInput == "r":
                self.unPickle()
            elif usrInput == "d":
                self.dispayList()
            elif usrInput == "rf":
                self.removeFirst()
            elif usrInput == "rl":
                self.removeLast()
            elif usrInput == "if":
                self.insertFirst()
            elif usrInput == "il":
                self.insertLast()


menu = ListMenu()
menu.interactiveMenu()
