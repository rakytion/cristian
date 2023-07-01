#Solicitar al usuario un numero de cliente. Si el numero es el 1000, imprimir ganaste un premio

"""
x=int(input("ingrese: "))

if x>1000:
    print("ganaste un premio")
else:
    print("perdedor")
"""

#ingrese dos numeros y mustre cual es el menor
"""
a=int(input("ingrese primer numero: "))
b=int(input("ingrese segundo numero: "))
if a>b:
    print(b," es menor")
else:
    print(a, "es menor")
"""
#ingrese dos numeros y mustre cual es el menor, considerar si son iguales
"""
c=int(input("ingrese primer numero: "))
d=int(input("ingrese segundo numero: "))
if c>d:
    print(d," es menor")
elif c<d:
    print(c, "es menor")
else:
    print("son iguales")
"""
#Pedir 10 numeros y decir cual es el mayor
"""
x=int(input("CANTIDAD DE NUMEROS"))
contador=0
mayor=0
menor=0
suma=0
while True:
    if x==contador:
        break
    y=int(input("ingresar numero"))
    contador=contador +1

    if menor==0:
        menor=y
    elif y>mayor:
        mayor=y
    elif y<menor:
        menor=y


    suma=suma+y
    prom=suma/x

print("promedio", prom)
print("menor", menor)
print("mayor", mayor)
"""

#cmomusar el while
"""
x=20
while x>10:
    print("hola")
    x-=1
    if x==13:
        break
    
"""

#crear un bucle que sume y mnuestre del 100 al 200
"""
x=100
suma=0

while x<=200:
    print(x)
    suma=suma+x
    x+=1
print(suma)
"""
#crear u ciclo infinito,
"""
while True
    print("hola")
"""

#escriba un programa que pregunte una y otra vez un programa a no ser que escribas si

#crea una tupla con numero, pide numero por teclado e indica cuantas veces se repite
# tupla=(1,2,5,1,5,0,65,1,5,1,51,54)
# contar=int(input("ingrese numero a recontar: "))
# conteo=0
# for numero in range(len(tupla)):
#     if tupla(numero)==contar:
#         conteo+=1
# print(conteo)

# diccionario={"criss":8, "juan":4,"perro":2}
# print (diccionario{"criss"})
# diccionario["criss"]=5
# print(diccionario)

# def MostrarMensaje(X):
#     global juan
#     juan=1
#     print(f"Hola {X}")
# juan=2
# MostrarMensaje("nico")
# MostrarMensaje("seba")
# print(juan)
#f sirve para cpncatenar

# def suma2numeors(numero1, numero2):
#     suma=numero1+numero2
#     return suma
# resultado=suma2numeors(2,4)
# print(resultado)


#upper y lower
# palabra="hola"
# print(palabra.upper())
# #strip o lstrip izquieda rstrip derecha
# palabra="    hola      "
# print(palabra.strip())


# def suma2numeors(numero1, numero2=2):
#     suma=numero1+numero2
#     return suma
# resultado=suma2numeors(2,)
# print(resultado)
