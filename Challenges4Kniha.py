# uloha 1
def f(x):
    return x**2

print(f(2))
# uloha 2
jmeno = input("Jak se jmenujes?")
def nejkrasnejsi(x):
    return "%s je nejkrasnejsi"%x

print(nejkrasnejsi(jmeno))

# uloha 3
# optional parameters must be defined as first in the function
def mesicniOdmena(d,e,a=10,b=4,c=0):
    return a+b+c+d-e

print(mesicniOdmena(10,4))

# uloha 4
def divided(x):
    return x / 2

def multiply(x):
    return x * 4

cislo = int(input("Zadej cislo"))

while cislo<=0:
    cislo=int(input("Zadej nove cislo"))
result=divided(cislo)
totalResult=multiply(result)
print(totalResult)

# uloha 5
zadani=input("Napis cokoliv")
def floatujeme(x):
    return float(x)
try:
    print(floatujeme(zadani))
except (ValueError):
    print("Spatne zadani")





















