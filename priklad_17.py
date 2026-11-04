#Tomáš Jelšík
veta = input("Zadaj mi vetu s velkymi pismenami:")

pocty = [0] * 10

for znak in veta:
    if znak == " ":
        cislo = 0
        opakovanie = 1
        vysledok = "0"
    else:
        cislo = (ord(znak) - ord("A")) //3 +1
        opakovanie= (ord(znak) - ord("A")) % 3 +1
        vysledok = str(cislo) * opakovanie
        

    print(vysledok, end = " ")
    pocty[cislo] += opakovanie
najviac = max(pocty)

print()
print("Najcastejsie zvolene policko:", end = " ")

for i in range(10):
    if pocty[i] == najviac:
        print(i, end = " ")
        