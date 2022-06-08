#Ir descomntariando cada seccion ya que va creando archivos y carpetas que unas vez se crea
#lanzan error si se vuelve a ejecutar


import os

#SECCION 1

# #Creacion de carpeta
# os.makedirs('Carpeta_Creacion_Ejercicio_28') #Creacion de una carpeta
# print(os.listdir('./')) #permite Visualizar los archivos actuales que hay en una carpeta

#SECCION 2

# #Crear Archivos

# archivos = open('datos.txt','w') # w: (Escritura) para crear o describir un archivo, r: (Lectura) para poner que se va a utilizar mas adelante

# archivos.write('Hola Mundo \n')
# archivos.write('Carlos Sierra \n')
# archivos.write('Ing. de Sistemas\n')

#SECCION 3

# #Leer Archivo

# archivo1 = open('datos.txt', 'r')
# contenido = archivo1.read()
# print(contenido)
# archivo1.close()

#SECCION 4

#Leer archivo linea a linea

# archivo1 = open('datos.txt', 'r')
# linea = archivo1.readline()

# while linea != '':
#     print(linea, end = '')
#     linea = archivo1.readline()

# archivo1.close()
