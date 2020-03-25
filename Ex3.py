class Rational:
    def __init__(self,num,den):
        self.__num=num
        self.__den=den
    def __pgcd(self):
        a=self.__num
        b= self.__den
        reste=1
        while reste!=0:
            reste=a%b
            a=b
            b=reste
        return a
    def simplification(self):
        a=self.__num
        b= self.__den
        x=a/self.__pgcd()
        y=b/self.__pgcd()
        self.__num=x
        self.__den=y

    def __add__(self, other):
        if isinstance(other,Rational):
            a=self.__num*other.__den+other.__num*self.__den
            b=self.__den*other.__den
            res=Rational(a,b)
            res.simplification()
            return res

    def __sub__(self, other):
        if isinstance(other,Rational):
            return Rational(self.__num*other.__den-other.__num*self.__den,self.__den*other.__den)

    def __mul__(self, other):
        if isinstance(other,Rational):
            res=Rational(self.__num*other.__num,self.__den*other.__den)
            res.simplification()
            return res

    def __truediv__(self, other):
        if isinstance(other,Rational):
            res=Rational(self.__num*other.__den,self.__den*other.__num)
            res.simplification()
            return res


    def __str__(self):
        return (str(self.__num)+"/"+str(self.__den))

r1=Rational(1,3)
r2=Rational(2,6)

r3=r1 + r2
r4=r1*r2
print(r3,r4)
