a= int(input("Kolik mas bodu? "))

if a<10:
    print("Mas malo bodu a koncis")
if a>=10:
    print("Ziskala jsi min pocet bodu a pokracujes ve hre")


b= int(input("Kolik mas bodu? "))

if b<11:
    print("Mas malo bodu a koncis")
if b>9 and b<26:
    print("Ziskala jsi min pocet bodu a pokracujes ve hre")
if b>25:
    print("Vyhrala jsi")

c=int(input("Zadej prvni cislo:"))
d=int(input("Zadej druhe cislo:"))

print(c%d)
print(c//d)

