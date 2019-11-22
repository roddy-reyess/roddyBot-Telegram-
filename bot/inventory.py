#-*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class inventory():
    """Classe que controla l'inventari"""
    def __init__(self):
        self.invObjects = []

    def addtoInventory(self,invFichero,object,description,type):
        invFile = open(str(invFichero),'a')
        invFile.write(object + " ; " + description + " ; " + type + "\n")
        invFile.close()

    def checkObject(self,invFichero,object):
        invFile = open(str(invFichero),'r')
        doc_contents = invFile.readlines()[1:]
        exists = False
        for i in doc_contents:
            if object in i:
                exists = True
        invFile.close()
        return exists

    def showInv(self, invFichero):
        self.invObjects = []
        invFile = open(str(invFichero),'r')
        doc_contents = invFile.readlines()[1:]
        for i in doc_contents:
            content  = i.split(";")
            dicContent = {
            "objeto" : str(content[0]),
            "descripcion" : str(content[1]),
            "tipo" : str(content[2])
            }
            self.invObjects.append(dicContent)
        return self.invObjects
