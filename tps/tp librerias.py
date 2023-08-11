#Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el 
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior (3).

# def redondear(numero):
#     entero=numero//1
#     decimales=numero-entero
#     if decimales>0.5:
#         entero+=1
#     print (f"su numero redondeado es: {entero}")
# x=float(input("Ingrese un numero: "))
# redondear(x)

#Coloque el módulo del ejercicio anterior dentro de un paquete. En un modulo que esté fuera de ese paquete, cree una función de suma de 
#decimales que redondee el resultado haciendo uso de la función redondear() del paquete recién creado.

# from modulo import modulo1
# while True:
#     primernum=float(input("ingrese primer numero: "))
#     segnum=float(input("ingrese segundo numero: "))
#     suma=primernum+segnum
#     modulo1.redondear(suma)

#progama que muestre la fecha y hbora actual

# import datetime
# hoy=datetime.datetime.now()
# formato= "%Y-%m-%d %H:%M:%S"
# fecha=hoy.strftime(formato)
# print(fecha)

#programa que de numero al azar

# import random
# while True:
#     numalea= random.randint(2,8)
#     print(numalea)

#Bola mágica: La bola mágica (Magic 8 ball)

# import random
#print("piense en la pregunta que desea que la bola magica le responda")
# eleccion=random.randint(0,7)
# mensajes=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
# print(mensajes[eleccion])

#. Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)
# import time
# import random

# inicio=time.time()

# print("piense en la pregunta que desea que la bola magica le responda")
# for i in range(100):
#     #haciendo tiempo c:
#     print("...")
# eleccion=random.randint(0,7)
# mensajes=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
# print(mensajes[eleccion])

# final=time.time()
# print(f"Eltiempo de ejecucion es: {final - inicio} ")