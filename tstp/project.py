import tstp.hello as dana

dana.print_hello()

from tstp.hello import print_hello as ph

ph()

import os
print(os.path.join("A", "B", "C"))



file=open("Filujeme.txt", "w")
file.write("Hello\n")
file.close()

file=open("Filujeme.txt", "a")
file.write("How are you?")
file.close()

with open("Filujeme.txt", "r") as file:
    print(file.read())
# file se automaticky zavre, az s nim prestanu pracovat v ramci bloku

import csv
with open("tabulka.csv", "w", newline="") as file:
    w= csv.writer(file, delimiter=",")
    w.writerow([1,2,3])
    w.writerow([4,5,6, "=b1*3"])






