from NodoFilas import filas
from ListaFilas2 import listafilas2
fila2=listafilas2()
class listafilas:
 def __init__ (self):
     self.cabeza=None
 def insertar(self,x,y,p,valor):
     nuevo=filas(x,y,p,valor)
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
         print("x: "+tmp.x+" Y: "+tmp.y+" Valor: "+tmp.valor+" P: "+tmp.p)
         print("-------------")
         tmp=tmp.siguiente
 def insertar2(self):
     tmp=self.cabeza
     while tmp is not None:
         a=0
         b=tmp.x
         c=tmp.y
         d=tmp.p
         e=tmp.valor
         if int(tmp.valor)!=0:
             a=1     
         fila2.insertar(b,c,d,e,a)
         tmp=tmp.siguiente
         
 
