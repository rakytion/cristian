#escriba una funcion que muestre todos los numeros primos entre 1 y un numero n que es ingresado por parametro

# def determinarprimo(x):
#     while True:
#      if x==1 or x==0:
#       return False
#      for i in range(2,x+1):
#        div=x//i
#        multi=div*i
#        if x==multi:
#         if x==i:
#           return True
#         else:
#           return False
#      break

# lista=[]
# limite=int(input("Ingrese hasta que numero desea mostrar los numeros primos: "))
# for i in range(limite):
#   determinado=determinarprimo(i)
#   if determinado:
#     lista.append(i)
# print(lista)

#Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta que el usuario ingrese ‘salir’

# def sandwich():
#     condimentos=[]
#     while True:
#      elegidos=input("escriba aqui sus aderezos: ")
#      elegidos=elegidos.lower()
#      if elegidos=="salir":
#       print(f"sus condimentos son: {condimentos}")
#       break
#      else:
#       print("ya se agrego el condimento")
#       condimentos.append(elegidos)
# print("Que condimentos desea? en caso de no desear nada o terminar de elegir escriba -salir")
# sandwich()



# def sandwich():
#     condimentos=[]
#     while True:
#      elegidos=input("escriba aqui sus aderezos: ")
#      condimentos.append(elegidos)
#      print("ya se agrego el condimento")
#      deseo=input("Desea agregar mas condimentos? responda SI/NO: ")
#      deseo=deseo.upper()
#      if deseo=="NO":
#       print(f"sus condimentos son: {condimentos}")
#       break
# print("Que condimentos desea?")
# sandwich()

#Remera: Escriba una función “hacer_remera()” que tome como parámetros un tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez usando argumentos por posición. Llámela una segunda vez usando argumentos por clave

# def hacer_remera(tamaño, mensaje):
#     print(f"Su remera en talle {tamaño} dira el siguiente mensaje: {mensaje}")
# hacer_remera("M", "just do it")
# hacer_remera(mensaje="Phitonic", tamaño= "L")

#Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los 
#valores por defecto, y la segunda con valores diferentes. 

# def hacer_remera(tamaño="L", mensaje="Me gusta Python"):
#     print(f"Su remera en talle {tamaño} dira el siguiente mensaje: {mensaje}")
# hacer_remera()
# hacer_remera(mensaje="Phitonic", tamaño= "XL")

#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 

def fibonacci(n):
    lista=[0,1,]
    num=1
    numanterior=0
    while True:
     resultado=num+numanterior
     if n<=resultado:
      print(lista)
      break
     lista.append(resultado)
     numanterior=num
     num=resultado
       

limite=int(input("Ingrese hasta donde desea ver la serie Fibonacci: "))
fibonacci(limite)
