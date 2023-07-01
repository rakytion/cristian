traductormorse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
texto=input("ingresar texto a traducir a codigo Morse: ")
lista=[]
lista2=[]
vacio=" "
for i in range(len(texto)):
  lista.append(texto[i])
  while vacio in lista:
    lista.append("/")
print(lista)
