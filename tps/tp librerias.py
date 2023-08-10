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

from modulo import modulo1
while True:
    primernum=float(input("ingrese primer numero: "))
    segnum=float(input("ingrese segundo numero: "))
    suma=primernum+segnum
    modulo1.redondear(suma)

