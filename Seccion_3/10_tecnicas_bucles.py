#TECNICAS DE BUCLES

#1. recorrer los diccionarios, la clave y el valor correspondiente se pueden recuperar al mismo tiempo
#   utilizando el item()

datos={'id':1,'name':'Carlos','edad':33}

for x,y in datos.items():
    print(x,y)

#2. recorrer una secuencia, el indice de posicion y el valor correspondiente se pueden recuperar al
#   al mismo tiempo utlizando la enumerate()

for x,y in enumerate(['saludos','Hola','Mundo']):
    print(x,y)

#3. Recorrer dos o mas secuencias al mismo tiempo, las entradas se pueden emparejar con la zip()

question = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'What the matter', 'Green']

for x,y in zip(question,answers):
    print(f'what is your {x} ? it is {y}')

#4. para recorrer una secuencia es reversa, primero especifique la secuencia hacia adelante  luego 
#   llame a la reversed()

for i in reversed(range(1,10,2)):
    print(i)

