#coding:utf-8
import fractions
class Fractional:
    def __init__(self,numerator,denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.denominator == 0:
            raise ValueError
        else:
            return ('{n}/{d}'.format(n=self.numerator,d=self.denominator))

    __repr__=__str__

    #计算最大公约数
    def gcd(a,b):
        if a < b:
            a,b = b,a
        while b != 0:
            mod = a % b
            a,b = b,mod
        return a
    #计算最小公倍数
    def lcm(a,b):
        return (a * b) / Fractional.gcd(a,b)

    def __add__(self,other):
        lcm_num = Fractional.lcm(self.denominator,other.denominator)
        add_num = (lcm_num / self.denominator) * self.numerator + \
                  (lcm_num / other.denominator) * other.numerator
        return Fractional(add_num,lcm_num)


f = Fractional(3,4)
print(f)
n = Fractional(2,3)
print(n)
s = f + n
print(s)