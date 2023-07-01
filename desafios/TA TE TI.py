A=input("Jugador N°1 ingrese su nombre: ")
B=input("Jugador N2 ingrese su nombre: ")


primera=[" ","/"," ","/"," "]
segunda=[" ","/"," ","/"," "]
tercera=[' ','/',' ','/',' ']

print(primera)
print(segunda)
print(tercera)

while True:
    print("Jugador N°1: ",A)
    xcolumna=int(input("Ingresá N° Columna: "))
    xfila=int(input("Ingresá N° Fila: "))

    while xcolumna>3 or xfila>3 or xcolumna<1 or xfila<1:
        print("Elegir columna y fila del 1 al 3")
        xcolumna=int(input("Ingrese nuevamente N° Columna"))
        xfila=int(input("Ingrese nuevamente N° Fila"))

        
    if xfila==1:
        if xcolumna==1:
            ocupa=primera.pop(0)
            if ocupa=="O" or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                primera.insert(0,ocupa)
            else:
                primera.insert(0,"X")
        elif xcolumna==2:
            ocupa=primera.pop(2)
            if ocupa=="O" or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                primera.insert(2,ocupa)
            else:
                primera.insert(2,"X")
        elif xcolumna==3:
            ocupa=primera.pop(4)
            if ocupa=="O" or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                primera.insert(4,ocupa)
            else:
                primera.insert(4,"X")
    elif xfila==2:
        if xcolumna==1:
            ocupa=segunda.pop(0)
            if ocupa=="O"or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                segunda.insert(0,ocupa)
            else:
                segunda.insert(0,"X")
        elif xcolumna==2:
            ocupa=segunda.pop(2)
            if ocupa=="O" or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                segunda.insert(2,ocupa)
            else:
                segunda.insert(2,"X")
        elif xcolumna==3:
            ocupa=segunda.pop(4)
            if ocupa=="O"or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                segunda.insert(4,ocupa)
            else:
                segunda.insert(4,"X")
    elif xfila==3:
        if xcolumna==1:
            ocupa=tercera.pop(0)
            if ocupa=="O"or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                tercera.insert(0,ocupa)
            else:
                tercera.insert(0,"X")
        elif xcolumna==2:
            ocupa=tercera.pop(2)
            if ocupa=="O"or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                tercera.insert(2,ocupa)
            else:
                tercera.insert(2,"X")
        elif xcolumna==3:
            ocupa=tercera.pop(4)
            if ocupa=="O"or ocupa=="X":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                tercera.insert(4,ocupa)
            else:
                tercera.insert(4,"X")
        
    print(primera)
    print(segunda)
    print(tercera)

    print("Jugador N°2: ",B)
    ocolumna=int(input("Ingrese N Columna: "))
    ofila=int(input("ingrese N Fila: "))

    while ocolumna>3 or ofila>3 or ocolumna<1 or ofila<1:
        print("Elegir columna y fila del 1 al 3")
        ocolumna=int(input("Ingrese nuevamente N° Columna"))
        ofila=int(input("Ingrese nuevamente N° Fila"))

    if ofila==1:
        if ocolumna==1:
                ocupa=primera.pop(0)
                if ocupa=="X" or ocupa=="O":
                    print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                    primera.insert(0,ocupa)
                else:
                    primera.insert(0,"O")
        elif ocolumna==2:
            ocupa=primera.pop(2)
            if ocupa=="X" or ocupa=="O":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                primera.insert(2,ocupa)
            else:
                primera.insert(2,"O")
        elif ocolumna==3:
            ocupa=primera.pop(4)
            if ocupa=="X" or ocupa=="O":
                    print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                    primera.insert(4,ocupa)
            else:
                primera.insert(4,"O")
    elif ofila==2:
        if ocolumna==1:
            ocupa=segunda.pop(0)
            if ocupa=="X" or ocupa=="O":
                    print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                    segunda.insert(0,ocupa)
            else:
                segunda.insert(0,"O")
        elif ocolumna==2:
            ocupa=segunda.pop(2)
            if ocupa=="X" or ocupa=="O":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                segunda.insert(2,ocupa)
            else:
                segunda.insert(2,"O")
        elif ocolumna==3:
            ocupa=segunda.pop(4)
            if ocupa=="X" or ocupa=="O":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                segunda.insert(4,ocupa)
            else:
                segunda.insert(4,"O")
    elif ofila==3:
        if ocolumna==1:
            ocupa=tercera.pop(0)
            if ocupa=="X" or ocupa=="O":
                print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                tercera.insert(0,ocupa)
            else:
                tercera.insert(0,"O")
        elif ocolumna==2:
            ocupa=tercera.pop(2)
            if ocupa=="X" or ocupa=="O":
                 print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                 tercera.insert(2,ocupa)
            else:
                tercera.insert(2,"O")
        elif ocolumna==3:
            ocupa=tercera.pop(4)
            if ocupa=="X" or ocupa=="O":
                 print("No puedes usar un lugar ya ocupado, Pierdes el turno")
                 tercera.insert(4,ocupa)
            else:
                tercera.insert(4,"O")
            
    print(primera)
    print(segunda)
    print(tercera)

    total=primera+segunda+tercera
    if total[0] == total[2] == total[4] or total[5] == total[7] == total[9] or total[10] == total[12] == total[14]:
        print("El ganador es: ")
    elif total[0] == total[5] == total[10] or total[2] == total[7] == total[14] or total[4] == total[9] == total[14]:
        print("El ganador es: ")
    elif total[0] == total[7] == total[14] or total[4] == total[7] == total[10]:
        print("El ganador es: ")