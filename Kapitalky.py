veta = "Toto je veta, ktera by cela mely byt napsana slovy s velkymi pocatecnimi pismeny."

slova = veta.split(" ")

def zvetsiSlovo(slovo):
    if len(slovo) > 1:
        return slovo[0].upper() + slovo[1::]
    else:
        return slovo

slova = map(zvetsiSlovo, slova)
velkaSlova = list(slova)
print(velkaSlova)

print(" ".join(velkaSlova))