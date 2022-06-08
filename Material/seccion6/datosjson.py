import json

datos ={ "name":"juan",
        "edad":23,
        "ciudad":"lima"}

datosjson= json.dumps(datos)
print(datosjson)

with open("datos1.json","w") as f:
    json.dump(datos,f)

with open("datos1.json","r") as f:
    cadenajson = json.load(f)    
    print(cadenajson)
    

