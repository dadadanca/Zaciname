import re

jmena=["Alice", "Zuzana", "David"]

def osloveni(seznam_jmen):
    spojene_carkou = ", ".join(seznam_jmen[:-1])
    return "Dear " + " and ".join([spojene_carkou, seznam_jmen[-1]])

print(osloveni(jmena))

slova=["FraWWnta Vomacka", "David", "Franta vomacka", "Julie Nejedla", "Anna Marie Vomackova", "  ferda "]
def je_jmeno(x):
    if " " in x.strip():
        rozdelena_jmena = x.split(" ")
        for a in rozdelena_jmena:
            if a[0].isupper(): continue
            else: return False
        return True
    else: return False

jmena = filter(je_jmeno, slova)
print(list(jmena))

def je_jmenoRE (z):
    overeni=re.fullmatch(r"[A-Z][a-z]+( [A-Z][a-z]+)+", z)
    return overeni!=None

jmena=filter(je_jmenoRE, slova)
print(list(jmena))

