#Constructor: Es un metodo especial, instancia objetos de una clase, se invoca automaticamente.
#en el se inicializan los atributos de un objeto
#No es obligatorio crearlo ni inicializar todos los atributos
#El metodo __init__ es un metodo espacial de una clase en python. EL Objetivo fundamental 
# es inicializar  los atributos del objeto que se creo.

class Empleados:
    def __init__(self,param1,param2,param3,param4):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3 
        self.param4 = param4        

    def imprimir(self):
        print(f'Nombre: {self.param1} \nEdad: {self.param2} \nJefe Directo: {self.param3.param1}')

    def sueldo(self):
        if self.param4>3000:
            print('El pago tributario es: ',self.param4)
        else:
            print('No paga impuesto Tributario')



emp1 = Empleados('Sierra',33,Empleados('Juan',35,'',5000),2500)
emp1.imprimir()
emp1.sueldo()