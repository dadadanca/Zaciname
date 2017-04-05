
zamestnanci = [
    {"Jmeno": "Vasek", "vek": 30, "plat": 100, "zena": False},
    {"Jmeno": "Jana", "vek": 28, "plat": 89, "zena": True},
    {"Jmeno": "Adam", "vek": 35, "plat": 121, "zena": False},
    {"Jmeno": "Lada", "vek": 37, "plat": 112, "zena": True}
]

def jeZena (z):
    return z["zena"]

jenZeny = []
jenMuzi = []

for z in zamestnanci:
    if jeZena(z):
        jenZeny.append(z)
    else:
        jenMuzi.append(z)

print(jenMuzi)
print(jenZeny)

import functools

zeny = list(filter(jeZena,zamestnanci))
muzi = list(filter(lambda z: not jeZena(z), zamestnanci))

print(list(zeny))

def soucetVeku (acc, z):
    return acc + z["vek"]

vekZen = functools.reduce(soucetVeku, zeny,0)
vekMuzu = functools.reduce(soucetVeku, muzi,0)

print(vekZen)
print(vekMuzu)


def soucetPlatu (sum, z):
    return sum + z["plat"]

SoucetPlatuZen = functools.reduce(soucetPlatu, zeny, 0)
SoucetPlatuMuzu = functools.reduce(soucetPlatu, muzi, 0)

print(SoucetPlatuMuzu)
print(SoucetPlatuZen)

if vekMuzu < vekZen:
    print("Muzi jsou mladsi")
elif vekMuzu > vekZen:
    print("Zeny jsou mladsi")
else:
    print("Zeny a muzi jsou stejne stari")


# while??? jak se definuje?? zde se použije
