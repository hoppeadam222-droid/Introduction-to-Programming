#delka = 1250
#centimetry = delka/10
#metry = delka/1000
#palce = centimetry/ 2.54
#print(f" {delka}, {centimetry}, {metry}, {palce:.2f}")

#cas_sekund=int(input("zadej cas v sekundach"))
#hodiny = cas_sekund // 3600
#zbytek_hodin = cas_sekund%3600
#minuty = zbytek_hodin // 60
#zbytek_minut = zbytek_hodin % 60
#print(f"čas je {hodiny} hodin, {minuty} minut a {zbytek_minut} sekund")


#slovo = "Nepotopen"
#pocet_znaku = len(slovo)
#prvni_znak = slovo[0]
#slovo_pozpatku = slovo[::-1]
#posledni_znak = slovo_pozpatku[0]
#cap_slovo = slovo.capitalize()
#cap_slovo_pozpatku = slovo_pozpatku.capitalize()
#if cap_slovo == cap_slovo_pozpatku:
#    print(f"slovo {slovo} je palindrom ")
#print(pocet_znaku, prvni_znak, posledni_znak, slovo_pozpatku, cap_slovo.upper())

#x = int(input("zadej cislo bitu"))
#low_xbit = (-2**(x-1))
#up_xbit = (2**(x-1))-1
#print(low_xbit, up_xbit)

cislo = int(input("zadej cislo pro prevedeni do binarniho tvaru"))
cislo_bin = ""
kontrola = bin(cislo)
while cislo % 2 != 0:
    cislo = cislo%2
    str(cislo)
    cislo_bin = cislo_bin + cislo
    int (cislo)

print(cislo_bin)

