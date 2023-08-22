
def SumaDiag (a,b,c):
    resultado=0
    for i in range(a,b+1):
        resultado = resultado + c*i
    return resultado

def SumaDiag2 (a,b):
    mitad=a/2
    cantDiv=1
    while abs(a-mitad)>=(10**b):
        #print(a," y ",mitad)
        a=mitad
        mitad=mitad/2
        cantDiv+=1
        
    #print(a," y ",mitad)   
    return cantDiv