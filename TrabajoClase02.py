import sympy as sp
from MetodosNuméricos import raicesEcuaciones as rE
import pandas as pd

x=sp.symbols('x')
f=9*sp.exp(-0.7*x)*sp.cos(4*x)-3.5
tol=10**(-100)
iterMax=1000

a=0
b=1.4

solucion=rE(f,tol,iterMax)
[eBis,aBis]=solucion.biseccion(a, b)
[eFPos,aFPos]=solucion.falsaPosicion(a, b)
[eSec,aSec]=solucion.secante(a, b)
[eHall,aHall]=solucion.halley(a)

#crear un DataFrame
dataBis={"Aproximación Biseccion":aBis, "Error Biseccion":eBis}
dfBis=pd.DataFrame(dataBis)

dataFPos={"Aproximación Falsa Posición":aFPos, "Error Falsa Posción":eFPos}
dfFPos=pd.DataFrame(dataFPos)

dataSec={"Aproximación Secante":aSec, "Error Secante":eSec}
dfSec=pd.DataFrame(dataSec)

dataHall={"Aproximación Halley":aHall, "Error Halley":eHall}
dfHall=pd.DataFrame(dataHall)


#Mostrar el DataFrame
print("\nDataframe Bisección\n")
print(dfBis)

solucion.grafErrorIter(eBis,"Bisección")
solucion.grafAproxIter(aBis, "Bisección")

print("\nDataframe Falsa Posición\n")
print(dfFPos)

solucion.grafErrorIter(eFPos,"Falsa Posición")
solucion.grafAproxIter(aFPos, "Falsa Posición")

print("\nDataframe Secante\n")
print(dfSec)

solucion.grafErrorIter(eSec,"Secante")
solucion.grafAproxIter(aSec, "Secante")

print("\nDataframe Halley\n")
print(dfHall)

solucion.grafErrorIter(eHall,"Halley")
solucion.grafAproxIter(aHall, "Halley")


