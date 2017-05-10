veta = input("Zadejte vetu ke zvetseni:")
while veta!="":
    slova = veta.split(" ")

    def ZvetsiSlovo (slovo):
        if len(slovo)>1:
            return slovo[0].upper()+ slovo[1::]
        else:
            return slovo
    # Dana: map aplikuje funkci ZvetsiSlovo na všechna slova
    slova = map(ZvetsiSlovo, slova)
    velkaSlova = list(slova)

    print(" ".join(velkaSlova))
    # vytvori mi vetu z velkaSlova
    veta = input("Zadejte dalsi vetu ke zvetseni:")
print("Diky, ahoj")

