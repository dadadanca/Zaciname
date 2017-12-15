sifrovaci_klic = list(" bdCĚT6IQ5ŠRzhžm4ýXÁFČ2GÍe.3xáf1čNÚOĎŮg0íjawŽMÝEJAWék,lnúoďůcět7iqšrp8sřuvyBDZHÉKLPS9ŘUVY")

def desifruj(zasifrovana_zprava):
    zasifrovana_zprava_jako_list = zasifrovana_zprava.split(", ")
    desifrovana_zprava_jako_list = [sifrovaci_klic[int(cislo)] for cislo in zasifrovana_zprava_jako_list]
    return "".join(desifrovana_zprava_jako_list)

def sifruj(zprava):
    zprava_jako_list = list(zprava)
    zasifrovana_zprava_jako_list = []
    for pismeno in zprava_jako_list:
        index = sifrovaci_klic.index(pismeno)
        zasifrovana_zprava_jako_list.append(str(index))
    return ", ".join(zasifrovana_zprava_jako_list)



zprava = "76, 42, 55, 64, 53, 0, 72, 15, 40, 66, 0, 68, 61, 52, 55, 61, 0, 68, 67, 57, 38, 67, 42, 15, 57, 73, 42, 62, 26, 0, 48, 70, 25, 15, 0, 55, 42, 0, 5, 25, 1, 25, 0, 68, 74, 66, 55, 17, 26, 0, 87, 42, 66, 25, 52"
print(desifruj(zprava))
