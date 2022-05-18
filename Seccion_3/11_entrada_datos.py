#ENTRADA DE DATOS


nombre = input('Ingrese nombre: ')
edad = int(input('Ingrese edad: '))
talla = float(input('ingrese Estatura: '))
print(f'su nombre es: {nombre}')
print(f'su edad es: {edad}')
print(f'su estatura es: {talla}')

#Entrar datos en un alista
print('____________________________________________________________')
lista=[]
for i in range(3):
    entrada=input(f'Ingrese un dato {i}: ')
    lista.append(entrada)
print(lista)