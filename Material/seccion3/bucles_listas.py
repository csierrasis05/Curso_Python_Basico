# lista es un conjunto de elementos ordenados 

num=[1,3,4,5]
frutas=["manzana","naranja","fruta"]
mixto=[1,"zapato",2,"toalla",3,"ropa"]
print(num[0])
print(frutas[1])
print(mixto[3])

#Bucles hacen resultado de forma repetiva y rapida


#while hacen de forma infinita
i=0
while i<6:
    i=i+1
    print(f"el numero es {i}")

#for repetiva pero con limite o rango

for i in range(0,6):
    print(f" numeros for es {i}")


i=0
while i <len(frutas):    
    print(f" la fruta es {frutas[i]}")
    i=i+1
    

j=0
for i in frutas:
    print(f"la fruta por for es {i}")





