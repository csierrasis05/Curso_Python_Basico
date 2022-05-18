#EJERCICIO 2: Visualizar tiempo reloj del procesador
#time: devuelve tiempo procesador
#hashlib: Permite realizar cifrados directamente en Python. Llaves secretas

import time
import hashlib

data = open(__file__,'rb').read()

for i in range(10):
    h = hashlib.sha1()
    print(time.ctime(),':{:0.3f} {:0.3f}'.format(time.time(),time.clock()))
    for j in range(300000):
        h.update(data)
    cksum = h.digest()
