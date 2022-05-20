#Encapsulamienti: Consiste en denegar el acceso a los atributos y metodos internos de 
#la clase desde el exterior

class Alumnos():
    def __init__(self,nombre):
        self.nombre=nombre
        self.__id=444444 #el doble guion nos indica que es un atributo privado

var=Alumnos('Juan')
print(var.nombre)
#print(var.__id) #ERROR no deja acceder
print(var._Alumnos__id) #De esta manera si nos deja acceder