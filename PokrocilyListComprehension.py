krestni=["Adam", "Ferda", "Lumir"]
prijmeni=["Novak", "Dvorak"]

jmena=[(x + " " + y) for x in krestni if len(x)>4 for y in prijmeni if len(y)>5]
print(jmena)

for _ in range(4):
    print("ahoj")

# podtrzitko - muze tam byt cokoliv, jde mi o pocet opakovani

ctyri = [x for x in krestni for __ in range(4)]
print(ctyri)

import statistics
statistics.mode()

