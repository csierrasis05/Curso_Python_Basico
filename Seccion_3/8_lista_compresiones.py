#LISTA DE COMPRESIONES: ES UNA FUNCIONALIDAD QUE PERMITE CREAR LISTAS AVANZADAS EN UNA MISMA LINEA DE CODIGO

#Hay dos formas de crear listas
#1. normal
#2. [expresione for item in iterable]

#1.Normal

lista=[]
for i in range(1,6):
    lista.append(i)
print(lista)

#2. Lista de compresiones
list = [x for x in range(1,6)]
print(list)

#Lista con texto  Normal
lista2=[]
for texto in 'Hola':
    lista2.append(texto)
print(lista2)

#Lista con texto  lista de compresiones
list2=[letra for letra in 'Hola']
print(list2)