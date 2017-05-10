veta = "Toto je veta, ktera by cela mely byt napsana slovy s velkymi pocatecnimi pismeny."

slova = veta.split(" ")

def ZvetsiSlovo (slovo):
    if len(slovo)>1:
        return slovo[0].upper()+ slovo[1::]
    else:
        return slovo
# Dana: map aplikuje funkci ZvetsiSlovo na všechna slova
slova = map(ZvetsiSlovo, slova)
velkaSlova = list(slova)
print(velkaSlova)

print(" ".join(velkaSlova))
# vytvori mi vetu z velkaSlova

