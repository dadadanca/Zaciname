cisla = [2, 4, 6, 8, 10, 13, 17]


suda = filter(lambda x: x%2==0, cisla)

import functools

soucet = functools.reduce(lambda acc, z: acc + z, suda)
print(soucet)
