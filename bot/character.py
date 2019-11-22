#-*- coding: utf8 -*-
class character():
    """
    Classe que controla els personatges.
    """

    def __init__(self):
        self.arrayChars = []

    def createPjDict(self, cid):
        charDict = {
        "cid" : str(cid),
        "nombre" : "",
        "edad" : "",
        "clase" : "",
        "apariencia" : "",
        "personalidad" : "",
        "historia" : ""
        }
        self.arrayChars.append(charDict)

    def charCheck(self, cid):
        missingFields = []
        for i in self.arrayChars:
            if cid == i["cid"]:
                for x,y in i.items():
                    if y == "":
                        missingFields.append(x)
        return missingFields
    def addField(self, cid, definer, text):
        for i in range(len(self.arrayChars)):
            if self.arrayChars[i]["cid"] == cid:
                print("entra")
                self.arrayChars[i][definer] = str(text)
        print(self.arrayChars)
    def removeAllFields(self, cid):
        for i in range(len(self.arrayChars)):
            if self.arrayChars[i]["cid"] == cid:
                for x,y in self.arrayChars[i]:
                    self.charDict[x] = ""
        
    def checkFileContent(self,file_tocheck):
        charDoc = open(str(file_tocheck), 'r')
        doc_contents = charDoc.readlines()[1:]
        content = []
        for i in doc_contents:
            content = i.split(";")
        return content

    def saveCharVal(self,user_file, cid):
            charDoc = open(str(user_file)+".txt", 'a')
            for i in self.arrayChars:
                if i["cid"] == cid:
                    charDoc.write(i["nombre"]+";")
                    charDoc.write(i["edad"]+";")
                    charDoc.write(i["clase"]+";")
                    charDoc.write(i["apariencia"]+";")
                    charDoc.write(i["personalidad"]+";")
                    charDoc.write(i["historia"]+"\n")
                    charDoc.close()
