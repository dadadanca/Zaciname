cisla = [12, 3, 87, 46, 67, 15, 9, 2, 32, 99, 1, 56, 42, 38, 27, 18]

vysledek = []

# insert sort
while len(cisla)!=0:
    pamet=cisla[0]

    for x in cisla:
        if x < pamet:
            pamet = x
    vysledek.append(pamet)
    cisla.remove(pamet)
print(vysledek)


# bubble sort
# cisla = [12, 3, 87, 46, 67, 15, 9, 2, 32, 99, 1, 56, 42, 38, 27, 18]
cisla = [1, 2, 3, 5, 4, 6, 7, 8, 9]
bylaZmena = True

while bylaZmena:
    bylaZmena=False
    index = 0
    while index < len(cisla)-1:
        if cisla[index]>cisla[index+1]:
            c = cisla[index+1]
            cisla[index+1]=cisla[index]
            cisla[index]=c
            bylaZmena=True
        index = index + 1
        print(cisla)

print(cisla)