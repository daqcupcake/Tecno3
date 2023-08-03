# definicion de funcion
'''Otro comentario'''

import math
import matplotlib.pyplot as plt
import numpy as np

def SolCuad(a,b,c): # a,b,c coeficientes de la ecuacion cuadratica

    #calculo discriminante
    discriminante = b**2-4*a*c
    
    #análisis discriminante    
    if discriminante>0:
        
        sol1= (-b+ math.sqrt(discriminante))/(2*a)
        sol2= (-b-math.sqrt(discriminante))/(2*a)
        return (2,[sol1,sol2])
       
    
    elif discriminante==0:
        sol1= -b/(2*a)
        return (1,[sol1])
    else:
        return (0,[])
    
def Grafica (a,b,c):
    x= np.linspace(-10,10,1000) #espacio de -10 a 10, luego n puntos retorna una lista de los n puntos equidistantes   
    y= a*x**2+b*x+c
    
    plt.plot(x,y,label=f"{a}x^2+{b}x+{c}")
    
    plt.axhline(0, color="black", lw=0.5)
    plt.axvline(0, color="black", lw=0.5)
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de la función cuadrática")
    plt.grid(True)
    
    plt.show()
def MonotoCuad(a,b,c): #a,b,c coeficientes de la ecuacion cuadratica

    
    if a!=0:
        #calculo vertice
        vertice = -b/(2*a)
        
        #analisis concavidad
        if a>0:
            print("la función es decreciente en ]-∞,", vertice ,"[\n")
            print("la función es creciente en ]", vertice ,",+∞[")
        else:
            print("la función es creciente en ]-∞,", vertice ,"[\n")
            print("la función es decreciente en ]", vertice ,",+∞[")
    else:
        print("No es una función cuadrática")