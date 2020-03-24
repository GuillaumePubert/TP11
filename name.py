class Circle :
    def __init__(self,rayon):
        self.__rayon=rayon

    def get_rayon(self):
        return self.__rayon

    def __add__(self,other):
        return(Circle(self.__rayon+other.__rayon))

    def __lt__(self,other):
        return self.__rayon<other.__rayon

    def __gt__(self,other):
        return self.__rayon>other.__rayon
    def __str__(self):
        return str(self.__rayon)




if __name__ == '__main__' :
    c1=Circle(2)
    c2=Circle(3)
    c3=c1+c2
    c4=c1<c2
    c5=c2>c3
    print(c3,c4,c5)

