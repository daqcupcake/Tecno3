import sympy as sp
from MetodosNuméricos import raicesEcuaciones as rE
import pandas as pd

x=sp.symbols('x')
f=80*sp.exp(-2*x)+20*sp.exp(-0.5*x)-7
tol=10**(-10)
iterMax=1000

a=1.5
b=2.5

solucion=rE(f,tol,iterMax)
[eBis,aBis]=solucion.biseccion(a, b)
[eFPos,aFPos]=solucion.falsaPosicion(a, b)
[eSec,aSec]=solucion.secante(a, b)

#crear un DataFrame
dataBis={"Aproximación Biseccion":aBis, "Error Biseccion":eBis}
dfBis=pd.DataFrame(dataBis)

dataFPos={"Aproximación Falsa Posición":aFPos, "Error Falsa Posción":eFPos}
dfFPos=pd.DataFrame(dataFPos)

dataSec={"Aproximación Secante":aSec, "Error Secante":eSec}
dfSec=pd.DataFrame(dataSec)

#Mostrar el DataFrame
print("\nDataframe Bisección\n")
print(dfBis)

print("\nDataframe Falsa Posición\n")
print(dfFPos)

print("\nDataframe Secante\n")
print(dfSec)
