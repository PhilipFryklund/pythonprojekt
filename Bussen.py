# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare:
Datum:
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
#Importera random
import random as rand

#Klassdefinitioner
class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def __str__(self):
        return f"{self.namn}, {self.ålder} år gammal."

    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder