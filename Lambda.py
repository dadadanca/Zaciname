zamestnanci = [
    {"jmeno": "Franta", "vek": 20,"zena": False, "plat": 100},
    {"jmeno": "Alice", "vek": 28, "zena": True, "plat": 125},
    {"jmeno": "Pepa", "vek": 33, "zena": False, "plat": 233},
    {"jmeno": "Jaja", "vek": 35, "zena": True, "plat": 347}]


def jeZena (z):
    return z["zena"]
# def jeMuz (z):
#     return not jeZena(z)

zeny = filter(jeZena, zamestnanci)
muzi = filter(lambda z: not jeZena(z), zamestnanci)

import functools

def soucetPlatu (acc, z):
    return acc + z["plat"]

platZeny = functools.reduce(soucetPlatu, zeny, 0)
platMuzi = functools.reduce(soucetPlatu, muzi, 0)

if platZeny > platMuzi:
    print("Zeny maji navrch")
elif platZeny==platMuzi:
    print("Maji stejne")
else:
    print ("Muzi maji vic")

print(platZeny)
print(platMuzi)
