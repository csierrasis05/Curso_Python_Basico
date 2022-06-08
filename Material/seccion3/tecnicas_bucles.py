""" 1. Recorrer los diccionarios, la clave y el valor correspondiente se pueden recuperar al mismo tiempo
    utilizando el items()  """

datos={"id":1,"name":"ever","edad":24}
for x,y in datos.items():
    print(x,y)


""" 2. Recorrer una secuencia, el índice de posición y el valor correspondiente se pueden recuperar al mismo
    tiempo utilizando la enumerate() """

for x,y in enumerate(["saludo","hola","nombre"]):
    print(x,y)

""" 3. Recorrer dos o más secuencias al mismo tiempo, las entradas se pueden emparejar con la zip(). """

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for x,y in zip(questions,answers):
    print(f" What is your {x} ? it is {y}")


""" 4. Recorrer una secuencia en reversa, primero especifique la secuencia hacia adelante 
   y luego llame a la reversed() """

for i in reversed(range(1,10,2)):
    print(i)






