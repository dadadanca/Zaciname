a = "Camus"
print(a[0])
print(a[1])

reponse_one = input("What did you write yesterday?")
reponse_two = input("And whom did you send it?")

sentence = "I wrote {} to {}."
print(sentence.format(reponse_one, reponse_two))

author = "aldous HuxlEy"
print(author.capitalize())
# zvetsi jen prvni pismenko a ostatni ucini malym
print(author.title())
# udela pismenka na zacatku kazdeho slova velkymi


a = "Where now?"
b = "Who now?"
otazky = []
otazky.append(a)
otazky.append(b)
print(otazky)

slova = ["The", "fox", "jumped", "."]
cast_vety = " ".join(slova[0:3])
cela_veta =cast_vety + slova[3]
print(cela_veta)

word = "screaming"
new_word = word.replace("s","d")
print(new_word)

Ernest = "Hemingway"
print(Ernest.index("m"))

tri = "three"
print("three " + "three " + "three ")
trizasebou = tri*3
prvni = trizasebou[:5]
druhy = trizasebou[5:10]
treti = trizasebou[10:]

print(prvni + druhy + treti)




