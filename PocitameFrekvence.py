JmenoPocitanehoSouboru = input("Jak se jmenuje tvuj vychozi soubor?")

PocitanySoubor = open(JmenoPocitanehoSouboru, "r")
frekvence = {}

for radek in PocitanySoubor:
    SlovaNaRadku = radek.strip(" \n").split(" ")
    for slovo in SlovaNaRadku:
        if frekvence.__contains__(slovo):
            hodnota = frekvence[slovo]
            frekvence[slovo] = hodnota+1
        else:
            frekvence[slovo]= 1

print(frekvence)


PocitanySoubor.close()
