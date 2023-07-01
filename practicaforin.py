#clase 10/6
"""
for numero in range(10):
    print(numero)

for numero in range(10,20):
    print(numero)

for numero in range(1,20,3):
    print(numero)

for numero in range(1,20,3):
    print(numero)
"""
#pide numero muestra tabla de multiplicar del 1 al 10
"""
x=int(input("ingrese un numero"))
for numero in range (0,11):
    print(x*numero)
"""
"""
x=int(input("ingrese un numero"))
c=int(input("cantidad de multiplos a mostrar"))
for numero in range (0,c+1):
    print(x*numero)
"""
#bucle que sume y muestre del 100 al 200
"""
x=100
suma=0
for numero in range(x,201):
    print(x)
    suma=x+suma
    x+=1
print(suma)
"""
#lista en la lista se comienza a contar desde 0 en adelante o desde el final usando el indice negativo
lista=[1,2,3,4,5]
print(lista[3])

palabra="palabra"
print(palabra[2])

lista1=[1,2,[245, "l",3],4,5]
print(lista1[2])

lista3=[1,2,3,4,5]
print(len(lista3))

lista4=[1,2,3,4,5]
print(lista[0:4])

lista4=[1,2,3,4,5]+[33,55,64]
print(lista[2:])

#funcion append
lista=[1,2,3,4,5]
lista.append(6)
print(lista)

#funcion insert
lista=[1,2,3,4,5]
lista.insert(2,"g")
print(lista)

#.extend para sumar lista
#.remove
lista=[1,2,3,"g",4,5]
lista.remove("g")
print(lista)
#pop
lista=[1,2,3,"g",4,5]
lista.pop()
print(lista)
#.remove
lista=[1,2,3,"g",4,"g",5]
while "g" in lista:
    lista.remove("g")
print(lista)

#meter los numeros del 1al35 y mostrarla en pantalla. hacer lo mismo para un rango de tiempo indicado por un usuario
"""
lista=[]
for numero in range (1,36):
    lista.append(numero)
print(lista)
"""
"""
cantidad=int(input("ingrese final"))
lista=[]
for numero in range (1,cantidad+1):
    lista.append(numero)
    print(lista)
"""
#pide una cadena de string por teclado mete los caracteres en una lista sin espacios
"""
palabra=input("ingrese texto: ")
lista=[]
for numero in range(len(palabra)):
    lista.append(palabra[numero])
print(lista)
"""
"""
lista=[0,1,2,3,4,5,6,7,8,9]
for numero in range(len(lista)):
   print(lista[numero])
"""

lista=[]
for numero in range(10):
    numeros=float(input("ingresar numeros: "))
    lista.append(numeros)
menor=lista[0]
for numero in range(len(lista)):
    if lista[numero]<menor:
        menor=lista[numero]
print(lista)
print("menor es:", menor)


"hola como estas"
#[h,o,l,a,c,o,m,o ] Todo entre ""
a=input("ingresar una palabra: ")
print(a[2])
lista=[]
vacio=" "
for i in range(len(a)):
    lista.append(a[i])
print(lista)
while vacio in lista:
    lista.remove(vacio)    
print(lista)


#realizar un programa que inicialice  una lista de 10 valores

#funcion index

lista=[1,2,5,4,5]
print(lista.index(5))

#lista="holaa"
#print(lista.find(3))