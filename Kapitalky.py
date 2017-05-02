veta = "Toto je veta, ktera by cela mely byt napsana slovy s velkymi pocatecnimi pismeny."

slova = veta.split(" ")
slova = map(lambda slovo: slovo.upper(), slova)
velkaSlova = list(slova)
print(velkaSlova)

print(" ".join(velkaSlova))