#__str__: Metodo especial para mostrar objetos
#Devuelve una cadena de caracteres con lo que queremos mostrar. Ese metodo se invoca cada vez que llamamos a la
#funcion str

class Personas:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return 'El nombre de la persona es: {0} \nSu edad es: {1}'.format(self.nombre,self.edad)

pers1 = Personas('Camilo', 35)
pers2 = Personas('Andrea', 28)

print(pers1)
print(pers2)
 