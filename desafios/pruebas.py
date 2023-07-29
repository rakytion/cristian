#encontrar primer caracater que no se repita
# caracter=input("Ingrese texto: ")
# posicion=0
# repeticiones=0
# while True:
#     for i in range (len(caracter)):
#         print(i)
#         if posicion!=i and caracter[posicion]==caracter[i]:
#          repeticiones+=1
#     if repeticiones==0:
#         print("El primer caracter que no se repite es: ",caracter[posicion])
#         break
#     else:
#         posicion+=1
#         repeticiones=0

#contdor de palabras
def separadorpalabras():
    lista=[]
    vacio=" "
    palabra=[]
    diccionario={}
    posicion=0
    repeticiones=1
    for i in range (len(texto)):
        if texto[i]!= vacio:
         palabra+=texto[i]           
        else:
         lista+=palabra
         palabra=[]
        if i==len(texto)-1:
         lista.append(palabra)
    while "" in lista:
          lista.remove("")
    print(lista)
    while True:
        for j in range(len(lista)):
            if posicion!=j and lista[posicion]==lista[j]:
             repeticiones+=1
        diccionario[lista[posicion]]= repeticiones
        posicion+=1
        repeticiones=1
        if posicion>len(lista)-1:
         print(diccionario)
         break
texto="ingresar texto: "
separadorpalabras()