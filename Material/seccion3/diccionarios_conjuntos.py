""" CONJUNTO DE DATOS: Es una coleccion desordenada sin elementos duplicados.  """
deportes={"voley","futbol","basquet","tenis"}
print(deportes)
print("vole" in deportes)
a=set('abracadabra')
print(a)
#una lista de compresiones
a={ x for x in a if x not in "abc"}
print(a)

""" DICCIONARIOS: es una forma de almacenar datos, podemos usar cualquier
 cosa para identificarlas.  """

datos={'id':1,'name':'ever'}
print(datos["id"])
datos["city"]="lima"
print(datos["city"])










