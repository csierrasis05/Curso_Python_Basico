#FUNCIONES

#se define con la palabra def


def inicio(*arg):
    sum, res, div, mul, num1, num2 = arg
    print(f'{sum} es {num1+num2}')
    print(f'{res} es {num1-num2}')
    print(f'{div} es {num1/num2}')
    print(f'{mul} es {num1*num2}')

inicio('Suma','Resta','Division','Multiplicacion',5,15)