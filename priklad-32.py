def spracuj_riadok(riadok):
    text = ""
    for i in range(0, len(riadok), 2):
        if int(riadok[i:i+2], 16) < 128:
            text += "0 "
        else:
            text += "1 "
    return text.strip()


vstup = open("ciernobiely_obrazok_1 (2).txt")
rozmery = vstup.readline().strip()
sirka, vyska = rozmery.split()
print("Šírka:", sirka, "Výška:", vyska, "Počet bodov:", int(sirka) * int(vyska))

prvy_riadok = vstup.readline().strip()
print(spracuj_riadok(prvy_riadok))

vystup = open("konverzia_suboru_1_vystup.txt", "w")
vystup.write(rozmery + "\n")
vystup.write(spracuj_riadok(prvy_riadok) + "\n")
for riadok in vstup:
    vystup.write(spracuj_riadok(riadok.strip()) + "\n")
    
vystup.close()
vstup.close()