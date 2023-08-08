# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np

class ClaseCuadratica:
    def __init__(self, a,b,c):  #siempre recibe a self
        self.a=self.validarCuad(a)
        self.b=b
        self.c=c
        self.vertX = -b/(2*a)
        
    def validarCuad(self,a): #funcion para que a no sea 0 OPCION 1
        if a==0:
            raise ValueError("Si el valor de a es 0, no sería una función cuadrática")
        return a
    
    
    def discriminante(self):
        return self.b**2-4*self.a*self.c
    
    def SolCuad(self): 

        #calculo discriminante
        discriminante = self.discriminante()
        
        #análisis discriminante    
        if discriminante>0:
            
            sol1= (-self.b+ math.sqrt(discriminante))/(2*self.a)
            sol2= (-self.b-math.sqrt(discriminante))/(2*self.a)
            return (2,[sol1,sol2])
           
        
        elif discriminante==0:
            sol1= -self.b/(2*self.a)
            return (1,[sol1])
        else:
            return (0,[])
        
    def MonotoCuad(self): 
        
        if self.a!=0:
            
            #analisis concavidad
            if self.a>0:
                print("la función es decreciente en ]-∞,", self.vertX ,"[\n")
                print("la función es creciente en ]", self.vertX ,",+∞ [")
            else:
                print("la función es creciente en ]-∞,", self.vertX ,"[\n")
                print("la función es decreciente en ]", self.vertX ,",+∞ [")
        else:
         return ("No es una función cuadrática")
    
    def Prueba (self):
        return f"texto mixto  {self.a}"
    
    def Grafica (self):
        x= np.linspace((self.vertX-10),(self.vertX+10),1000) #espacio de -10 a 10, luego n puntos retorna una lista de los n puntos equidistantes   
        y= self.a*x**2+self.b*x+self.c
        
        plt.plot(x,y,label=f"{self.a}x^2+{self.b}x+{self.c}")
        plt.axvline(self.vertX, color="red", lw=0.5)
        plt.axhline(0, color="black", lw=0.5)
        plt.axvline(0, color="black", lw=0.5)
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico de la función cuadrática")
        plt.grid(True)
        
        plt.show()
        
        
        

