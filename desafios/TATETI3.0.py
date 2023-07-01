#Presentacion
print("EL FAMOSO Y POPULAR JUEGO DEL TA-TE-TI")
print("Listos para jugar??")
#ingreso de nombres de jugadores
A=input("Jugador N°1 ingrese su nombre: ")
B=input("Jugador N2 ingrese su nombre: ")
#muestra de tablero, 3 variables del tipo lista que serviran de tablero
print("Este será su tablero!")
primera=[" ","/"," ","/"," "]
segunda=[" ","/"," ","/"," "]
tercera=[' ','/',' ','/',' ']

print(primera)
print(segunda)
print(tercera)

#La variable contador y div, nos serviran para determinar los turnos de cada jugador, determinando si contador es par/impar
#Comienza el jugador 1 (Variable A) impar y el jugador 2 será la (variable B) par
contador=1
div=1

#la variable repechaje nos ayudara a repetir el turno del jugador en caso de que elija un lugar no disponible
repechaje=0
while True:
    if repechaje==1:            #Cada vez que alguien elija un lugar no disponible repechaje=1 
        contador-=1             #entonces restamos 1 al contador para repetir el turno del jugador
        repechaje=0
    if contador != div*2:       #Si el contador es impar juega el jugador 1 (A)
        turno=A
        simbolo="X"
    else:                       #Si el contador es par juega el jugador 2 (B)
        turno=B
        simbolo="O"
   
    #calculo para llevar el contador y la div para determinar el par/impar despues
    contador+=1
    div=contador//2

    #segun sea par/impar la variable turno me permitira cambiar entre cada jugador y su respectivo simbolo
    print("Le toca a:",turno, "juega la ficha: ", simbolo)
    xcolumna=int(input("Ingresá N° Columna: "))
    xfila=int(input("Ingresá N° Fila: "))

    #op por si ingresan un numero fuera del rango de mi matriz
    while xcolumna>3 or xfila>3 or xcolumna<1 or xfila<1:
        print("Elegir columna y fila del 1 al 3")
        xcolumna=int(input("Ingrese nuevamente N° Columna"))
        xfila=int(input("Ingrese nuevamente N° Fila"))

    # rastreamos la ubicacion primero por fila y luego por columna
    # luego preguntamos si ya esta ocupada esa ubicacion
    # si ya esta ocupada: repechaje=1 y contador-=1 para poder repetir el turno y elija nuevamente
    # si no esta ocupada: eliminamos el espacio vacio y colocamos el simbolo correspondiente
    if xfila==1:
        if xcolumna==1:
            if primera[0]=="O" or primera[0]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                primera.pop(0)
                primera.insert(0,simbolo)
        elif xcolumna==2:
            if primera[2]=="O" or primera[2]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1    
            else:
                primera.pop(2)
                primera.insert(2,simbolo)
        elif xcolumna==3:
            if primera[4]=="O" or primera[4]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                primera.pop(4)
                primera.insert(4,simbolo)
    elif xfila==2:
        if xcolumna==1:
            if segunda[0]=="O"or segunda[0]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                segunda.pop(0)
                segunda.insert(0,simbolo)
        elif xcolumna==2:
            if segunda[2]=="O" or segunda[2]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                segunda.pop(2)
                segunda.insert(2,simbolo)
        elif xcolumna==3:
            if segunda[4]=="O"or segunda[4]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                segunda.pop(4)
                segunda.insert(4,simbolo)
    elif xfila==3:
        if xcolumna==1:
            if tercera[0]=="O"or tercera[0]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                tercera.pop(0)
                tercera.insert(0,simbolo)
        elif xcolumna==2:
            if tercera[2]=="O"or tercera[2]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                tercera.pop(2)
                tercera.insert(2,simbolo)
        elif xcolumna==3:
            if tercera[4]=="O"or tercera[4]=="X":
                print("No puedes usar un lugar ya ocupado, Elige nuevamente Fila y Columna")
                repechaje=1
            else:
                tercera.pop(4)
                tercera.insert(4,simbolo)
    #mostramos como queda el tablero con la jugada reciente
    print(primera)
    print(segunda)
    print(tercera)
    #la variable total nos ayudara a definir las jugadas ganadoras
    #la variable empate cuenta la cantidad de espacios vacios en el tablero
    total=primera+segunda+tercera
    empate=total.count(" ")
    #El if define las jugadas ganadoras, primer de 3en raya horizontales, el primer elif las 3enraya verticales
    #el segundo elif define las 3en raya diagonales y ultimo el empate 
    if total[0] == total[2] == total[4] !=" " or total[5] == total[7] == total[9] !=" "or total[10] == total[12] == total[14]!=" ":
        print("El ganador es: ",turno) 
        break
    elif total[0] == total[5] == total[10] !=" "or total[2] == total[7] == total[12]!=" " or total[4] == total[9] == total[14]!=" ":
        print("El ganador es: ",turno)
        break
    elif total[0] == total[7] == total[14] !=" " or total[4] == total[7] == total[10]!=" ":
        print("El ganador es: ",turno)
        break
    elif empate==0:
        print("ya no hay mas espacios disponibles para seguir jugando")
        print("EMPATE")
        break