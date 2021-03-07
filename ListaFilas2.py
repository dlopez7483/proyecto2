from NodoFilas2 import filas2
class listafilas2:
 def __init__ (self):
     self.cabeza=None
 def insertar(self,x,y,p,valor1,valor2):
     nuevo=filas2(x,y,p,valor1,valor2)
     if self.cabeza is None:
         self.cabeza=nuevo
     else:    
         tmp=self.cabeza
         while tmp.siguiente is not None:
             tmp = tmp.siguiente
         tmp.siguiente=nuevo  
 def Mostrar(self):
     tmp=self.cabeza
     while tmp is not None:
         a=tmp.x
         b=tmp.y
         c=tmp.valor1
         d=tmp.p
         e=tmp.valor2
         return "x: "+a+" Y: "+b+" Valor: "+c+"P: "+d+"Valor2: "+e
         tmp=tmp.siguiente