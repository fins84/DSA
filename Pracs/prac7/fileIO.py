import DSAHashTable as Hash

class FileIO():
    def __init__(self):
        self.HashTable = Hash.DSAHashTable(100)


    def readFile(self):
        try:
            filename = input("Name of file: ")
            with open(filename, "r") as f:
                for lines in f:
                    lett = lines.split(",")
                    try:
                        self.HashTable.put(lett[0], lett[1])
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e, "Error reading file")



test = FileIO()
test.readFile()
print(test.HashTable.count)