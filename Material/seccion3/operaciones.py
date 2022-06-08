
def listar():
    lista=[]
    for i in range(5):
        i=i+1
        var=int(input(f"Ingresar {i} valor:"))
        lista.append(var)
    return lista

def listar_mayor(lista):
    may=lista[0]
    for i in range(1,5):
        if lista[i]>may:
            may=lista[i]
    print(f"el mayor es: {may}")

def listar_suma(lista):
    sum=0
    for i in lista:
        sum=sum+i 
    print(f"la suma es:{sum}")