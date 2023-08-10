def redondear(numero):
    entero=numero//1
    decimales=numero-entero
    if decimales>0.5:
        entero+=1
    print (f"su numero redondeado es: {entero}")