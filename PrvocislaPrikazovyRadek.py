import sys
import math
import functools

cisla = [int(x) for x in sys.argv [1::] if int(x) > 0]
print(cisla)

def JeToPrvocislo (x):
    DruhaOdmocnina = int(math.sqrt(x)) + 1
    Delitele = range (2, DruhaOdmocnina)
    # skutecniDelitele = [d for d in Delitele if x%d==0]
    # return len(skutecniDelitele) == 0

    for delitel in Delitele:
        if x%delitel == 0:
            return False
    return True


Prvocisla = list(filter (JeToPrvocislo,cisla))

print(Prvocisla)

SoucetPrvocisel = functools.reduce(lambda acc, prvocislo: acc + prvocislo,Prvocisla, 0)
print(SoucetPrvocisel)
