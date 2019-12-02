#-*- coding: utf8 -*-
class equip(object):
    """docstring for equip."""

    def __init__(self):
        self.arrayEq = []

    def createEqDict(self,cid):
        eqDict = {
        "cid" : str(cid),
        "arma" : "",
        "armadura" : ""
        }
        self.arrayEq.append(eqDict)

    def checkCid(self, cid):
        exists = False;
        for i in self.arrayEq:
            if i["cid"] == cid:
                exists = True
        return exists

    def addField(self, cid, definer, text):
        for i in range(len(self.arrayEq)):
            if self.arrayEq[i]["cid"] == cid:
                self.arrayEq[i][definer] = str(text)

    def checkFields(self, cid):
        missingFields = []
        for i in self.arrayEq:
            if cid == i["cid"]:
                for x,y in i.items():
                    if y == "":
                        missingFields.append(x)
        return missingFields

    def showEq(self, cid):
        for i in self.arrayEq:
            if cid == i["cid"]:
                return i
