"""EJERCICIO2: TIEMPO DEL RELOJ DEL PROCESADOR 
   time: devuelve el tiempo del reloj del procesador
   hashlib: permite realizar cifrados directamente en python BLAKE, SHAKE, SHA1, SHA224, SHA256, SHA384, SHA512 y MD5. """

import time
import hashlib

data=open(__file__,'rb').read()

for i in range(10):
    h=hashlib.sha1()
    print(time.ctime(),':{:0.3f} {:0.3f}'.format(time.time(),time.clock()))
    for i in range(300000):
        h.update(data)
    cksum= h.digest()