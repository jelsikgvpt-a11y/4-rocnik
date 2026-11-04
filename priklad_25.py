#a
import random

tipy = input("Zadaj 6 cisel od 1 do 49: ").split()
tipy = set(map(int, tipy))

zreb = set()

while len(zreb) < 6:
    zreb.add(random.randint(1, 49))

print("Vyzrebovane cisla:", zreb)

uhadnute = tipy & zreb
print("Uhadnute cisla:", uhadnute)
print("Pocet uhadnutych:", len(uhadnute))

subor = open("loteria_1.txt", "r")

pocty = [0, 0, 0, 0, 0, 0, 0]

for riadok in subor:
    cisla = set(map(int, riadok.split()))
    uhadnute = tipy & cisla
    pocty[len(uhadnute)] += 1

subor.close()

print("Pocet tipov s 0 uhadnutymi:", pocty[0])
print("Pocet tipov s 1 uhadnutym:", pocty[1])
print("Pocet tipov s 2 uhadnutymi:", pocty[2])
print("Pocet tipov s 3 uhadnutymi:", pocty[3])
print("Pocet tipov s 4 uhadnutymi:", pocty[4])  
print("Pocet tipov s 5 uhadnutymi:", pocty[5])
print("Pocet tipov s 6 uhadnutymi:", pocty[6])