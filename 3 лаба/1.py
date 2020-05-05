"""
Дополнить класс таким образом, чтобы выполнялся следующий код:
frac = Fraction(7, 2)
print(-frac) # выводит -7/2
print(~frac) # выводит 2/7
print(frac**2) # выводит 49/4
print(float(frac)) # выводит 3.5
print(int(frac)) # выводит 3
"""
class Fraction(object):

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def __neg__(self):
        return "%d/%d" % (-self.__num, self.__den)

    def __invert__(self):
        return "%d/%d" % (self.__den, self.__num)

    def __float__(self):
        return float(self.__num/self.__den)

    def __int__(self):
        return int(self.__num/self.__den)

    def __pow__(self, step):
        return "%d/%d" % (self.__num**step, self.__den**step)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
        return g

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)


frac = Fraction(7, 2)
print(frac)
print(-frac)
print(~frac)
print(frac**2)
print(float(frac))
print(int(frac))
