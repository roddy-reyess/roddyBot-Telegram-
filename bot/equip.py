#-*- coding: utf8 -*-
class equip(object):
    """docstring for equip."""

    def __init__(self):
        self.arrayEq = []

    def createEqDict(self,cid):
        eqDict = {
        "cid" = str(cid),
        "arma" = "",
        "armadura" = ""
        }
        self.arrayEq.append(eqDict)

    def checkCid(self, cid):
        exists = False;
        for i in self.arrayEq:
            if i["cid"] == cid:
                exists = True
        return exists

    def addField(self, cid, definer, text):
        for i in range(len(self.arrayChars)):
            if self.arrayChars[i]["cid"] == cid:
                self.arrayChars[i][definer] = str(text)
        
