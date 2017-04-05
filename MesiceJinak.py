# parcialni aplikace funkce
from enum import Enum
class Mesice(Enum):
    leden, unor, brezen, duben, kveten, cerven, cervenec, srpen, zari, rijen, listopad, prosinec = range(1, 13)

import functools

def vypoctiSlozeneUroky (urok, castka, vklady={}):
    aktualniCastka = castka
    for mesic in Mesice:
        if vklady.__contains__(mesic):
            def soucetMesicnichVkladu (mesicniVklady):
                sum = 0
                for x in mesicniVklady:
                    sum = sum + x
                return sum

            def soucetMesicnichVkladu2 (mesicniVklady):
                return functools.reduce(lambda acc, vklad: acc + vklad, mesicniVklady)

            aktualniCastka = aktualniCastka + soucetMesicnichVkladu2(vklady[mesic])

        aktualniCastka = aktualniCastka *(1 + urok/100/12)
        aktualniCastka = round(aktualniCastka, 2)
        # print("Castka na uctu v %s je: %s."%(mesic, aktualniCastka))
    return aktualniCastka

def vypoctiSlozeneUrokyBezVkladu (urok, castka):
    return vypoctiSlozeneUroky(urok, castka,{})

vklady = {
    Mesice.leden: [20],
    Mesice.brezen: [-10, -20],
    Mesice.kveten: [30, 70],
    Mesice.zari: [-20, 80]
}
print(vypoctiSlozeneUroky(5,100))

from functools import partial
VypoctiUrokyNaBU = partial(vypoctiSlozeneUroky, 6)
VypoctiUrokyNaSU = partial(vypoctiSlozeneUroky, 12)

print(VypoctiUrokyNaBU(100))
print(VypoctiUrokyNaSU(100))


def soucet (a,b):
    return a + b

print(soucet(10,30))


OJednoVyssi = partial(soucet,1)
print(OJednoVyssi(39))

