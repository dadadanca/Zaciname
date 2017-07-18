class Firma:
    def __init__(self, nazev):
        self.nazev = nazev
        self.zamestnanci = []
        self.reditel = None

    def LzePrijmout(self,k):
        for z in self.zamestnanci:
            if z.role==k.role:
                return False
        return True

    def najmi(self, z):
        self.zamestnanci.append(z)

    def propust(self, z):
        self.zamestnanci.remove(z)
        if self.reditel==z:
            self.reditel=None

    def vypisZamestnance(self):
        for z in self.zamestnanci:
            print(z)

class Zamestnanec:
    def __init__(self, jmeno, role):
        self.jmeno = jmeno
        self.role = role[0].upper() + role[1::]

    def __str__(self):
        return "%s - %s"%(self.jmeno,self.role)

jb = Firma("JetBrains")
e = Zamestnanec("Eda", "skladnik")
jb.najmi(e)
jb.najmi(Zamestnanec("Alice", "programatorka"))
jb.najmi(Zamestnanec("David", "kuchar"))

jb.reditel = e
jb.vypisZamestnance()
print(jb.LzePrijmout(Zamestnanec("Paja", "pravnicka")))
print(jb.LzePrijmout(Zamestnanec("Paja", "programatorka")))
jb.propust(e)



