"""
P�gina Desigualdad Triangular Proyecto 1

Encargado: Daniela Arias 

Miembros:   Daniela Arias
            Sebasti�n Ortiz
            Andy Torres
            
Contenido: 
            
"""
#IMPORTS
import tkinter as tk

#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#000000"
colorBotones="#25C7CA"
fuente=("Arial",15)

#FUNCIONES
def Calcular():
    print("Boton Ley de Cosenos presionado")
    
def AcercaDe():
    print("Boton Acerca de presionado")


#TKINTER

#   PRINCIPAL
root=tk.Tk()
root.title("Desigualdad Tri�ngular")
root.geometry("800x600")

#   BOTONES Y LABELS
titulo=tk.Label(root,text="Aqui va el t�tulo")
titulo.place(x=350,y=50)
desc=tk.Label(root,text="Aqui va la descripci�n del programa")
desc.place(x=300,y=100)




btnAcd=tk.Button(root,text="Acerca de",bg=colorBotones,command=AcercaDe)
btnAcd.place(x=700,y=550)


root.mainloop()