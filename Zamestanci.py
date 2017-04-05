zamestnanci = [
    {"jmeno": "Franta", "vek": 20,"zena": False},
    {"jmeno": "Alice", "vek": 28, "zena": True},
    {"jmeno": "Pepa", "vek": 33, "zena": False},
    {"jmeno": "Jaja", "vek": 35, "zena": True}]

def jeZena (z):
    return z["zena"]

zeny = filter(jeZena, zamestnanci)
import functools

def starsiZamestnanec (acc, z):
    if z["vek"] > acc["vek"]:
        return z
    else:
        return acc

nejstarsiZena = functools.reduce(starsiZamestnanec, zeny)

print(nejstarsiZena["jmeno"])
