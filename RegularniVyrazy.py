import re

print(re.findall(r"Dana", "Kde je Dana? Dana je doma."))
# vyhleda mi "Dana" v otazce a da mi vyhledane vyrazy do seznamu aneb hleda CO, KDE

print(re.findall(r"a", "Kde je Dana? Dana je doma."))

print(re.findall(r"na|ma", "Kde je Dana? Dana je doma. O Dane jsem dnes neslysel."))
# hledam to nebo to

print(re.findall(r"Dan[a-z]", "Kde je Dana? Dana je doma. O Dane jsem dnes neslysel."))
print(re.findall(r"Dan[a-zěščřž]", "Kde je Dana? Dana je doma. O Daně jsem dnes neslysel."))
# hleda mi to znaky od a do z vcetne specifickzch ceskzch znaku

print(re.findall(r"Dan[a-zěščřž]+", "Kde je Dana? Dana je doma. O Daně jsem dnes neslyšel.S Danou se dobře programuje."))

print(re.findall(r"Dan[a-zěščřž]*", "Kde je Dana? Dana je doma. O Daně jsem dnes neslyšel.S Danou se dobře programuje. Dan neprisel"))
#hleda Dan plus jakkykoliv dalsi znaky

print(re.findall(r"Dan[a-zěščřž]?", "Kde je Dana? Dana je doma. O Daně jsem dnes neslyšel.S Danou se dobře programuje. Dan neprisel"))
# hleda Dan a nic nebo jeden znak navic

print(re.findall(r"[D|d]an[a-zěščřž]{0,2}", "Kde je Dana? Dana je doma. O daně jsem dnes neslyšel.S Danou se dobře programuje. Dan neprisel"))
# kudrlinky: min, max - pocet pismenek

print(re.findall(r"[D|d]an[0-9]*", "Dan guwgdid Dan2 agshjdgwj Dan3 QHHDWQHD Dan4."))
print(re.findall(r"[D|d]an\d*", "Dan guwgdid Dan2 agshjdgwj Dan3 QHHDWQHD Dan4."))
# hleda Dan s cislicemi

print(re.findall(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-.]+[.][a-zA-Z]{2,3}$", "honza@seznam.cz"))






