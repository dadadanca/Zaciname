import re

zadani=input("Zadej text k zasifrovani: ").lower()
veta=""
seznam_slov=re.split(r" ", zadani)
for pozice, x in enumerate(seznam_slov):
    y=[]
    i=len(x)-1
    while i>=0:
        y.append(x[i])
        i-=1
    if y[0] == "," or y[0] == "." or y[0] == "!" or y[0] == "?" or y[0] == ":":
        y.append(y[0])
        y.pop(0)
    obracenex = "".join(y)
    if pozice==0:
        obracenex = obracenex.capitalize()
    veta= veta + obracenex +" "
print(veta)

