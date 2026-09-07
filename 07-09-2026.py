zoz = []

def prepare(n):
    global zoz
    zoz = ["-"] * n
    print (zoz)
    



def doit(n:int):
    prepare(n)

def schreder(n):
    global zoz
    if n == -1:
        print(zoz)
    else:
        for i in range(97,123):
            zoz[n-1] = chr(i)
            schreder(n-1)
            
            


doit(4)