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
