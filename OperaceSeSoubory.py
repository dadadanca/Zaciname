from ZvetsovaciFunkce import ZvetsiTotoSlovo
# importuju funkci z jineho souboru

NazevSouboruZadani = input("Dej sem věty!")
NazevSouboruVysledku = input("Kam to dáme?")

SouborZadani = open(NazevSouboruZadani, "r")
SouborVysledku = open(NazevSouboruVysledku, "w")

SouborVysledku.write("Haloooo\n")
SouborVysledku.write("Je tam nekdoooo\n")
# \n novy radek v souboru

obsah = SouborZadani.readlines()
for radek in obsah:
    slova = radek.split(" ")
    slova = map(ZvetsiTotoSlovo, slova)
    velkaSlova = list(slova)
    ZvetsenyRadek = (" ".join(velkaSlova))
    SouborVysledku.write(ZvetsenyRadek)

SouborZadani.close()
SouborVysledku.close()
