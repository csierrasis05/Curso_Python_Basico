def listar():
    lista = []
    for i in range(5):
        i = i + 1
        var = int(input(print(f'Ingresar Valor {i}:')))
        lista.append(var)
    return lista
    

def ListarMayor(lista):
    may = lista[0]
    for i in range(1,5):
        if lista[i] > may:
            may = lista[i]
    print(f'El mayor numero es: {may}')

def ListarSuma(lista):
    sum = 0
    for i in lista:
        sum = sum + i
    print(f'La suma de los valores es: {sum}')

