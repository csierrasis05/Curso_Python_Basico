from cmath import *
from pandas import isnull
import math


class Punto():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __init__(self):
        self.x = int(input('Por favor digite la coordenada X: '))
        self.y = int(input('Por favor digite la coordenada Y: '))
        if isnull(self.x) or self.x == '':
            self.x = 0
        if isnull(self.y) or self.y == '':
            self.y = 0
        
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)
    
    def Cuadrante(self):
        if self.x == 0 and self.y!=0:
            print('Cuadrante: Eje Y')
        elif self.x != 0 and self.y==0:
                print('Cuadrante: Eje X')
        elif self.x == 0 and self.y==0:
                print('Cuadrante: Origen')
        elif self.x > 0 and self.y > 0:
                print('Cuadrante: Cuadrante 1')
        elif self.x < 0 and self.y > 0:
                print('Cuadrante: Cuadrante 2')
        elif self.x < 0 and self.y < 0:
                print('Cuadrante: Cuadrante 3')
        elif self.x > 0 and self.y < 0:
                print('Cuadrante: Cuadrante 4')
        
    def Vector(self,p2):
        vectx = p2.x - self.x
        vecty = p2.y -self.y
        return '({0},{1})'.format(vectx,vecty)
    
    def Distancia(self,p2):
        dist = sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2)
        print(f'La distancia entre los puntos es: {dist}')
        

class Rectangulo():        
        def __init__(self,pini=Punto(),pfin=Punto()):
            self.pini = pini
            self.pfin = pfin
            
        def base(self):
            base = abs(self.pfin.x - self.pini.x)
            return base
        
        def altura(self):
            return abs(self.pfin.y - self.pini.y)
    
        def area(self):
            area = (self.base()*self.altura())/2
            print(f'El area del rectangulo es: {area}')
                
  
if __name__=='__main__': 
        p1 = Punto()
        print(p1)
        p1.Cuadrante()
        print('_______________Calcular Vector_______________')
        p2=Punto()
        print(p2)
        print(f'El Vector Resultante es: {p1.Vector(p2)}')
        p1.Distancia(p2)
        print('_______________RECTANGULO_______________')
        r = Rectangulo()
        base = r.base()
        print(base)
        altu = r.altura()
        print(altu) 
        r.area()
        