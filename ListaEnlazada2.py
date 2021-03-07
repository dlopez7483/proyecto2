from NodoMatriz2 import matriz2
class listaenlazada2:
 def __init__ (self):
     self.cabeza=None
 def insertar(self,m,n,nombre,p,Filas2):
     nuevo=matriz2(m,n,nombre,p,Filas2)
     if self.cabeza is None:
         self.cabeza=nuevo
     else:    
         tmp=self.cabeza
         while tmp.siguiente is not None:
             tmp = tmp.siguiente
         tmp.siguiente=nuevo 
 def Mostrar2(self):
     tmp=self.cabeza
     while tmp is not None:
         print("M: "+tmp.m+"N: "+tmp.n+"Nombre: "+tmp.nombre+"p: "+tmp.p)
         tmp=tmp.siguiente