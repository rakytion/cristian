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
# import desafiopruebas as c

# import desafiopruebas
# desafiopruebas.saludar()


# file=open("librerias.txt","w")
# file.write("perro")
# file.close()

# file=open("librerias.txt","r")
# print(file.read())


#Clase 22/7 OBJETOS
# class vehiculo:
#     def __init__(self,motor,ruedas):
#         self.motor=motor
#         self.ruedas=ruedas
#     def arrancar(self):
#         print("brumm")
# class auto(vehiculo):
#     velocidad=10
#     color="rojo"
#     claxon="turuturu"
#     modelo="1"
#     def __init__(self,claxon,color,velocidad,modelo,motor, ruedas):
#         self.claxon=claxon
#         self.velocidad=velocidad
#         self.color=color
#         self.modelo=modelo
#         super().__init__(motor,ruedas)
#     def arrancar(self):
#         print("brumm")
#     def tocarclaxon(self):
#         print(self.claxon)
#     def __str__(self):
#         return f"el auto es de color{self.color}, modelo {self.modelo},etc"
#     def dicc(self):
#         print(vars(self))
# miautito=auto("tururu","rojo",12,"3",4,5)
# miautito.tocarclaxon()
# miautote=auto("pipi", "verde",15,"2",2,4)
# miautote.tocarclaxon()
# miautito.dicc()

#crear un gato 5 atributos nombre collor de pelo color de ojos cansancio y hambre y 
# 4 metodos comer dormir jugar acariciar. instanciar 3 objetos

class gato():
    def __init__(self, nombre, pelo, ojos, cansancio, hambre):
        self.nombre=nombre
        self.pelo=pelo
        self.ojos=ojos
        self.cansancio=cansancio
        self.hambre=hambre
    def comer(self):
            print(self.nombre,"Tiene de hambre: ",self.hambre)
            print("*Empieza a comer..* ñam ñam ñam")
    def dormir(self):
            print(self.nombre,"tenia mucho sueño: ",self.cansancio,"sus ojos: ",self.ojos,"se cierran.. *Se tira a dormir* ..Zzzzzz..")
    def jugar(self):
            print(f"{self.nombre} su pelo:{self.pelo}* se eriza yse pone en alerta* *rasgunazo*")
    def acariciar(self):
            print(f"{self.nombre} cierra sus ojos color {self.ojos}, se acurruca..prrr prrr prrr..")

gato1=gato("juan","Marron","celestes",5,10)
gato2=gato("Pedro","blanco","verdes",4,5)
gato3=gato("Peluza","gris","marrones",3,6)

gato1.comer()
gato2.comer()
gato3.comer()
gato1.dormir()
gato2.dormir()
gato3.dormir()
gato1.acariciar()
gato2.acariciar()
gato3.acariciar()

