
import sympy as sp
import matplotlib.pyplot as plt

class raicesEcuaciones:
    
    def __init__ (self,f,tol,iterMax): #f es la función, tol es la tolerancia y iterMax las iteraciones maximas del programa
        
        self.f=f
        self.tol=tol
        self.iterMax=iterMax
        
    def biseccion (self,x0,x1):
          
        error=[]
        aprox=[]
        cont=0      #contador que lleva las iteraciones
        x=sp.symbols('x') #indica que x es una variable simbólica
        fx0 = self.f.subs(x,x0).evalf() #evalua la funcion en x0
        fx1 = self.f.subs(x,x1).evalf() #evalua la funcion en x1 sustituyendo la variable
        
        
        if fx0*fx1<0:
            while cont<self.iterMax:
                xi=(x0+x1)/2
                aprox.append(xi)
                fxi=self.f.subs(x,xi).evalf()
                if fx0*fxi<0:
                    x1=xi
                    fx1=fxi
                elif fx1*fxi<0:
                    x0=xi
                    fx0=fxi
                else:
                    break
                
                if cont>=1:
                    error.append(abs(aprox[cont]-aprox[cont-1]))
                else:
                    error.append(1)
                if error[cont]<self.tol:
                    break
                cont+=1
        else:
            print("No se puede aplicar el método")
        return error, aprox
    
    def grafErrorIter (self,vectError): #grafica en el eje x el numero de iter y en el y el error
        
        plt.plot(range(len(vectError)),vectError, marker='o')
        plt.xlabel("Iteración")
        plt.ylabel("Error")
        
        plt.title(f"Iteración vs. Error con el método bisección de la función {self.f}")
        plt.grid(True)
        plt.show()
   
    def grafAproxIter (self,vectAprox): #grafica en el eje x el numero de iter y en el y la aproximacion
        
        plt.plot(range(len(vectAprox)),vectAprox, marker='o')
        plt.xlabel("Iteración")
        plt.ylabel("Aproximación")
        
        plt.title(f"Iteración vs. Aproximación con el método bisección de la función {self.f}")
        plt.grid(True)
        plt.show()
   
    def falsaPosicion(self,x0,x1):
        
        error=[]
        aprox=[]
        cont=0      #contador que lleva las iteraciones
        x=sp.symbols('x') #indica que x es una variable simbólica
        fx0 = self.f.subs(x,x0).evalf() #evalua la funcion en x0
        fx1 = self.f.subs(x,x1).evalf() #evalua la funcion en x1 sustituyendo la variable
        
        if (fx0*fx1<0):
            while cont<self.iterMax: 
                
                x2=x1-(fx1*(x1-x0))/(fx1-fx0)
                fx2=self.f.subs(x,x2).evalf()
                aprox.append(x2)
                
                if fx2==0:
                    
                    error.append(0)
                    print("por aqui salio")
                    break
                    
                elif fx2*fx0<0:
                    x1=x2
                    fx1=fx2
                    
                elif fx1*fx2<0:
                    x0=x2
                    fx0=fx2
                    
                else:
                    break
                
                if cont>=1:
                    error.append(abs(aprox[cont]-aprox[cont-1]))
                else:
                    error.append(1)
                if error[cont]<self.tol:
                    break
                cont+=1
                
            
            
        else:
            print("No se puede aplicar el método")
    
        return error, aprox
    
    def secante(self,x0,x1):
        
        x=sp.symbols('x') #indica que x es una variable simbólica
        fx0 = self.f.subs(x,x0).evalf() #evalua la funcion en x0
        fx1 = self.f.subs(x,x1).evalf() #evalua la funcion en x1 sustituyendo la variable
         
        cont=0
        error=[]
        aprox=[]
        
        while(cont<self.iterMax):
            
            xi=x1-(fx1*(x1-x0))/(fx1-fx0)
            fxi = self.f.subs(x,xi).evalf() #evalua la funcion en xi sustituyendo la variable
            aprox.append(xi)
            
            x0=x1
            fx0=fx1
            x1=xi
            fx1=fxi
            
            if cont>=1:
                error.append(abs(aprox[cont]-aprox[cont-1]))
            else:
                error.append(1)
                
            if error[cont]<self.tol:
                break
                
            cont+=1
            
        return error,aprox
            
            
        

