#Herencia: Permite crear nuevas clases de clases existentes. tendra todos los atributos y metodos de su "superclase"
#o "Clase Padre" y ademas se le podran añadir otros metodos y atributos propios


#Clase PAdre
class Personas:
    def __init__(self):
        self.nombre = input('Ingresar Nombre: ')
        self.edad = input('Ingresar Edad:')

    def __str__(self):
        return 'Nombre: {0} \nEdad: {1}'.format(self.nombre,self.edad)

#Clase Hija
class Empleados(Personas):
    def __init__(self):
        super().__init__()
        self.salario = float(input('\nIngresar Salario: '))

    def Imprimir(self):
        print(f'Nombre Empleado: {self.nombre} \nSalario: {self.salario}')

    def Impuesto(self):
        if self.salario > 3000:
            print('Debe pagar Impuesto')
        else:
            print('No debe pagar Impuesto')

pers1 = Personas()
print(pers1)

emp1 = Empleados()
emp1.Imprimir()
emp1.Impuesto()

