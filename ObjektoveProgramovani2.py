class Zivocich:
    pass

o = Zivocich()
o.name = "Franta"


class Zvire:

    def __init__(self, vek):
        self.vek = vek

    def projevse (self):
        pass

class DomaciMazlicek(Zvire):
    def __init__(self, jmeno, vek):
        super().__init__(vek)
        self.jmeno = jmeno

class Pes(DomaciMazlicek):
    def projevse(self):
        print("HAF")

class Kocka(DomaciMazlicek):
    def projevse(self):
        print("MNAU")


Alik=Pes("Alik",3)
Alik.projevse()

Micka=Kocka("Micka",6)
Micka.projevse()

Zviratka=[Pes("Azor",2), Kocka("Helena",1), Kocka("Alena",4)]
for zviratko in Zviratka:
    zviratko.projevse()

class ZlyPes(Pes):
    def __init__(self, jmeno, vek, velikost):
        super().__init__(jmeno,vek)
        self.velikost = velikost
    def projevse(self):
        print("zacatek")
        for i in range(1, self.velikost):
            super().projevse()
        print("konec")


Brucoun=ZlyPes("Brucoun", 10, 6)
Brucoun.projevse()
