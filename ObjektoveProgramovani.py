class Pes:

    def __init__(self, jmeno, vek):
        self.name = jmeno
        self.alter = vek

    def mluv(self):
        stekot = ""
        for i in range(1,self.alter+1):
            stekot+="HAF"
        return stekot

    def narozeniny(self):
        self.alter += 1

MujPes = Pes("Alik",3)

print(MujPes.mluv())

MujPes.narozeniny()
print(MujPes.mluv())
