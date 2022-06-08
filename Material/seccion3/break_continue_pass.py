""" PASS-> La declaración  pass no hace nada."""

"""while True:
    pass

class  hola:
    pass"""

"""  BREAK -> El ciclo while(false) o for(Agotamiento) es terminado  break """

for val in "string":
    if val =="i":
       break
    print(val)
     
print("fin")
    
"""  CONTINUE -> Continúa con la siguiente iteración del ciclo """

for num in range(2,10):
    if num%2==0:
        print(f"es numero es par {num}")
        continue
    print(f"es un numero impar {num}")
    


    