class Complex:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self.__a+other.__a,self.__b+other.__b)
    def __sub__(self, other):
        if isinstance(other,Complex):
            return Complex(self.__a-other.__a,self.__b-other.__b)
    def __mul__(self, other):
        if isinstance(other,Complex):
            return Complex(self.__a*other.__a-self.__b*other.__b,self.__a*other.__b+self.__b*other.__a)
    def __truediv__(self, other):
        if isinstance(other,Complex):
            return Complex(((self.__a*other.__a)+(self.__b*other.__b))/(other.__a**2+other.__b**2),((self.__b*other.__a)-self.__a*other.__b)/(other.__a**2+other.__b**2))

    def __abs__(self):
        return Complex((self.__a**2)**0.5,(self.__b**2)**0.5)
    def __eq__(self, other):
        if isinstance(other,Complex):
            return self.__a==other.__a and self.__b==other.__b
    def __ne__(self, other):
        if isinstance(other,Complex):
            return self.__a!=other.__a or self.__b!=other.__b
    def __str__(self):
        return str(self.__a)+'+'+str(self.__b)+'i'

if __name__ == '__main__' :
    comp1=Complex(1,2)
    comp2=Complex(3,4)
    comp3=comp1 + comp2
    comp4=comp1-comp2
    comp5=comp1*comp2
    comp6=comp1/comp2
    comp9=Complex(-3,7)
    comp10=abs(comp9)
    comp11=comp9==comp10
    comp12=comp9!=comp10

    print(comp3,comp4,comp5,comp6,comp10,comp11,comp12)
