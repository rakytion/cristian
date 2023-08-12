#Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

# class rectangulo():
#     def __init__(self,base,altura):
#         self.base=base
#         self.altura=altura
#     def area(self):
#         print(f"El Area de su rectangulo es: {self.base+self.altura}")
# recp=rectangulo(5,8)
# recs=rectangulo(2,3)
# rectangulo.area(recp)
# rectangulo.area(recs)

#Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina

class mate():
    def __init__(self,estado,restante,cantidad):
        self.estado=estado
        self.restante=restante
        self.cantidad=cantidad

    def cebar(self):
        if self.estado=="lleno":
            print(f"El mate esta lleno, te quemaste  tequedan {self.restante} cebadas, tu mate esta {self.estado}")
        else:
            if self.restante<=0:
             self.estado="lleno"
             self.restante=0
             print("mate lavado cambiar yerba")
             print(f"listo, mate lleno  tequedan {self.restante} cebadas, tu mate esta {self.estado}")
            else:
             self.estado="lleno"
             self.restante-=1
             print(f"listo, mate lleno tequedan {self.restante} cebadas, tu mate esta {self.estado}")
             
             
    def beber(self):
       
       if self.estado=="lleno":
           if self.restante<=0:
             self.restante=0
             self.estado="vacio"
             print("bebiste un Mate")
             print(f"Advertencia el mate esta lavado, tequedan {self.restante} cebadas, tu mate esta {self.estado}")
             
           else:
            print("bebiste un Mate")      
            self.estado="vacio"
            print(f"El mate esta vacio, debes recargarlo tequedan {self.restante} cebadas, tu mate esta {self.estado}")
       else:
          print("El mate esta vacio, debes recargarlo")

mate1=mate("lleno",1,10)

mate.beber(mate1)
mate.cebar(mate1)
mate.beber(mate1)
mate.beber(mate1)
mate.cebar(mate1)
mate.beber(mate1)

#sacacorchos

class Corcho:
    def __init__(self, Bodega):
        self.Bodega=Bodega
    
    def __str__(self):
        return self.Bodega

class Botella:
    def __init__(self, Corcho:Corcho):
        self.CorchoDeBotella=Corcho

class Sacacorcho:
    def __init__(self):
        self.CorchoSacacorcho=None
    
    def Destapar(self,Botella:Botella):
        if self.CorchoSacacorcho==None:
            if Botella.CorchoDeBotella!=None:
                self.CorchoSacacorcho=Botella.CorchoDeBotella
                Botella.CorchoDeBotella=None
                print("Botella destapada")
            else:
                print("La botella ya esta destapada")
        else:
            print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")
            
    def Limpiar(self):
        if self.CorchoSacacorcho==None:
            print("El sacacorchos ya esta limpio")
        else:
            self.CorchoSacacorcho=None
            print("Sacacorcho limpiado")