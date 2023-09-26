import sympy as sp
from tkinter import *
from tkinter.ttk import Combobox
from ClaseCuadratica import ClaseCuadratica as Cc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox

fig, ax = plt.subplots()
# Definición de las funciones

def alClickBoton():
    
    #Escribir acá el código del funcionamiento del botón
    a=float(valA.get())
    
    if(a!=0):
        b=float(valB.get())
        c=float(valC.get())
        
        ecua=Cc(a,b,c)
        
        
        inter.config(text=ecua.raicesX())
        
        valDisc.config(text=f"El valor del discriminante es de: {ecua.discriminante()}")
        
        grafica=FigureCanvasTkAgg(ecua.grafica(),root)
        grafica.get_tk_widget().place(x=50,y=200)
    else:
        print("alguien inentó poner 0 en a")
    
    
# Escribir acá la inicialización de la ventana principal
root=Tk()
root.title("Ecuación Cuadrática")
root.geometry("950x520")

# Escribir acá la creación y colocación de los componentes
inst=Label(root,text="Ingrese en las siguientes casillas los coeficientes de la ecuación cuadrática.")
inst.place(x=50,y=50)

lblA=Label(root,text="valor de a:")
lblA.place(x=50,y=100)
valA=Entry(root,width=10)
valA.place(x=150,y=100)

lblB=Label(root,text="valor de b:")
lblB.place(x=250,y=100)
valB=Entry(root,width=10)
valB.place(x=350,y=100)

lblC=Label(root,text="valor de c:")
lblC.place(x=450,y=100)
valC=Entry(root,width=10)
valC.place(x=560,y=100)

activar=Button(root,text="Calcular",command=alClickBoton)
activar.place(x=250,y=150)

inter=Label(root,text="")
inter.place(x=500,y=200)
 
 
valDisc=Label(root,text="")
valDisc.place(x=500,y=300)
 



# Iniciar el bucle principal
root.mainloop()
