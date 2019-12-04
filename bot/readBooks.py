#-*- coding: utf8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
class readBooks(object):
    """docstring for readBooks."""

    def __init__(self):
        self.booksRead = []
        self.getBooks()

    def getBooks(self):
        for r, d, f in os.walk("assets/libros/"):
            for file in f:
                self.booksRead.append(os.path.join(r,file))
        print(self.booksRead)
    def readBooks(self, bookName):
        book = ""
        for i in self.booksRead:

            if i.find(bookName) == -1:
                print "entro"
                new = open(i, 'r')
                doc_contents = new.readlines()
                for z in doc_contents:
                    book += z
        return book
