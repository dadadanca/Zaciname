zpravaProDanu = "Tohle je tajná zpráva, kterou je nutné přečíst. Konference se mi moc líbila a naše účast stála za to Mimochodem, pěkný stánek."

# A tohle jsem pripsal Ja

print(len(zpravaProDanu))
print(zpravaProDanu[4])
print(zpravaProDanu[:10:-1])
print(zpravaProDanu[::-1])

# zprava[od:do:krok]

print(zpravaProDanu.upper())
print(zpravaProDanu.lower())

print(zpravaProDanu.count("o"))
print(zpravaProDanu.count("je"))
print(zpravaProDanu.count("te"))

print(zpravaProDanu.__contains__("z"))
print(zpravaProDanu.__contains__("naše účast stála"))

print(zpravaProDanu.index("f"))
# pozice toho, co hledam (kde je to umisteny)

# MalyText = zpravaProDanu.lower()
# print(MalyText.index("t"))

print(zpravaProDanu.lower().index("t"))

print(zpravaProDanu.startswith("g"))
print(zpravaProDanu.startswith("Tohle"))

print(zpravaProDanu.endswith("a"))

print(len(zpravaProDanu.split(" ")))


