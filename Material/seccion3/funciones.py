""" LAS FUNCIONES  
1. Nombran fragmento de codigo
2. Toman argumentos similar a (argv.))
3. Nos permiten crear propio miniprogramas
"""
def inicio(*arg):
    suma,resta,divi,multi,num1,num2=arg
    print(f"{suma} es {num1+num2}")
    print(f"{resta} es {num1-num2}")
    print(f"{divi} es {num1/num2}")
    print(f"{multi} es {num1*num2}")

inicio("suma","resta","division","multiplicacion",5,7)


