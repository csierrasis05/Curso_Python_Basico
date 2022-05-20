#Polimorfismo:Es la tecnica  que nos posibilita que al invocar un determinado metodo de un objeto, podran obtenerse
#distintos resultados segun la clase del objeto 

class Gatos:
    def hablar(self):
        print('MIAU')

class Perros:
    def hablar(self):
        print('GUAU')

def mascota(obj_animal):
     obj_animal.hablar()


#if __name__ == "__main__": Si se ha ejecutado como programa principal se ejecuta el codigo dentro del condicional

if __name__ == "__main__":
    g = Gatos()
    p = Perros()
    mascota(g)
    mascota(p)
