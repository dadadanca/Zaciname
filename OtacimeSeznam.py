seznam = [1,2,3,4,5]
otoceny_seznam = []

for cislo in seznam:
    otoceny_seznam.insert(0, cislo)

print(otoceny_seznam)

otoceny_seznam = []
delka=-len(seznam)
index = -1

while index >= delka:
    otoceny_seznam.append(seznam[index])
    index -= 1

print(otoceny_seznam)


index=0
while index < len(seznam)/2:
    pomoc= seznam[index]
    seznam[index] = seznam[-index-1]
    seznam[-index - 1]=pomoc
    index += 1

print(seznam)

def je_palindrom(slovo):
    slovo = slovo.lower()
    bez_mezer = slovo.split(" ")
    slovo = "".join(bez_mezer)
    index = 0
    while index < len(seznam) / 2:
        if slovo[index] == slovo[-index-1]:
            index += 1
        else:
            return False
    return True

print(je_palindrom("Jelenovi pivo nelej"))
