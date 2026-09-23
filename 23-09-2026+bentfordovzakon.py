import random
vysledky = {}
pocet_opakovani = 10000
for i in range(1,10):
    vysledky[i] = 0
    
for i in range(0,pocet_opakovani):
    c1 = random.randrange(start=1, stop=101)
    c2 = random.randrange(start=1, stop=101)
    c= c1**c2
    cifra = int(str(c)[0])
    vysledky [cifra] +=1
print(vysledky)

for i in vysledky:
    cislo = vysledky[i]/100
    print(cislo)
    
