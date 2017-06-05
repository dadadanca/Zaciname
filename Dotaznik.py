zdrojovyDokument = open("Answers.csv")
acc = 0
v = 0
prvniRadek = True
jmenoNejstarsiho = ""

for radek in zdrojovyDokument:
    if prvniRadek:
        prvniRadek = False
        continue
    jedenFormular = radek.strip("\n").split(",")
    if jedenFormular[2] == "Yes":
        acc = acc + 1 + int(jedenFormular[4])
        if int(jedenFormular[3]) > v:
            v = int(jedenFormular[3])
            jmenoNejstarsiho = jedenFormular[1]


print(acc)
print(v)
print(jmenoNejstarsiho)

zdrojovyDokument.close()
# parsujeme dokument