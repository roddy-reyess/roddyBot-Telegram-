#-*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class object():
    """docstring for object."""

    def __init__(self):
        self.objectArmas = []
        self.objectArmaduras = []
        self.objectColeccionables = []
        self.objectLibros = []
        self.fillArmas()
        self.fillArmaduras()
        self.fillColeccionables()
        self.fillLibros()

    def fillArmas(self):
        weaponFile = open("assets/Armas.txt",'r')
        doc_contents = weaponFile.readlines()[1:]
        for i in doc_contents:
            content = i.split(";")
            content[1] = content[1].replace('\n','')
            dicContent = {
            "objeto" : str(content[0]),
            "descripcion" : str(content[1]),
            "tipo" : "[Arma]"
            }
            self.objectArmas.append(dicContent)


    def fillArmaduras(self):
        armorFile = open("assets/Armaduras.txt",'r')
        doc_contents = armorFile.readlines()[1:]
        for i in doc_contents:
            content = i.split(";")
            content[1] = content[1].replace('\n','')
            dicContent = {
            "objeto" : str(content[0]),
            "descripcion" : str(content[1]),
            "tipo" : "[Armadura]"
            }
            self.objectArmaduras.append(dicContent)

    def fillColeccionables(self):
        objectFile = open("assets/Objetos.txt",'r')
        doc_contents = objectFile.readlines()[1:]
        for i in doc_contents:
            content = i.split(";")
            content[1] = content[1].replace('\n','')
            dicContent = {
            "objeto" : str(content[0]),
            "descripcion" : str(content[1]),
            "tipo" : "[Coleccionable]"
            }
            self.objectColeccionables.append(dicContent)

    def fillLibros(self):
        bookFile = open("assets/Libros.txt",'r')
        doc_contents = bookFile.readlines()[1:]
        for i in doc_contents:
            content = i.split(";")
            content[1] = content[1].replace('\n','')
            dicContent = {
            "objeto" : str(content[0]),
            "descripcion" : str(content[1]),
            "tipo" : "[Libro]"
            }
            self.objectLibros.append(dicContent)
