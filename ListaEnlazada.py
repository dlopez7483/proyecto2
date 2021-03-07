from NodoMatriz import matriz
from ListaFilas import listafilas
from ListaEnlazada2 import listaenlazada2
from ListaFilas2 import listafilas2
lista2=listafilas2()
lista=listaenlazada2()
class listaenlazada:
 def __init__ (self):
     self.cabeza=None
 def insertar(self,m,n,nombre,p,filas):
     nuevo=matriz(m,n,nombre,p,filas)
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
         print("M: "+tmp.m+"N: "+tmp.n+"Nombre: "+tmp.nombre+"P "+tmp.p+"Filas "+str(tmp.filas))
         print("--------------")
         tmp=tmp.siguiente
 def insertar2(self):
     tmp=self.cabeza
     while tmp is not None:
         lista.insertar(tmp.m,tmp.n,tmp.nombre,tmp.p,lista2)
         tmp=tmp.siguiente        
     



