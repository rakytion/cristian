
p=str(input("INGRESAR CANTIDAD DE NUMEROS A EVALUAR: "))

if float(p):
    pass
else:
    print("error")

x=float(p)


while x<0:
    print("INGRESAR CANTIDAD DE NUMEROS A EVALUAR (NUMERO POSITIVO)")
    x =int(input("INGRESAR CANTIDAD DE NUMEROS A EVALUAR: "))

if x==0:
        print("promedio 0")
        print("menor 0 ")
        print("mayor 0 ")

cantidad= x//1
contador=0

suma=0
while True:
    if cantidad==contador:
        break
    y=float(input("ingresar numero: "))
   
    contador=contador +1

    if contador==1:
        menor=y
        mayor=y
    elif y>mayor:
        mayor=y
    elif y<menor:
        menor=y

    suma=suma+y
      
if x>0:
    prom=suma/x
    print("promedio", prom)
    print("menor", menor)
    print("mayor", mayor)
    
