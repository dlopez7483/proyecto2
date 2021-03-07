from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import*
from tkinter import filedialog
from ListaEnlazada import listaenlazada
from ListaFilas import listafilas
from ListaFilas2 import listafilas2
from ListaEnlazada2 import listaenlazada2 
Boleano = True
numero2=0
listamatriz = listaenlazada()
ListaFilas=listafilas()
listamatriz2=listaenlazada2()
Listafilas2=listafilas2()
while Boleano:
 print("Menú\n\
     1.Cargar Archivo\n\
     2.Procesar Archivo\n\
     3.Escribir Archivo Salida\n\
     4.Mostrar datos del estudiante\n\
     5.Generar Grafica\n\
     6.Salida          ")
 numero = input()
 numero2 = int(numero)

 if numero2==1:
     archivo = filedialog.askopenfilename()
     tree = ET.parse(archivo)
     root = tree.getroot()
     #print(len(root))
     number=0
     for elem in root:
         number+=1
         number2=0
         for sub in elem:
             number2+=1
             if number2<=(len(elem)):
                 number3=0
                 if int(sub.text)!=0:
                     number3=1
                 ListaFilas.insertar(sub.attrib['y'],sub.attrib['x'],str(number),sub.text)    
         listamatriz.insertar(elem.attrib['m'],elem.attrib['n'],elem.attrib['nombre'],str(number),ListaFilas)  
     listamatriz.Mostrar()   
     ListaFilas.Mostrar()
     
 elif numero2==2:
     print("Ya vamos Jovén")
     ListaFilas.insertar2()
     listamatriz.insertar2()
     listamatriz2.Mostrar2()
 
 elif numero2==6:
     Boleano=False
     print("ADIOS")
     break

 
