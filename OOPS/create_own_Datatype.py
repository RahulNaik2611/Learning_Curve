class Fraction:

    #parametrized constructor
    def __init__(self,x ,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        newnum = self.num * other.den + self.den*other.num
        newden = self.den * other.den
        return '{}/{}'.format(newnum,newden)

    def __sub__(self,other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return '{}/{}'.format(newnum,newden)

    def __mul__(self,other):
        newnumm = self.num * other.num
        newden = self.den * other.den
        return '{}/{}'.format(newnumm,newden)

    def __truediv__(self,other):
        newnumm = self.num * other.den
        newden = self.den * other.num
        return '{}/{}'.format(newnumm,newden)

    def convert_to_decimal(self):
        return self.num/self.den




fr1 = Fraction(1,7)
fr2 = Fraction(3,8)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_to_decimal())

