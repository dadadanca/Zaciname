def spojJmeno (firstName, lastName):
    return firstName+" "+lastName
# zotaveni z chyb: uzivatel zada prazdne jmeno nebo prijmeni
def spojJmeno1 (firstName, lastName):
    if firstName == "":
        return lastName
    if lastName == "":
        return firstName
    return firstName+" "+lastName

#vraceni chyboveho kodu: uzivateli nahlasim chybu
def spojJmeno2 (firstName, lastName):
    if firstName == "":
        return "error1"
    if lastName == "":
        return "error2"
    return firstName+" "+lastName

class FirstNameError(ValueError):
    pass

class LastNameError(ValueError):
    pass

#vyhazovani vyjimek: odchytim si chybu uzivatele
def spojJmeno3 (firstName, lastName):
    if firstName == "":
        raise FirstNameError
    if lastName == "":
        raise LastNameError
    return firstName+" "+lastName

jmeno=input("Zadej jmeno")
prijmeni=input("Zadej prijmeni")

vysledek=spojJmeno2(jmeno,prijmeni)

if vysledek == "error1":print("Chybne jmeno")
elif vysledek == "error2":print("Chybne prijmeni")
else:print(vysledek)

try:
    vysledek=spojJmeno3(jmeno,prijmeni)
except FirstNameError:
    print("Chybne jmeno")
except LastNameError:
    print("Chybne prijmeni")

import sys
sys.exit(43)