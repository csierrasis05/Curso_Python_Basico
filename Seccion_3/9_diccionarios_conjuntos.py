#DICCIONARIOS Y CONJUNTOS

#CONJUNTO DE DATOS: es una coleccion desordenada sin elementos duplicados

deportes={"voley","futbol","basquet","tenis"}
deportes.add("Beisball")
print(deportes)
deportes.remove("Beisball")
print(deportes)
print("voley" in deportes) #para validar si existe un elemento dentro del conjunto de datos
a=set('esternocleidomastoideo') #extrae todas las vocales de na palabra
print(a)

#una lista de compresiones
a = {x for x in a if x not in 'abc'}
print(a)


'''
Método	Descripción
add()	Añade un elemento
clear()	Remueve todos los elementos
copy()	Entrega una copia del set
difference()	Entrega un set conteniendo los miembros diferentes entre dos o más sets
difference_update()	Remueve los elementos en este set que también se incluyen en otro set específico
discard()	Remueve un elemento específico
intersection()	Entrega un set, que es la intersección de otros dos sets
intersec_update()	Remueve los elementos en este set que no se encuentran presentes en otro set específico.
isdisjoint()	Entrega si dos sets tienen una intersección o no
issubset()	Entrega si otro set contiene este set o no
issuperset()	Entrega si este set contiene otro set o no
pop()	Remueve un elemento específico
remove()	Remueve un elemento específico
symmetric_difference()	Entrega un set con la diferencia simétrica de dos sets
union()	Entrega un set que contiene la unión de dos sets
update()	Actualiza el set con la unión de éste y otros sets

set_frutas = {"fresa", "piña", "cereza"}
print(set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
for x in set_frutas:
    print(x)
    
print("piña" in set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
set_frutas.add("sandía")
print(set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
set_frutas.update(["sandía", "melón", "mango"])
print(set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
set_frutas.remove("piña")
print(set_frutas)
set_frutas.discard("cereza")
print(set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
set_frutas.clear()
print(set_frutas)

set_frutas = {"fresa", "piña", "cereza"}
del set_frutas
#print(set_frutas)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

'''
#DICCIONARIOS: es una forma de almacenar datos, podemos usar cualquier cosa para identificarlos
datos={'id':1,'nombre':'Carlos'}
print(datos)
print(datos['id'])
datos['Ciudad']='Medellin' #Se puede usar para adicionar nuevos elementos al diccionario
print(datos['Ciudad'])
print(datos)

#podemos recorrer el diccionario con una estructura for
for key in datos:
  print(key, ":", datos[key])