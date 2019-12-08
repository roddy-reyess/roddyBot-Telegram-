#-*- coding: utf8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
class readBooks():
    """docstring for readBooks."""

    def __init__(self):
        self.booksRead = []
        self.getBooks()

    def getBooks(self):
        for r, d, f in os.walk("assets/libros/"):
            for file in f:
                self.booksRead.append(os.path.join(r,file))

    def readBooks(self, bookName):
        content = ""
        for i in self.booksRead:
            books = i.split("/")
            if bookName.lower() in books[2].lower():
                print("entro")
                new = open(i, 'r')
                doc_contents = new.readlines()
                for z in doc_contents:
                    content += z
        return content
