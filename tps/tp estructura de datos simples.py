#mostrar en pantallas num del 1 al 20 y luego rango de usuario
# lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(lista)

#Rango del usuario

# inicio=int(input("ingrese inicio del rango: "))
# fin=int(input("ingrese fin del rango: "))
# lista=[]
# for numero in range(inicio, fin+1):
#     lista.append(numero)
# print(lista)

#pedir numero y guardar tabla de multiplicar

# valor=int(input("ingrese un numero: "))
# lista=[]
# for numero in range(1,11):
#     tabla=valor*numero
#     lista.append(tabla)
# print(lista)

#pide cadena str y meter caracter sin que se repitan

# palabras=input("ingrese palabras: ")
# lista=[]
# for i in range(len(palabras)):
#         if palabras[i] not in lista:
#             lista.append(palabras[i])
# print(lista)

#pide cadena str y meter caracter en una lista sin espacios

# palabras=input("ingrese palabras: ")
# lista=[]
# vacio=" "
# for i in range(len(palabras)):
#         lista.append(palabras[i])
#         while vacio in lista:
#           lista.remove(vacio)
# print(lista)

#crear una tupla con num, pid un num po teclado e indica cuantas veces se repite

# conjunto=(0,2,4,3,5,64,3,2,3,4,5,6)
# elegido=int(input("elige numero a buscar:"))
# conteo=0
# for numero in range(len(conjunto)):
#     if conjunto[numero]==elegido:
#         conteo+=1
# print("Hay ",conteo,"veces el numero ", elegido)

#meses del año

# año=("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE")
# while True:
#     mes=int(input("Ingresar numero del mes que desea visualizar: "))
#     if mes==0:
#         break
#     elif mes<0 or mes>12:
#         print("Eror ingrese numero nuevamente")
#     else:
#         print("Corresponde al mes: ",año[mes-1])
#         break

#tupla con numeros indicar mayor menor

# lista=(12,432,54,32,3,43,11,23,61,58,5,17,156,16,2,7,18)
# menor=lista[0]
# mayor=lista[0]
# for numero in range(len(lista)):
#     if lista[numero]<menor:
#         menor=lista[numero]
#     elif lista[numero]>mayor:
#         mayor=lista[numero]
# print(lista)
# print("menor es:", menor)
# print("mayor es:", mayor)

#agenda telefonica


# agenda={"amor1":3871616844,"amor2":3884785963,"amor3":3864154236,"amor4":3879845976}
# while True:
#     print("Bienvenido a su Agenda")
#     print("Para salir marque: *")
#     contacto=input("Ingrese contacto a buscar: ")
#     if contacto=="*":
#         break
#     if contacto not in agenda:
#         print("el contacto no existe")
#         print("agregar numero telefonico de ", contacto)
#         nuevocontacto=input("ingrese numero: ")
#         if nuevocontacto=="*":
#             break
#         agenda[contacto]=nuevocontacto
#         print("Se agrego el contacto exitosamente")
#     else:
#         print(agenda[contacto])
#         print("desea cambiar el numero de contacto?")
#         respuesta=input("responder SI o NO: ")
#         if respuesta=="si":
#             nuevonumero=input("Ingrese nuevo numero:")
#             if nuevonumero=="*":
#                 break
#             agenda[contacto]=nuevonumero
#             print("Se cambio el numero exitosamente")
#         elif respuesta=="*":
#             break
# print("saliendo de Agenda")

#pide numeros en lista cuando el usuario meta un 0 cortar ymostrar de mayor a menor

# listado=[]
# listamax=[]
# while True:
#     numeros=float(input("ingrese numeros: "))
#     if numeros==0:
#         break
#     listado.append(numeros)

# for numero in range(len(listado)):
#     maximo=max(listado)
#     listado.remove(maximo)
#     listamax.append(maximo)
# print(listamax)

#pide numeros en lista cuando el usuario meta un 0 cortar ymostrar de menor a mayor

# listado=[]
# listamin=[]
# while True:
#     numeros=float(input("ingrese numeros: "))
#     if numeros==0:
#         break
#     listado.append(numeros)

# for numero in range(len(listado)):
#     minimo=min(listado)
#     listado.remove(minimo)
#     listamin.append(minimo)
# print(listamin)

#traductor morse

# traductormorse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
# texto=input("ingresar texto a traducir a codigo Morse: ")
# lista=[]
# vacio=" "
# for i in range(len(texto)):
#   if vacio in texto[i]:
#     lista.append("/")
#   else:lista.append(traductormorse[texto[i]])
# print(lista)

