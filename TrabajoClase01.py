import math
import matplotlib.pyplot as plt
import numpy as np

class Triangulo:
    #NOTA aqui le agregue las variables del self
    
    def __init__(self,ladoA,ladoB,ladoC):
        self.a=ladoA
        self.b=ladoB
        self.c=ladoC
        
    def ValTriangulo(self):
        if (self.a+self.b)>self.c :
            if (self.b+self.c)>self.a :
                if (self.c+self.a)>self.b :
                    return 1
                else:
                    return 0
            else: 
                return 0
        else:
            return 0
        
    def Perimetro(self):
        if self.ValTriangulo()==1:
            return self.a+self.b+self.c
        else:
            return 0
    
    def Area (self):
        if self.ValTriangulo()==1:
            s=self.Perimetro()/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            #NOTA aqui me falto el math. para que funcione sqrt
        else:
            return 0
        
    def MedidasAngInt (self):
        
        if self.ValTriangulo()==1:
            #NOTA: Aquí cometí un error en el papel y puse solo las letras sin el self
            a1=math.acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c))
            a2=math.acos((self.a**2+self.b**2-self.c**2)/(2*self.a*self.b))
            a3=math.acos((self.c**2+self.a**2-self.b**2)/(2*self.c*self.a))
            
            return [math.degrees(a1),math.degrees(a2),math.degrees(a3)]
        else: 
            return [0,0,0]
        
    

    def plot_triangle(self):
        # Verificar si las medidas pueden formar un triángulo
        if self.ValTriangulo()==1:
            # Crear las coordenadas de los vértices del triángulo
            vertices = np.array([[0, 0], [self.a, 0], [0.5 * self.a, (self.c**2 - (0.5 * self.a)**2)**0.5]])
    
            # Crear el triángulo
            triangle = plt.Polygon(vertices, fill=None, edgecolor='black')
    
            # Crear la figura y el eje
            fig, ax = plt.subplots()
    
            # Agregar el triángulo al eje
            ax.add_patch(triangle)
    
            # Establecer límites del eje
            ax.set_xlim(0, max(self.a, self.b, self.c) + 1)
            ax.set_ylim(0, max(self.a, self.b, self.c) + 1)
    
            # Etiquetar los vértices del triángulo
            ax.text(vertices[0, 0], vertices[0, 1], 'A')
            ax.text(vertices[1, 0], vertices[1, 1], 'B')
            ax.text(vertices[2, 0], vertices[2, 1], 'C')
    
            # Etiquetar los lados del triángulo
            ax.text(0.5 * vertices[0, 0], 0.5 * vertices[0, 1], str(self.a))
            ax.text(0.5 * vertices[1, 0], 0.5 * vertices[1, 1], str(self.b))
            ax.text(0.5 * vertices[2, 0], 0.5 * vertices[2, 1], str(self.c))
    
            # Mostrar la gráfica
            plt.show()
        else:
            print("Las medidas proporcionadas no forman un triángulo válido.")
    
    #

        
        

