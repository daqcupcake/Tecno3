# -*- coding: utf-8 -*-
"""
Página Principal Proyecto 1

Encargado: Daniela Arias 

Miembros:   Daniela Arias
            Sebastián Ortiz
            Andy Torres
            
Contenido: El programa contiene la primera pantalla que funciona como menú para todo el proyecto           
            
"""

#IMPORTS
import tkinter as tk

#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#000000"
colorBotones="#25C7CA"

#FUNCIONES

def Desigualdad():
    print("Boton desigualdad presionado")
    
def Pitagoras():
    print("Boton Pitagoras presionado")
    
def LeySen():
    print("Boton Ley de Senos presionado")
    
def LeyCos():
    print("Boton Ley de Cosenos presionado")
    
def AcercaDe():
    print("Boton Acerca de presionado")

#TKINTER

#   PRINCIPAL
root=tk.Tk()
root.title("Página Principal Triángulos")
root.geometry("800x600")


#   BOTONES Y LABELS
titulo=tk.Label(root,text="Aqui va el título")
titulo.place(x=350,y=50)
desc=tk.Label(root,text="Aqui va la descripción del programa")
desc.place(x=300,y=100)


btnDes=tk.Button(root,text="Desigualdad triangular",bg=colorBotones,command=Desigualdad)
btnDes.place(x=200,y=150)
btnPit=tk.Button(root,text="Pitágoras",bg=colorBotones,command=Pitagoras)
btnPit.place(x=400,y=150)
btnLSen=tk.Button(root,text="Ley de Senos",bg=colorBotones,command=LeySen)
btnLSen.place(x=200,y=200)
btnLCos=tk.Button(root,text="ley de Cosenos",bg=colorBotones,command=LeyCos)
btnLCos.place(x=400,y=200)
btnAcd=tk.Button(root,text="Acerca de",bg=colorBotones,command=AcercaDe)
btnAcd.place(x=700,y=550)



#PRINCIPAL
root.mainloop()


