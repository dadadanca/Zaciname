class Zvire:
    standardniPocetNohou = 4

class Pes(Zvire):
    pocetPsu=0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocetNohou = Pes.standardniPocetNohou
        # Pes.pocetPsu+=1

    def __repr__(self):
        return "Muj pejsek, ktery se jmenuje %s"%self.jmeno

    def __add__(self, other):
        return Pes(self.jmeno+other.jmeno)

    def __mul__(self, other):
        return [Pes("Stene %s"%x) for x in range(other)]

    def __eq__(self, other):
        return self.jmeno == other.jmeno and self.pocetNohou == other.pocetNohou
    # porovnavame vlastnosti objektu pro operator ==


Marcel=Pes("Marcel")
Olga=Pes("Olga")
Olga.pocetNohou = 5

print(Pes.pocetPsu)
print(Marcel)
# repr - magicka metoda (vypise Marcela)
print(Olga)
print(Marcel+Olga)
# add - magicka metoda (secte dva pejsky - vytvori novyho)
print(Marcel*3)

Azor1=Pes("Azor")
Azor2=Pes("Azor")
Azor3=Azor1

print(Azor1 is Azor2)
# porovnavame sipky na objekty
print(Azor1==Azor2)

