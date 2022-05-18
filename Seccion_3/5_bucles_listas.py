#BUCLES Y LISTAS

#listas: Conjunto de elementos oredenados
num = [1,2,6,7,9]
frutas = ['Manzana','Mango','Pera','Naranja','Mandarina']
mixto = ["Aguja",3,'Mar',5,'Energia']

print(num)
print(frutas)
print(mixto)

#Referencia a un solo alemento de la lista
print(num[3])
print(frutas[3])

#WHILE 
#si no se define una variable de parada se hace infinitamente
i=0
while i<6:
    i=i+1
    print(f'el numero es: {i}')
 
i=0   
while i<len(frutas):    
    print(f'Fruta: {frutas[i]}')
    i=i+1
        
#FOR
#se define un limite o rango
for j in range(0,6):
    print(f'el NUM es: {j}')
    
for j in frutas:
    print(f'NOMBRE FRUTA: {j}')
    
