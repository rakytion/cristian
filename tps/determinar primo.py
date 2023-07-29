#escriba una funcion que muestre todos los numeros primos entre 1 y un numero n que es ingresado por parametro

# x=int(input("ingrese un numero: "))
# for numero in range(1,x+1):
#     resultado=x//numero
#     preuba=resultado*numero
#     if :
#         print(numero)
while True:
    x=int(input("ingrese un numero: "))
    for numero in range(2,x+1):
        div=x//numero
        multi=div*numero
        if x==multi:
            if x==numero:
                primo=True
            else:primo=False
            break
    print(primo)