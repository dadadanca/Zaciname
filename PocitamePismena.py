import functools
JmenoPocitanehoSouboru = input("Jak se jmenuje tvuj vychozi soubor?")

PocitanySoubor = open(JmenoPocitanehoSouboru, "r")
# acc = 0
# for radek in PocitanySoubor:
#     DelkaRadku = len(radek)
#     acc = acc + DelkaRadku - 1

DelkyRadku = map(lambda r: len(r)-1, PocitanySoubor)
acc = functools.reduce(lambda a,v: a+v, DelkyRadku, 0)

print(acc)






PocitanySoubor.close()
