class Firma:
    def __init__(self, nazev):
        self.nazev = nazev
        self.zamestnanci = []
        self.reditel = None

    def najmi(self, z):
        self.zamestnanci.append(z)

    def propust(self, z):
        self.zamestnanci.remove(z)

class Zamestnanec:
    def __init__(self, jmeno, role):
        self.jmeno = jmeno
        self.role = role[0].upper() + role[1::]

jb = Firma("JetBrains")
e = Zamestnanec("Eda", "skladnik")
jb.najmi(e)
jb.najmi(Zamestnanec("Alice", "programatorka"))
jb.najmi(Zamestnanec("David", "kuchar"))

jb.reditel = e


