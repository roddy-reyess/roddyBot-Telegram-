#-*- coding: utf8 -*-
class character():
    """
    Classe que controla els personatges.
    """

    def __init__(self):
        self.charDict = {
        "nombre" : "",
        "edad" : "",
        "clase" : "",
        "apariencia" : "",
        "personalidad" : "",
        "historia" : ""
        }

    def charCheck(self):
        missingFields = []
        for x,y in self.charDict.items():
            if y != "":
                pass
            elif y == "":
                missingFields.append(x)
        return missingFields

    def addField(self, definer, text):
        if definer in self.charDict:
            self.charDict[definer] = text

    def removeAllFields(self):
        for x,y in self.charDict.items():
            self.charDict[x] = ""
            print(self.charDict[x])
    def checkFileContent(self,file_tocheck):
        charDoc = open(str(file_tocheck), 'r')
        doc_contents = charDoc.readlines()[1:]
        content = []
        for i in doc_contents:
            content = i.split(";")
        return content

    def saveCharVal(self,user_file):
            charDoc = open(str(user_file)+".txt", 'a')
            charDoc.write(self.charDict["nombre"]+";")
            charDoc.write(self.charDict["edad"]+";")
            charDoc.write(self.charDict["clase"]+";")
            charDoc.write(self.charDict["apariencia"]+";")
            charDoc.write(self.charDict["personalidad"]+";")
            charDoc.write(self.charDict["historia"]+"\n")
            charDoc.close()
