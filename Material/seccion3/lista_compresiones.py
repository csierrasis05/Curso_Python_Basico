""" LISTA DE COMPRESIONES: es una funcionalidad que le permite crear listas avanzadas en una misma línea de código.    
    
    << [expresion for item in iterable] >> """

lista=[]
for i in range(1,6):
     lista.append(i)  
print(lista) 

#lista comprensiones
lis=[x for x in range(1,6)]
print(lis)


lista2=[]
for texto in "hola":
    lista2.append(texto)
print(lista2)
lis2=[letra for letra in "hola"]
print(lis2)
