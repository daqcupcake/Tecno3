# definicion de funcion
'''Otro comentario'''
def SolCuad(a,b,c): # a,b,c coeficientes de la ecuacion cuadratica

    #calculo discriminante
    discriminante = b**2-4*a*c
    
    #análisis discriminante    
    if discriminante>0:
        return 2
    elif discriminante==0:
        return 1
    else:
        return 0
    
    
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