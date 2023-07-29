#contdor de palabras
def separadorpalabras():
    #en -lista- guardaremos las palabras del texto en una lista, para luego poder contarlas y agregarlas al diccionario, -vacio- y -palabra- nos ayudaran con eso
    #en diccionario guardaremos las palabras ya contadas con -posicion- eligiremos la palabra a contar y en -repeticiones- guardaremos la cantidad de repeticiones de la palbra
    lista=[]
    vacio=" "
    palabra=""
    diccionario={}
    posicion=0
    repeticiones=1
    for i in range (len(texto)):
        if texto[i]!= vacio:
         palabra+=texto[i]           
        else:
         lista.append(palabra)
         palabra=""
        if i==len(texto)-1:
         lista.append(palabra)
    while "" in lista:
          lista.remove("")
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
texto=input("ingresar texto: ")
separadorpalabras()