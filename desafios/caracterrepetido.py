#encontrar primer caracater que no se repita

caracteres=input("ingresar texto: ")
#con -posicion- determinamos el caracter que vamos a comparar con el resto de caracteres,
# con -repeticiones- la cantidad de veces que se repite y -comparador- para ayudarnos a comparar con el resto de caracteres
posicion=0
repeticiones=0
comparador=0
while True:
    if posicion!=comparador and caracteres[posicion]==caracteres[comparador]:
         repeticiones+=1
         comparador+=1
    else:
         comparador+=1
    if comparador>len(caracteres)-1 and repeticiones==0:
            print("El primer caracter que no se repite es: ",caracteres[posicion])
            break
    if comparador>len(caracteres)-1:
        posicion+=1
        repeticiones=0
        comparador=0
    if posicion>len(caracteres)-1:
         print("No hay ningun caracter que no se repita")
         break

