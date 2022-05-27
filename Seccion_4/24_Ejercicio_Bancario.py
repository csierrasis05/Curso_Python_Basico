""" 
Desarrollar un programa, que conste de una clase padre "Cuenta", y dos subclases "PlazoFijo","CajaAhorro".
Definir los atributos titular y cantidad y un metodo para imprimir los datos en la clase Cuenta. La clase
CajaAhorro tendra un metodo para heredar los datos y uno para mostrar la informacion.
La Clase PlazoFijo tendra dos atributos propios, plazo e interez. Tendra un metodo  para optener el importe
del interes (cantidad*interes/100) y otro metodo para mostrar la informacion, datos del titular plazo, interes,
y total de interes.
Crear almenos un objeto de cada subclase  
"""

from unicodedata import name


class Cuentas():
    def __init__(self, titular='', cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def __str__(self):
        return 'Datos de Cuenta:\n\tTitular: {0}\n\tCantidad: {1}'.format(self.titular,self.cantidad)
    
class CajaAhorro(Cuentas):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)

    def __str__(self):
        return 'Datos de Caja de Ahorro:\n\tTitular: {0}\n\tCantidad: {1}'.format(self.titular,self.cantidad)

class PlazoFijo(Cuentas):
    def __init__(self,cuenta):
        super().__init__(cuenta.titular,cuenta.cantidad)
        self.plazo = int(input('Digite el plazo: '))
        self.interes = float(input('Digite el interes: '))
        
    # def __init__(self,titular,cantidad):
    #     super().__init__(titular,cantidad)
    #     self.plazo = int(input('Digite el plazo: '))
    #     self.interes = float(input('Digite el interes: '))

    def ObtenerInteres(self):
        return (self.cantidad*self.interes)/100

    def __str__(self,tinteres):
        return 'Datos del Titular:\n\tNombre:\t\t{0}\n\tCantidad:\t{1}\n\tPlazo:\t\t{2}\n\tInteres:\t{3}\n\tTotal Interes:\t{4}'.format(self.titular,self.cantidad,self.plazo,self.interes,tinteres)


if __name__=='__main__':
    c1 = Cuentas('Diana',20000000)
    print(c1)

    ca1 = CajaAhorro('Carlos',30000000)
    print(ca1)

    pf2 = PlazoFijo(c1)
    tint = pf2.ObtenerInteres()
    print(pf2.__str__(tint))

    # pf = PlazoFijo('Federico',5000000)
    # tint = pf.ObtenerInteres()
    # print(pf.__str__(tint))
