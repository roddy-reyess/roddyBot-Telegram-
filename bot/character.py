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
    def checkFileContent(file_tocheck):
        charDoc = open(str(file_tocheck), 'r')
        doc_contents = charDoc.readlines()[1:]
        content = []
        for i in doc_contents:
            content = i.split(";")
        return content

        def saveCharVal(user_file):
            charDoc = open(str(user_file)+".txt", 'a')
            charDoc.write(pj.charDict["nombre"]+";")
            charDoc.write(pj.charDict["edad"]+";")
            charDoc.write(pj.charDict["clase"]+";")
            charDoc.write(pj.charDict["apariencia"]+";")
            charDoc.write(pj.charDict["personalidad"]+";")
            charDoc.write(pj.charDict["historia"]+"\n")
            charDoc.close()
