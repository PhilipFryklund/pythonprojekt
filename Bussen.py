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

# ------------------------- Funktionsdefinitioner ---------------------------- #
buss = []

def plockaUpp():
    if len(buss) < 25:
        namn = input("Ange namn: ")
        ålder = int(input("Ange ålder: "))
        person = Person(namn, ålder)
        buss.append(person)
        print(f"{namn} har stigit på bussen.")
    else:
        print("Bussen är full.")

def gåAv():
    namn = input("Ange namn på passageraren som ska gå av: ")
    for person in buss:
        if person.getNamn() == namn:
            buss.remove(person)
            print(f"{namn} har gått av bussen.")
            return
    print(f"{namn} finns inte på bussen.")

def skrivUt():
    if buss:
        for person in buss:
            print(person)
    else:
        print("Inga passagerare på bussen.")

def sammanlagdÅlder():
    total = sum(person.getÅlder() for person in buss)
    print(f"Sammanlagd ålder: {total} år.")
    return total

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder():
    return

# Skriver ut personen som är äldst på bussen.
def äldst():
    return

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    return

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare(åldersSpann):
    return

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    return

# ------------------------------ Huvudprogram --------------------------------- #
# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            plockaUpp()
        elif menyVal == "2":
            gåAv()
        elif menyVal == "3":
            skrivUt()
        elif menyVal == "4":
            sammanlagdÅlder()
        elif menyVal == "5":
            medelÅlder()
        elif menyVal == "6":
            äldst()
        elif menyVal == "7":
            busSort()
        elif menyVal == "8":
            hittaPassagerare()
        elif menyVal == "9":
            peta()
        elif menyVal == "q":
            print("Bussen körde av vägen pga ishalka")
        else:
            print("Ogiltigt val. Försök igen.")
    
    # Bussen visas efter att programmet avslutas.
    print(
    """
                                           _____________
                                         _/_|[][][][][] | - -
                                        ( SL - Lokalbuss| - -
                                        =--OO-------OO--=
    """)

main()
