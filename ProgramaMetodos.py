# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:46:22 2023

@author: belenballestero07
"""
import sympy as sp
from tkinter import * 
from tkinter.ttk import Combobox
from MetodosNuméricos import raicesEcuaciones as rE
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


root=Tk()
root.title("Métodos Numéricos") #Cambiar nombre de la ventana
root.geometry("600x800")

frame1=Frame(root)
frame2=Frame(root)
"""
Variables globables
"""
metodos=["Bisección", "Secante", "Falsa posición", "Halley"]
listMetodos=Combobox(frame1,values=metodos,width=20) #En values debe venir el nombre de la lista que se creo

def visX1(event):
    metSelec=listMetodos.get()
    if metSelec in ["Bisección","Secante","Falsa posición"]:
        label05.pack()
        txtX1.pack()
    else:
        label05.pack_forget() #.place_forget
        txtX1.pack_forget() #.grid_remove
        
def clickCalc():
    global cvGraficoAprox, cvGraficoError
    x=sp.symbols("x")
    f=sp.sympify(txtFuncion.get())
    tol=float(txtTol.get())
    iterMax=int(txtIterMax.get())
    x0=float(txtX0.get())
    metSelec=listMetodos.get()
    
    funcionUsuario=rE(f,tol,iterMax)
    if metSelec=="Bisección":
        x1=float(txtX1.get())
        [eBis,aBis]=funcionUsuario.biseccion(x0, x1)
        grafError=funcionUsuario.grafErrorIter(eBis, "Biseccion")
        grafAprox=funcionUsuario.grafAproxIter(aBis, "Biseccion")
        
        cvGraficoError=FigureCanvasTkAgg(grafError,figure,master=cvGraficoError)
        cvGraficoError.get_tk_widget().pack()
"""
BOTONES
"""

txtFuncion=Entry(frame1, width=17, font=("Arial",15))
txtTol=Entry(frame1, width=17, font=("Arial",15))
txtIterMax=Entry(frame1, width=17, font=("Arial",15))
txtX0=Entry(frame1, width=17, font=("Arial",15))
txtX1=Entry(frame1, width=17, font=("Arial",15))
btnCalcular=Button(frame1, text="Calcular",command=clickCalc)
cvGraficoError=Canvas(frame2, bg="white", width=400, height=300)
cvGraficoAprox=Canvas(frame2, bg="white", width=400, height=300)
label01=Label(frame1, text="Función")
label02=Label(frame1, text="Tolerancia")
label03=Label(frame1, text="Iteracciones Máximas")
label04=Label(frame1, text="x0")
label05=Label(frame1, text="x1")


frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)


listMetodos.bind("<<ComboboxSelected>>",visX1)

label01.pack()
txtFuncion.pack()
label02.pack()
txtTol.pack()
label03.pack()
txtIterMax.pack()
label04.pack()
txtX0.pack()
listMetodos.pack()
btnCalcular.pack()

cvGraficoError.pack()
cvGraficoAprox.pack()

root.mainloop()