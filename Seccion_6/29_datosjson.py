import json

datos = {'name':'Carlos',
         'edad':32,
         'ciudad':'Medellin'
         }

#Forma Simple
datosjson = json.dumps(datos)
print(datosjson)


#guardar un archivo Json
with open('datos1.json','w') as f:
    json.dump(datos,f)
    

#Leer una archivo Json
with open('datos1.json','r') as f:
    cadenajson = json.load(f)

print(cadenajson)