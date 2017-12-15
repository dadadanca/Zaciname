import functools

class Batoh:
    def __init__(self, kapacita, ulozene_veci):
        if kapacita < 0:
            raise ValueError("Kapacita musi byt vetsi nez 0")
        self.ulozene_veci=ulozene_veci
        self.kapacita=kapacita
    def obsazeno(self):
        return functools.reduce(lambda a,b: a+b, self.ulozene_veci, 0)
    def volno(self):
        return self.kapacita-self.obsazeno()


vsechny_veci= [19, 9, 6, 7, 10, 52, 8, 7, 4, 3, 2, 3, 7, 9]
batoh = Batoh(10, [5])
print(batoh.obsazeno())
print(batoh.volno())

def napln_batoh (batuzek, veci):
    if len(veci)== 0: return batuzek
    if veci[0] > batuzek.volno():
        return napln_batoh(batuzek, veci[1::])
    else:
        novy_batoh = Batoh(batuzek.kapacita, batuzek.ulozene_veci+[veci[0]])
        kandidat1 = napln_batoh(novy_batoh, veci[1::])
        novy_druhy_batoh = Batoh(batuzek.kapacita, batuzek.ulozene_veci)
        kandidat2 = napln_batoh(novy_druhy_batoh, veci[1::])
        if kandidat1.obsazeno()>kandidat2.obsazeno():
            return kandidat1
        else: return kandidat2

batoh = Batoh(17, [])
vysledny_batoh=napln_batoh(batoh, vsechny_veci)
print(vysledny_batoh.obsazeno())
print(vysledny_batoh.ulozene_veci)



