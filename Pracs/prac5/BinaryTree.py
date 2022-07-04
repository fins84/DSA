import linkedLists as Linked


class DSASearchTree():
    def __init__(self):
        self._root = None
        self.linkedL = Linked.DSALinkedList()
    
    def find(self, key):
        try:
            return_val = self._findRec(key, self._root)
        except:
            print("Error: Value not found")
        return return_val

    def _findRec(self, key, cur):
        value = None
        if cur == None:
            raise ValueError("Key " + str(key) + " not found")
        elif key == cur.getKey():
            value = cur.getValue()
        elif key < cur.getKey():
            value = self._findRec(key, cur.getLeft())
        else:
            value = self._findRec(key, cur.getRight())

        return value

    def insert(self, key, value):
        try:
            return_val = self._insert(key, value, self._root)
        except:
            print("Error: Value already in tree")
        return return_val

    def _insert(self, key, value, cur):
        updateNode = cur
        if cur == None:
            newNode = DSATreeNode(key, value)
            updateNode = newNode
            if(self._root == None):
                self._root = newNode
        elif key == cur.getKey():
            raise ValueError("Value already in tree")
        elif key < cur.getKey():
            cur.setLeft(self._insert(key, value, cur.getLeft()))
        else:
            cur.setRight(self._insert(key, value, cur.getRight()))

        return updateNode

    def delete(self, key):
        try:
            self._root = self.deleteRec(key,self._root)
        except:
            print("Error deleting node")

    def deleteRec(self, key, cur):
        updateNode = cur
        if cur == None:
            raise ValueError("Node is empty")
        elif key == cur.getKey():
            updateNode = self.deleteNode(cur)
        elif key < cur.getKey():
            cur.setLeft(self.deleteRec(key, cur.getLeft()))
        else:
            cur.setRight(self.deleteRec(key, cur.getRight()))
        
        return updateNode

    def deleteNode(self, node):
        updateNode = None

        if node.getLeft() == None and node.getRight() == None:
            updateNode = None
        elif node.getLeft() != None and node.getRight() == None:
            updateNode = node.getLeft()
        elif  node.getLeft() == None and node.getRight() != None:
            updateNode = node.getRight()
        else:
            updateNode = self.promoteSuccessor(node.getRight())
            if updateNode != node.getRight():
                updateNode.setRight(node.getRight())
            updateNode.setLeft(node.getLeft())

        return updateNode

    def promoteSuccessor(self,cur):
        successor = cur

        if cur.getLeft() != None:
            successor = self.promoteSuccessor(cur.getLeft())
            if successor == cur.getLeft():
                cur.setLeft(successor.getRight())

        return successor

    def height(self):
        return self.heightRec(self._root)

    def heightRec(self, cur):
        currHt = 0
        leftHt = 0
        rightHt = 0
        if cur == None:
            currHt = -1
        else:
            leftHt = self.heightRec(cur.getLeft())
            rightHt = self.heightRec(cur.getRight())

            currHt = max(leftHt, rightHt) + 1

        return currHt
            

    def min(self):
        if self._root == None:
            return_val = None
        else:
            return_val = self.minRec(self._root)
        return return_val

    def minRec(self, cur):
        if cur.getLeft() != None:
            min = self.minRec(cur.getLeft())
        else:
            min = cur.getKey()
        return min

    def max(self):
        if self._root == None:
            return_val = None
        else:
            return_val = self.maxRec(self._root)
        return return_val

    def maxRec(self, cur):
        if cur.getRight() != None:
            maxi = cur.getRight()
        else:
            maxi = cur.getKey()
        return maxi

    def balance(self):
        root = self._root
        if self._root == None:
            balance = 1

        else:
            Ht = self.heightRec(root)
            leftHt = self.heightRec(root.getLeft())
            rightHt = self.heightRec(root.getRight())

            dec = abs(leftHt - rightHt)
            if dec == 0:
                balance = 1
            else:
                balance = 1 - dec/Ht

        return balance

    def printLinkedList(self):
        for i in self.linkedL:
            print(i, end = " ")
    
    def cleanLinkedList(self):
        i = self.linkedL.getCount()

        for i in range(0, i):
            self.linkedL.removeFirst()
    
    def preorder(self):
        self.preorderRecurs(self._root)
        self.printLinkedList()

   
    def preorderRecurs(self, cur):
        if cur != None:
            self.linkedL.insertLast(cur.getValue())
            if cur.getLeft() == None and cur.getRight() != None:
                self.preorderRecurs(cur.getRight())
            elif cur.getRight() == None and cur.getLeft() != None:
                self.preorderRecurs(cur.getLeft())
            else:
                self.preorderRecurs(cur.getLeft())
                self.preorderRecurs(cur.getRight())

    def postorder(self):
        self.postorderRecurs(self._root)
        self.printLinkedList()

    def postorderRecurs(self, cur):
        if cur != None:
            self.postorderRecurs(cur.getLeft())
            self.postorderRecurs(cur.getRight())
            self.linkedL.insertLast(cur.getValue())

    def inorder(self):
        self.inorderRecurs(self._root)
        self.printLinkedList()

    def inorderRecurs(self,cur):
        if cur != None:
            self.inorderRecurs(cur.getLeft())
            self.linkedL.insertLast(cur.getValue())
            self.inorderRecurs(cur.getRight())

        


class DSATreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return("Key: " + str(self.key) + " Value: " + str(self.value))

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def setLeft(self, newLeft):
        self.leftChild = newLeft

    def setRight(self, newRight):
        self.rightChild = newRight





def CheckWorking():
    test.inorder()
    test.cleanLinkedList()
    print("\n")
    test.preorder()
    test.cleanLinkedList()
    print("\n")
    test.postorder()
    test.cleanLinkedList()
    print("\n")
    print(test.balance())
    print(test.height())
    print(test.min())
    print(test.max())


if __name__ == "__main__":
    test = DSASearchTree()
    #Testing With Lecture example Tree
    test.insert("D","D")
    test.insert("B","B")
    test.insert("A","A")
    test.insert("C","C")
    test.insert("F","F")
    test.insert("E","E")
    test.insert("G","G")
    CheckWorking()


    print("\n\n Deleting A\n\n")
    test.delete("A")
    CheckWorking()
    print("\n\n Deleting B\n\n")
    test.delete("B")
    CheckWorking()
    print("\n\n Deleting C\n\n")
    test.delete("C")
    CheckWorking()
    print("\n\n Deleting D\n\n")
    test.delete("D")
    CheckWorking()
    print("\n\n Deleting E\n\n")
    test.delete("E")
    CheckWorking()
    print("\n\n Deleting F\n\n")
    test.delete("F")
    CheckWorking()
    print("\n\n Deleting G\n\n")
    test.delete("G")
    CheckWorking()

