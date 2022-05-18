#PASS: es un valor vacio para que se ejecute un ciclo o clase
'''
while True: #este ciclo queda infinito
    pass 

class hola:
    pass
    
'''
#BREAK: usado cotidianamente para detener un ciclo

for val in "string":
    if val == "i":
        break
    print(val)
    
print("FIN")

#CONTINUE:: Continua con la siguiente iteracion del ciclo

for num in range(2,10):
    if num%2==0:
        print(f'es numero par: {num}')
        continue #HACER UNA PRUEBA QUITANDO ESTO PARA VER QUE PASA
    print(f'Es numero impar: {num}')
    