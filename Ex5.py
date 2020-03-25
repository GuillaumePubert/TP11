import numpy as np

class Matrice :
    def __init__(self,mat):
        self.__matrice=mat

    def __add__(self,other):
        new_matrice=np.array([[0, 0],
                             [0,0]])
        for i in range (2) :
            for j in range (2) :
                new_matrice[i, j]= self.__matrice[i, j] + other.__matrice[i, j]
        return Matrice(new_matrice)

    def __sub__(self,other):
        new_matrice=np.array([[0, 0],
                             [0,0]])
        for i in range (2) :
            for j in range (2) :
                new_matrice[i, j]= self.__matrice[i, j] - other.__matrice[i, j]
        return Matrice(new_matrice)

    def __iadd__(self,other):
        for i in range (2) :
            for j in range (2) :
                self.__matrice[i, j] += other.__matrice[i, j]
        return Matrice(self.__matrice)

    def __isub__(self,other):
        for i in range (2) :
            for j in range (2) :
                self.__matrice[i, j] -= other.__matrice[i, j]
        return Matrice(self.__matrice)

    def __mul__(self,other):
        return Matrice(np.dot(self.__matrice,other.__matrice))

    def __imul__(self,other):
        self.__matrice=np.dot(self.__matrice,other.__matrice)
        return Matrice(self.__matrice)

    def __str__(self):
        return str(self.__matrice)

    def __len__(self):
        return self.__matrice.shape()

    def __lt__(self,other):
        a=0
        for i in range (2) :
            for j in range (2) :
                a=self.__matrice[i,j]-other.__matrice[i,j]
                if a>0:
                    return False
        return True

    def __gt__(self,other):
        a=0
        for i in range (2) :
            for j in range (2) :
                a=self.__matrice[i,j]-other.__matrice[i,j]
                if a<0:
                    return False
        return True



if __name__ == '__main__' :
    m1=np.array([[1, 2],
                 [3,4]])
    m2=np.array([[1, 0],
                 [0,1]])

    m1=Matrice(m1)
    m2=Matrice(m2)
    m3= m1 < m2
    print(m3)
    m3= m1 > m2
    print(m3)
    m3= m1 + m2
    print(m3)
    m3= m1 - m2
    print(m3)
    m1+=m2
    print(m1)
    m1-=m2
    print(m1)
    m3= m1 * m2
    print(m3)
    m1*=m2
    print(m1)

