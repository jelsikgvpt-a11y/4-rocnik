#import math
#x = int(input("Zadaj cislo: "))
#urobme faktorial z cisla x
#faktorial = math.factorial(x)
#print(f"Faktorial cisla {x} je: {faktorial}")

def fak(n:int) -> int:
    re = 1
    for i in range(2, n+1):
        re *= i
        return re
def fak2(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * fak2(n-1)
print

def fibonacci(n):
    if n ==1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))



