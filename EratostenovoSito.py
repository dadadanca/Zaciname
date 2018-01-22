Sito = []
def je_prvocislo(cislo):
    for a in Sito:
        if cislo%a == 0:
            return False
    return True

for x in range(2,10):
    if(je_prvocislo(x)):
        Sito.append(x)

print(Sito)

class Prvocislo:
    def __init__(self, h):
        self.hodnota = h
        self.dalsi = None
    def je_prvocislo(self, x):
        if x%self.hodnota != 0:
            if self.dalsi== None:
                self.dalsi = Prvocislo(x)
                return True
            else:
                return self.dalsi.je_prvocislo(x)
        else:
            return False
    def seznamuj(self):
        if self.dalsi == None:
            return "%s"%self.hodnota
        else:return "%s, "%self.hodnota + self.dalsi.seznamuj()

Prvni = Prvocislo(2)

for x in range(3,100):
    vysledek = Prvni.je_prvocislo(x)
    if vysledek: print("%s je prvocislo"%x)
    else: print("%s neni prvocislo"%x)

print(Prvni.seznamuj())

