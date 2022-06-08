# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:09:46 2022

@author: carlsier
"""
import requests

#res = requests.get('https://sumaktec.com')
#print(res.text) #Trae todo el HTML de la pagina
#print(res.headers) #Trae la cabecera de la pagina
#print(res)  #Trae el codigo 200 exito, 400 error, 500 paginas no encontradas
#print(res.raw.read(10))


res = requests.get('https://cdn-images.motor.es/image/m/694w/fotos-noticias/2018/12/min652x435/dodge-demon-venta-gran-bretana-201853104_1.jpg')
res.raise_for_status()

with open('imagen1.jpg','wb') as fd:
    for imagen in res.iter_content(chunk_size=5000):
        print('Imagen recibida')
        fd.write(imagen)