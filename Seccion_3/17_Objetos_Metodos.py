#Atributos: Caracteristica que puede tener un atributo
#(int,cadenas,listas)

class Personas:
    nombre = 'Carlos'
    edad = 32
    sexo = 'M'

persona = Personas()
print(f'Nombre: {persona.nombre} \nEdad: {persona.edad} \nSexo: {persona.sexo}')
#Metodos: describen el comportamiento de los objetos de una clase. Estos representan
#las operaciones que se pueden realizar con los objetos de la clase. Son Funciones

class Personas:
    nombre = 'Carlos'
    edad = 32
    sexo = 'M'
    
    def Trabajar(self,tiempo,ciudad):
        self.tiempo = tiempo
        self.ciudad = ciudad
    
    def Imprimir(self):
        print(f'\nTiempo de labores es: {self.tiempo} horas \nCiudad de labor: {self.ciudad}')
    
    def Imprimir_con_Mensaje(self,texto):
        print(f'\n{texto}')


persona = Personas()
persona.Trabajar(10,'Barcelona')
persona.Imprimir()
persona.Imprimir_con_Mensaje('Yo soy ' + persona.nombre + ' ,Tengo ' + str(persona.edad) + ' años')



#Objetos: Al crear objetos, se le denomina instanciar una clase y dicha instancia, consiste
#en asignar la clase como valor a una variable.

class Personas:
    def datos(self,nombre,edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def Trabajar(self,tiempo,ciudad):
        self.tiempo = tiempo
        self.ciudad = ciudad
    
    def Imprimir(self):
        print(f'\nTiempo de labores es: {self.tiempo} horas \nCiudad de labor: {self.ciudad}')
    
    def Imprimir_con_Mensaje(self,texto):
        print(f'\n{texto}')


persona = Personas()
persona.datos('Felipe',31,'M')
persona.Trabajar(10,'Barcelona')
persona.Imprimir()
persona.Imprimir_con_Mensaje('Yo soy ' + persona.nombre + ' ,Tengo ' + str(persona.edad) + ' años')