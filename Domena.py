class Typ_zvirete:
    def __init__(self, nazev):
        self.nazev = nazev

kocka = Typ_zvirete("Kočka")
pes = Typ_zvirete("Pes")
kun = Typ_zvirete("Kun")

class Zvire:
    def __init__(self, jmeno, druh, hmotnost, vek):
        self.jmeno = jmeno
        self.druh = druh
        self.anamneza = ""
        self.majitel = None
        self.hmotnost = hmotnost
        self.vek = vek
    def __str__(self):
        return self.jmeno + " vek:{} hmotnost:{}".format(self.vek, self.hmotnost)

class Majitel:
    def __init__(self, jmeno_majitele, telefon, adresa):
        self.jmeno = jmeno_majitele
        self.telefon = telefon
        self.adresa = adresa
        self._zviratka = []

    def pridej_zvire(self, zvire):
        self._zviratka.append(zvire)

    def odeber_zvire(self, zvire):
        self._zviratka.remove(zvire)

    def Karta_majitele (self):
        return """Jmeno: {}
Tel.: {}
Zviratka: {}""".format(self.jmeno, self.telefon, self._zviratka)

class Navsteva:
    def __init__(self, datum, zviratko, zaznam):
        self.datum = datum
        self.zviratko = zviratko
        self.poznamky = zaznam

class Faktura:
    def __init__(self, majitel, navsteva, poplatek):
        self.majitel = majitel
        self.navsteva = navsteva
        self.castka = poplatek


Micka = Zvire("Micka", kocka, 5, 7)
Vasek = Majitel("Vaclav", "123456", "Kouty 14")
Vasek.pridej_zvire(Micka)
Vasek.pridej_zvire(Zvire("Alik", pes, 10, 2))
Vasek.pridej_zvire(Zvire("Ferda", kun, 300, 15))
Vasek.pridej_zvire(Zvire("Saryk", pes, 25, 12))
Vasek.pridej_zvire(Zvire("Semik", kun, 220, 1))
# print(Vasek.Karta_majitele())


def MergeSort (zvirata, porovnavac):
    if len(zvirata)== 1:
        return zvirata

    pulka_seznamu = len(zvirata)//2
    setridena_prvni_cast = MergeSort(zvirata[0:pulka_seznamu], porovnavac)
    setridena_druha_cast = MergeSort(zvirata[pulka_seznamu::], porovnavac)

    index_prvni_cast = 0
    index_druha_cast = 0
    vysledny_setrideny_seznam = []

    while index_prvni_cast < len(setridena_prvni_cast) and index_druha_cast < len(setridena_druha_cast):
        if porovnavac(setridena_prvni_cast[index_prvni_cast], setridena_druha_cast[index_druha_cast]):
            vysledny_setrideny_seznam.append(setridena_prvni_cast[index_prvni_cast])
            index_prvni_cast +=1
        else:
            vysledny_setrideny_seznam.append(setridena_druha_cast[index_druha_cast])
            index_druha_cast += 1

    if index_prvni_cast < len(setridena_prvni_cast):
        for x in setridena_prvni_cast[index_prvni_cast::]:
            vysledny_setrideny_seznam.append(x)

    if index_druha_cast < len(setridena_druha_cast):
        for x in setridena_druha_cast[index_druha_cast::]:
            vysledny_setrideny_seznam.append(x)

    return vysledny_setrideny_seznam

vekovyPorovnavac = lambda z1, z2: z1.vek < z2.vek

print("Podle veku")
for z in MergeSort(Vasek._zviratka, vekovyPorovnavac):
    print(z)

hmotnostniPorovnavac = lambda z1, z2: z1.hmotnost < z2.hmotnost

print("Podle hmotnosti")
for z in MergeSort(Vasek._zviratka, hmotnostniPorovnavac):
    print(z)