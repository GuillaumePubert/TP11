class Duree:
    def __init__(self,heure,min,sec):
        self.__heure=heure
        self.__min=min
        self.__sec=sec

    def __str__(self):
        return(str(self.__heure)+"h"+str(self.__min)+"min"+str(self.__sec)+"sec")

    def __add__(self, other):
        a=self.__heure+other.__heure
        b=self.__min+other.__min
        c=self.__sec+other.__sec
        if c>60:
            b+=1
            c-=60
        if b>60:
            a+=1
            b-=60
        return Duree(a,b,c)

d1=Duree(3,34,55)
d2=Duree(6,30,8)

d3=d1+d2

print(d3)
