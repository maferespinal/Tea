maximo = 0
mínimo = 999
while True:
 try:
     numero = input("Por favor ingrese un numero/n>>>")
     if(numero == "done"):
        break
     else:
        if int(máximo) < int (numero): 
           máximo = numero
        if int(minimo) > int(numero):
           minimo = numero
 except:
    print("Ingrese valores válidos")
    continue
print("maximo:"+ str(maximo))
print("minimo:"+ str(mínimo))