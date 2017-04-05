from random import randrange
# vrati mi nahodne cislo / import knihovny

import sys
# potrebne pro zpracovani zadanych parametru v cernobilem programovani

if len(sys.argv)== 3:
    JmenoHrace = sys.argv [1]
    JmenoPocitace = sys.argv [2]
else:
    JmenoHrace = "Hrac"
    JmenoPocitace = "Pocitac"

moznosti = ["kamen", "nuzky", "papir"]

HracuvText = input("Zvol: ")
HracovoSkore = 0
PocitacovoSkore = 0
while HracuvText!= "":
    d = int(HracuvText)
    HracovaVolba = d % 3
    print("Zvolil jste: %s"%moznosti[HracovaVolba])

    PocitacovaVolba = randrange(0,3)
    print("Pocitac zvolil: %s"%moznosti[PocitacovaVolba])

    if HracovaVolba == PocitacovaVolba:
        print("Remiza ")
    elif (HracovaVolba + 1)%3 == PocitacovaVolba:
        HracovoSkore = HracovoSkore + 1
        print("Vyhral jsi!!")
    else:
        PocitacovoSkore = PocitacovoSkore + 1
        print("Prohral jsi!")

    print("Skore: %s:%s %s:%s"%(JmenoHrace, JmenoPocitace, HracovoSkore,PocitacovoSkore))
    HracuvText = input("Zvol: ")

#     Vzdycky vyhraju


