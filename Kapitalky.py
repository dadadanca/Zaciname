from ZvetsovaciFunkce import ZvetsiTotoSlovo

veta = input("Zadejte vetu ke zvetseni:")
while veta!="":
    slova = veta.split(" ")


    # Dana: map aplikuje funkci ZvetsiSlovo na všechna slova
    slova = map(ZvetsiTotoSlovo, slova)
    velkaSlova = list(slova)

    print(" ".join(velkaSlova))
    # vytvori mi vetu z velkaSlova
    veta = input("Zadejte dalsi vetu ke zvetseni:")
print("Diky, ahoj")

