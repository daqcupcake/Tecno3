"""
Página Desigualdad Triangular Proyecto 1

Encargado: Daniela Arias 

Miembros:   Daniela Arias
            Sebastián Ortiz
            Andy Torres
            
Contenido: 
            
"""
#IMPORTS
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#000000"
colorBotones="#25C7CA"
fuente=("Arial",15)

#FUNCIONES
def graficoTri(a,b,c):
    m=(b**2-c**2-a**2)/(-2*a)
    h=np.sqrt(c**2-m**2)
    #triangulo=[(0,0),(a,0),(m,h),(0,0)]
    print(m,h)
    fig, ax = plt.subplots()
    
    trigX = [0, a, m,  0]
    trigY = [0, 0, h,  0]
   

def graficoNoTri(a,b,ca):
    #(0,b)(0,0),(a,0)(a,c)
    fig, ax = plt.subplots()
    x=[0,0,a,a]
    y=[b,0,0,c]
    plt.plot(x, y, 'o')
    plt.plot(x, y, '-')
    plt.show()
    return fig
    

def Revisar():
    
    if num1.get() and num2.get() and num3.get(): #verifica que haya algo en los input
        
        n1=float(num1.get())
        n2=float(num2.get())
        n3=float(num3.get())
        
        lados=[n1,n2,n3]
        lados.sort(reverse=True)
        
        if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
            lrespuesta.config(text="Las medidas dadas corresponden a un triángulo")
           
            
        else: 
            lrespuesta.config(text="Las medidas dadas no corresponden a un triángulo")
            
            #Ordenamos los lados es orden de tamaño
            
            grafico=graficoTri(5, 4, 3)
            grafica=FigureCanvasTkAgg(grafico,root)
            grafica.get_tk_widget().place(x=50,y=300)
            
            
            
        
   
    
def AcercaDe():
    print("Boton Acerca de presionado")


#TKINTER

#   PRINCIPAL
root=tk.Tk()
root.title("Desigualdad Triángular")
root.geometry("800x600")

#   BOTONES Y LABELS
titulo=tk.Label(root,text="Aqui va el título")
titulo.place(x=350,y=50)
desc=tk.Label(root,text="Aqui va la descripción del programa")
desc.place(x=300,y=100)
lnum1=tk.Label(root,text="Número 1:")
lnum1.place(x=50, y=150)
num1=tk.Entry(root,width=10)
num1.place(x=150, y=150)
lnum2=tk.Label(root,text="Número 2:")
lnum2.place(x=200, y=150)
num2=tk.Entry(root,width=10)
num2.place(x=300, y=150)
lnum3=tk.Label(root,text="Número 3:")
lnum3.place(x=350, y=150)
num3=tk.Entry(root,width=10)
num3.place(x=450, y=150)

btnRev=tk.Button(root,text="Revisar",command=Revisar)
btnRev.place(x=550,y=150)
lrespuesta=tk.Label(root,text="")
lrespuesta.place(x=50,y=200)





btnAcd=tk.Button(root,text="Acerca de",bg=colorBotones,command=AcercaDe)
btnAcd.place(x=700,y=550)


root.mainloop()