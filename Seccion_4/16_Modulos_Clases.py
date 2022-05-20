#Modulos: son como los diccionarios, nos permiten acceder a funciones y variables a traves
#de un fichero 

import cosas_16

cosas_16.mesa()

#Clase: Es una forma de agrupar funciones y datos y guardarlos en un contenedor de manera
#que se acceda a ellos a traves del operador '.'(Punto). La clase instancia Objetos

class saludo():
    nombre = 'Carlos'
    edad = 33

    def hola(self):
        print('Hola Mundo de la clase')


var = saludo()
print(var.nombre, var.edad)
var.hola()