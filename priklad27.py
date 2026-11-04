import random
subor = open("virus.txt", "r", encoding="utf-8")
riadky = subor.readlines()
subor.close()
print("Povodny text:")
print("".join(riadky))
if random.randint(0, 1) == 1:
    riadky.reverse()
for i in range(len(riadky)):
    slova = riadky[i].split()
    if random.randint(0, 1) == 1:
        slova.reverse()

    for j in range(len(slova)):
        if random.randint(0, 1) == 1:
            slova[j] = slova[j][::-1]

    riadky[i] = " ".join(slova) + "\n"

subor = open("virus_vystup.txt", "w", encoding="utf-8")
subor.writelines(riadky)
subor.close()
