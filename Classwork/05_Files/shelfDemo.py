from shelve import *

fList = ["Mavericks","Falcons"]
def saveFile(listIn):
    listFile = open("listFile")
    listFile["Yippee"] = listIn
    listFile.close()
    
def loadFile():
    listFile = open("listFile")
    list2 = listFile["Yippee"]
    listFile.close()
    return list2
    
saveFile(fList)
print(loadFile())
    