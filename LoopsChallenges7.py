sentence = ["The walking dead", "Entourage"]
index = 0
for x in sentence:
    print(x)
    print(index)
    index +=1


for a in range (25, 50):
    print(a)

cisla = [1, 3, 5, 7,9]
cislo = int(input("Guess a number:"))
while cislo != "q":
    if cislo in cisla:
        print("Right guess")
    else:
        print("Wrong guess")
    cislo = input("Guess another number:")

a=[8,19]
b=[9,1]
c=[]

for x in a:
    for y in b:
        c.append(x*y)
print(c)
