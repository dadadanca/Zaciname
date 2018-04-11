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



class Apple:
    def __init__(self, colour, weight, origin, kind):
        self.colour = colour
        self.weight = weight
        self.origin = origin
        self.kind = kind

    def __str__(self):
        return "Toto je {} jablko, ktere vazi {} gramu, pochazi z {} a je {}".format(self.colour, self.weight, self.origin, self.kind)

cervenacek=Apple("cervena", 2, "CZ", "skvrnite")
print(cervenacek)

import math
class Circle:
    def __init__(self, polomer):
        self.polomer = polomer
    def obsah(self):
        return math.pi*self.polomer*self.polomer

krouzek=Circle(4)
print(krouzek.obsah())
