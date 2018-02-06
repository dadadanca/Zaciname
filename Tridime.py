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

# quick sort
cisla = [12, 3, 87, 46, 67, 15, 9, 2, 32, 99, 1, 56, 42, 38, 27, 18]
def quick_sort (seznam):
    print(seznam)
    if len(seznam)<=1:
        return seznam
    pozice_pivota = 0
    levy_index = 1
    pravy_index = len(seznam)-1
    while levy_index<=pravy_index:
        if pozice_pivota < levy_index:
            if seznam[pozice_pivota] > seznam[pravy_index]:
                kapsa=seznam[pozice_pivota]
                seznam[pozice_pivota]=seznam[pravy_index]
                seznam[pravy_index]= kapsa
                pozice_pivota = pravy_index
            pravy_index-=1
        else:
            if seznam[pozice_pivota] < seznam[levy_index]:
                kapsa=seznam[pozice_pivota]
                seznam[pozice_pivota]=seznam[levy_index]
                seznam[levy_index]= kapsa
                pozice_pivota = levy_index
            levy_index+=1
    prvni_cast = quick_sort(seznam[0:pozice_pivota])
    druha_cast = quick_sort(seznam[pozice_pivota+1::])

    return prvni_cast + [seznam[pozice_pivota]] + druha_cast


print(quick_sort(cisla))










