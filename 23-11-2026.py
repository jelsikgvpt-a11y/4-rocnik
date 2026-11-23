class Fraction:
    def __init__(self, num1, num2):
        self.nominator = num1
        self.dominator = num2
    
    def simply(self):
        temp1 = self.nominator
        temp2 = self.dominator
        while temp1 != temp2:
            if temp1 > temp2:
                temp1 = temp1 - temp2
            else:
                temp2 = temp2 - temp1
        if temp1 != 1:
            self.nominator = self.nominator // temp1
            self.dominator = self.dominator // temp1
            
    def __str__(self):
        return f"{self.nominator}/{self.dominator}"
    
    def __add__(self, other):
        return 

a = Fraction(1,2)
b = Fraction(2,4)
a.simply()
b.simply()
print(a)
print(b)
