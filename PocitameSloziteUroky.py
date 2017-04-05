import functools

def vypoctiSlozeneUroky (urok, castka, vklady):
    aktualniCastka = castka
    for mesic in range (1,13):
        if vklady.__contains__(mesic):
            def soucetMesicnichVkladu (mesicniVklady):
                sum = 0
                for x in mesicniVklady:
                    sum = sum + x
                return sum

            def soucetMesicnichVkladu2 (mesicniVklady):
                return functools.reduce(lambda acc, vklad: acc + vklad, mesicniVklady)

            aktualniCastka = aktualniCastka + soucetMesicnichVkladu2(vklady[mesic])

        aktualniCastka = aktualniCastka *(1 + urok/100/12)
        aktualniCastka = round(aktualniCastka, 2)
        print("Castka na uctu v %s je: %s."%(mesic, aktualniCastka))
    return aktualniCastka

vklady = {
    1: [20],
    3: [-10, -20],
    5: [30, 70],
    9: [-20, 80]
}
print(vypoctiSlozeneUroky(5,100,vklady))

