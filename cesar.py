clave = input("ingrese clave: ")
paso = int(input ("ingrese paso: "))
code= " "
listacesar= list(clave)
for letra in listacesar:
    if not letra.isalpha():
        continue    
    #if letra == "z":
    #    code +=chr(ord("a") + (paso-1))
    numero = ord(letra) + paso
    if numero > ord("z"): # controlo si pasa de z para volver a sumar desde a
        numero = numero - ord("z")
        code += chr(ord("a") + (numero-1))
        continue
    code += chr(ord(letra)+ paso)

    
print(code)
    
         
            





   
