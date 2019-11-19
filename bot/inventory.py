#-*- coding: utf8 -*-
class inventory():
    """Classe que controla l'inventari"""
    def __init__(self):
        self.objetos = []

    def showInventory(self, invFichero):
        invFile = open(invFichero,'r')
        doc_contents = charDoc.readlines()[1:]
        content = []
        for i in doc_contents:
            content = i.split(";")
        return content

    def addtoInventory(self,invFichero,object,description,type):
        exists = checkObject(invFichero,object)
        if exists == False:
        invFile = open(invFichero,'a')
        invFile.write(object + " ; " + description + " ; " + type)
        invFile.close()

    def checkObject(self,invFichero,object):
        invFile = open(invFichero,'r')
        doc_contents = charDoc.readlines()[1:]
        exists = False
        for i in doc_contents:
            if object in i:
                exists = True
        invFile.close()
        return exists
