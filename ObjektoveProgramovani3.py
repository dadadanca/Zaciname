class Kniha:
    def __init__(self, autor, titul, pocet_stran):
        self.autor = autor
        self.autor.pridej_dilo(self)
        self.titul = titul
        self.pocet_stran = pocet_stran
    def __str__(self):
        return self.autor.__str__() + " - " + self.titul

class Autor:
    def __init__(self, jmeno_autora, datum_narozeni):
        self.jmeno = jmeno_autora
        self.datum = datum_narozeni
        self._dila = []
    def __str__(self):
        return self.jmeno
    def dila(self):
        return self._dila
    def pridej_dilo(self, kniha):
        self._dila.append(kniha)

class Pokoj:
    def __init__(self, nazev_pokoje, nazvy_lokaci):
        self.nazev = nazev_pokoje
        self.lokace_pokoje = []
        for x in nazvy_lokaci:
            self.lokace_pokoje.append(Lokace(x))

    def najdi_lokaci(self, nazev):
        for x in self.lokace_pokoje:
            if x.nazev == nazev:
                return x
        return None


class Lokace:
    def __init__(self, nazev):
        self.nazev = nazev
        self._knihy = []
    def umisti_knihu(self, kniha):
        self._knihy.append(kniha)
    def ulozene_knihy(self):
        return self._knihy

Pokoj1=Pokoj("Loznice", ["nocni_stolek", "knihovna"])


Autor1=Autor("Vaclav", "3.3.1990")
Kniha1=Kniha(Autor1, "Krtecek", 10)
# Autor1.pridej_dilo(Kniha1)
Kniha2=Kniha(Autor1, "Papouch", 20)
# Autor1.pridej_dilo(Kniha2)
Autor2=Autor("Dana", "5.5.1988")
Kniha3=Kniha(Autor2, "Jelinek", 30)

Lokace1=Pokoj1.najdi_lokaci("nocni_stolek")
Lokace1.umisti_knihu(Kniha1)
Lokace1.umisti_knihu(Kniha3)

for x in Pokoj1.najdi_lokaci("nocni_stolek").ulozene_knihy():
    print(x.autor)

print("Autorova dila:")
for x in Autor1.dila():
    print(x)

for x in Autor2.dila():
    print(x)



# knihy = [Kniha("Vaclav", "Krtecek1", 10), Kniha("Vaclav", "Krtecek2", 10), Kniha("Vaclav", "Krtecek3", 10), Kniha("Vaclav", "Krtecek4", 10)]
