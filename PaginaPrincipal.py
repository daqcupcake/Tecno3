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
fuente=("Arial",15)

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

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()  #define que esta es la ventana principal
        
        self.title("Página Principal Triángulos")
        self.geometry("800x600")


        #   BOTONES Y LABELS
        self.titulo=tk.Label(self,text="Aqui va el título",font=fuente)
        self.titulo.place(x=350,y=50)
        self.desc=tk.Label(self,text="Aqui va la descripción del programa",font=fuente)
        self.desc.place(x=300,y=100)
        
        
        self.btnDes=tk.Button(self,text="Desigualdad triangular",bg=colorBotones,command=Desigualdad,font=fuente)
        self.btnDes.place(x=200,y=150)
        self.btnPit=tk.Button(self,text="Pitágoras",bg=colorBotones,command=Pitagoras,font=fuente)
        self.btnPit.place(x=400,y=150)
        self.btnLSen=tk.Button(self,text="Ley de Senos",bg=colorBotones,command=LeySen,font=fuente)
        self.btnLSen.place(x=200,y=200)
        self.btnLCos=tk.Button(self,text="ley de Cosenos",bg=colorBotones,command=LeyCos,font=fuente)
        self.btnLCos.place(x=400,y=200)
        self.btnAcd=tk.Button(self,text="Acerca de",bg=colorBotones,command=AcercaDe,font=fuente)
        self.btnAcd.place(x=700,y=550)



#PRINCIPAL
if __name__=="__main__":
    app=Principal()
    app.mainloop()


