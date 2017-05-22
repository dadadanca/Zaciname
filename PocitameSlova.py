import functools
JmenoPocitanehoSouboru = input("Jak se jmenuje tvuj vychozi soubor?")

PocitanySoubor = open(JmenoPocitanehoSouboru, "r")
# acc = 0
# for radek in PocitanySoubor:
#     DelkaRadku = len(radek)
#     acc = acc + DelkaRadku - 1

def spoctiPocetSlovNaRadku(r):
    print(r.split(" "))
    if len(r.strip(" \n"))>0:
        return len(r.split(" "))
    else:
        return 0

DelkyRadku = map(lambda r: spoctiPocetSlovNaRadku(r), PocitanySoubor)
acc = functools.reduce(lambda a,v: a+v, DelkyRadku, 0)

print(acc)






PocitanySoubor.close()
