def vypoctiUroky (urok, castka):
    return castka *(1 + urok/100)

print(vypoctiUroky(5, 100))


def vypoctiSlozeneUroky (urok, castka):
    aktualniCastka = castka
    for mesic in range (1,13):
        aktualniCastka = aktualniCastka *(1 + urok/100/12)
        aktualniCastka = round(aktualniCastka, 2)
        print("Castka na uctu v %s je: %s."%(mesic, aktualniCastka))
    return aktualniCastka

print(vypoctiSlozeneUroky(5,100))





