#Ejercicio 1: Programa para convertir numeros Binarios a Enteros

def convertir(numbin):
    numbin = str(numbin)
    decimal = 0 
    exp = len(numbin)-1
    for i in numbin:
        decimal += (int(i)*2**(exp))
        exp = exp -1
    return decimal

print('_____________________________________')
entrada = input('Ingresar numero Binario: ')
conv = convertir(entrada)
print(f'{entrada} su conversion es {conv}')