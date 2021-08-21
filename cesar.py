clave = input("ingrese clave: ")
while True:#controlo que se ingrese un valor valido
    paso = int(input ("ingrese paso entre 1 y 25: "))
    if paso < 25 and paso > 1:
        break
    print( "ha ingresado un valor invalido")

code= " "
listacesar= list(clave)
for letra in listacesar:
    if not letra.isalpha():#quito espacios
        if letra.isdigit():# si es numero lo agrego
            code += letra
            continue
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
    
         
            





   
