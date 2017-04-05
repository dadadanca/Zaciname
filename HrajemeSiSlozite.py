print("Hello, world!")

seznam = range(1, 21)

def SplnujePodminky(x):
    return x%2==0

def uprav (x):
    return x

def Porovnej(acc, cislo):
    if cislo > acc:
        return cislo
    else:
        return acc

vyfiltrovano = filter (SplnujePodminky, seznam)
transformovano = map (uprav,vyfiltrovano)

import functools
soucet = functools.reduce(Porovnej, transformovano, 0)

print(soucet)










