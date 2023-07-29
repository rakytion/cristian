#Pedir 10 o mas numeros y decir cual es el mayor, menor y el promedio
x =input("INGRESAR CANTIDAD DE NUMEROS A EVALUAR: ")
while True:
    try:
        x=float(x)
    except ValueError:
        print("Solo ingresar NUMEROS, ENTEROS Y POSITIVOS")
        x =input("INGRESAR CANTIDAD DE NUMEROS A EVALUAR: ")
    else:
        if x<1:
            print("Solo ingresar NUMEROS, ENTEROS Y POSITIVOS")
            x =input("INGRESAR CANTIDAD DE NUMEROS A EVALUAR: ")
        else:
         break

cantidad= x//1

contador=0
suma=0
while contador!=cantidad:
    n=input("ingresar numero: ")
    while True:
        try:
            n=float(n)
        except ValueError:
            print("Solo ingresar NUMEROS")
            n=input("ingresar valor nuevamente: ")
        else:
            break

    contador=contador +1
    
    if contador==1:
        menor=n
        mayor=n
    elif n>mayor:
        mayor=n
    elif n<menor:
        menor=n

    suma=suma+n
    
prom=suma/cantidad
print("promedio", prom)
print("menor", menor)
print("mayor", mayor)
    
