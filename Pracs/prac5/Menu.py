import BinaryTree as Tree
import pickle

class ListMenu():
    def __init__(self):
        self.BTree = Tree.DSASearchTree()

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
                    inObject.postorder()
                    print("\n")
                    for items in inObject.linkedL:
                        self.BTree.insert(items, items)
                    exitLoop = True
                except:
                    print("Error: Object file does not exist")

    def pickle(self, fileName):
        try:
            with open(fileName, "wb") as dataFile:
                pickle.dump(self.BTree,dataFile)
        except:
            print("Error: problem pickling object")

    def csvRead(self):
        fileName = input("Enter Filename: \n")
        try:
            dataFile = open(fileName, "r")
            for item in dataFile.readline().split(","):
                self.BTree.insert(item, item)
        except Exception as e:
            print("Error: Object File does not exist ", e)


    def csvWrite(self, fileName):
        distype = ""
        while distype != "pr" and distype != "po" and distype != "in":
            distype = input("preorder (pr), postorder (po) or inorder (in)?\n")

        if distype == "pr":
            self.BTree.preorder()
        elif distype == "po":
            self.BTree.postorder()
        elif distype == "in":
            self.BTree.inorder()

        #for i in self.BTree.linkedL:
        #    print(i)

        try:
            with open(fileName,"w") as dataFile:
                for i in self.BTree.linkedL:
                  dataFile.write(i + ",")
        except Exception as e:
            print("Error writing to file", e)

        self.BTree.cleanLinkedList()

    def dispayList(self):
        distype = input("preorder (pr), postorder (po) or inorder (in)?\n")
        print("Displaying List... \n")
        if distype == "pr":
            self.BTree.preorder()
            self.BTree.cleanLinkedList()
        elif distype == "po":
            self.BTree.postorder()
            self.BTree.cleanLinkedList()
        elif distype == "in":
            self.BTree.inorder()
            self.BTree.cleanLinkedList()
        print("\n ...Display Complete \n")

    def addValue(self, i):
        self.BTree.insert(i, i)

    def removeValue(self, i):
        self.BTree.delete(i)

    def getBalance(self):
        print(self.BTree.balance(), "\n\n")

    def getHeight(self):
        print(self.BTree.height(), "\n\n")


    def interactiveMenu(self):
        exitLoop = False
        while exitLoop == False:
            usrInput = ""
            while usrInput != "r" and usrInput != "w" and usrInput != "d" and usrInput != "a" and usrInput != "rm" and usrInput != "b" and usrInput != "h" and usrInput != "x":
                usrInput = input("#####\nRead File (r)\nWrite File (w) \nDisplay (d)\nadd value(a)\nRmove Value (rm)\nBalance (b)\nHeight (h)\nExit Program(x)\n#####\n")
            if usrInput == "x":
                exitLoop = True
            elif usrInput == "w":
                filetype = input("Csv file or Serialised file? (c/s)")
                fileName = input("Enter filename: ")
                if filetype == "s":
                    self.pickle(fileName)
                elif filetype == "c":
                    self.csvWrite(fileName)
            elif usrInput == "r":
                filetype = input("Csv file or Serialised file? (c/s)")
                if filetype == "s":
                    self.unPickle()
                elif filetype == "c":
                    self.csvRead()
            elif usrInput == "d":
                self.dispayList()
            elif usrInput == "rm":
                value = input("enter a value: \n")
                self.removeValue(value)
            elif usrInput == "a":
                value = input("enter a value \n")
                self.addValue(value)
            elif usrInput == "b":
                self.getBalance()
            elif usrInput == "h":
                self.getHeight()


menu = ListMenu()
menu.interactiveMenu()
