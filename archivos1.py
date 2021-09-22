from os import strerror

try:
    archivo = input ("Ingrese nombre de archivo: ")
    f = open(archivo, 'rt')
    lista = f.readline()
    cont = 0
    abc = {
        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'ñ':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
    }
    for letra in lista:
        letra= letra.lower() #paso a minuscula las  letras mayuscula
        if abc [letra] != None:
            abc[letra] +=1
    f.close()
    for k,v in abc.items():
        if abc[k]!= 0:
            print("%s -> %s" %(k,v)) # doy formato clave -> valor a la salida

except IOError as e:
    print("EL archivo no se puede abrir o no existe",strerror(e.errno))