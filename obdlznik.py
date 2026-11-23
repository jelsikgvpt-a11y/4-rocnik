class Obdlznik:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def obvod(self):
        return 2 * (self.a + self.b)
    
    def obsah(self):
        return self.a * self.b
    
    

a = Obdlznik(3,2)
b = Obdlznik(4,3)

c = a.obvod(), a.obsah()
d = b.obvod(), b.obsah()
print(c)
print(d)

subor = open("skusam.py", "r")
