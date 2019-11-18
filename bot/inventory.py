#-*- coding: utf8 -*-
class inventory():
    """Classe que controla l'inventari"""
    def __init__(self, inventoryFile):
        self.invFichero = inventoryFile
        self.objetos = []

    def showInventory():
        invFile = open(self.invFichero,'r')
        doc_contents = charDoc.readlines()[1:]
        content = []
        for i in doc_contents:
            content = i.split(";")
        return content
    def addtoInventory():
        pass
