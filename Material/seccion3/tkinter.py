def decimal(numbin):
    numbin=str(numbin)
    decimal=0
    exp=len(numbin)-1
    for i in numbin:
        decimal +=(int(i)*2**(exp))
        exp=exp-1
    return decimal

entrada=input("ingrese numero binario:")
conv=decimal(entrada)
print(f" {entrada}  su coversion es: {conv} a numero entero")