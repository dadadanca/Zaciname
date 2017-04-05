print("Hello, world!")

seznam = [10, 20, 33, 47, 59, 67, 88]

def SplnujePodminky(x):
    return x%2==0 or x%3==0

def uprav (x):
    return -100*x

def Secti(acc, cislo):
    return acc+cislo

vyfiltrovano = filter (SplnujePodminky, seznam)
transformovano = map (uprav,vyfiltrovano)

import functools
soucet = functools.reduce(Secti, transformovano)

print(soucet)










