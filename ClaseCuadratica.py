import math
import matplotlib.pyplot as plt
import numpy as np

class ClaseCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.vertX=-b/(2*a)
    
    def raicesX(self):
        if self.discriminante() > 0:
            x1 = (-self.b + math.sqrt(self.discriminante())) / (2*self.a)
            x2 = (-self.b - math.sqrt(self.discriminante())) / (2*self.a)
            return f"La función tiene 2 soluciones x={x1} y x={x2}."  # Dos soluciones distintas
        elif self.discriminante() == 0:
            x1 = -self.b / (2*self.a)
            return f"La función tiene 1 solución x={x1}."  # Dos soluciones iguales
        else:
            return f"La función no tiene soluciones"  # No hay soluciones reales
        
    def discriminante(self):
        discriminante=self.b**2-4*self.a*self.c
        return discriminante
    
    def grafica(self):
        fig, ax = plt.subplots()
        x = np.linspace(self.vertX-10, self.vertX+10, 1000)  # Generamos 1000 puntos entre -10 y 10
        y = self.a * x**2 + self.b * x + self.c
        ax.plot(x, y, label=f"{self.a}x^2 + {self.b}x + {self.c}")
        ax.set_title(f'Gráfico de la función cuadrática')
        ax.grid(True)
        return fig     
    