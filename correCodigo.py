import sympy as sp
from MetodosNuméricos import raicesEcuaciones as rE
import pandas as pd


x=sp.symbols('x')
f=x**2-sp.cos(x)-1
tol=0.000001
iterMax=50

pancho=rE(f,tol,iterMax)
[errBis,aproxBis]=pancho.secante(1, 2)

#crear un DataFrame
data={"Aproximación":aproxBis, "Error":errBis}
df=pd.DataFrame(data)
pancho.grafErrorIter(errBis)
pancho.grafAproxIter(aproxBis)

#Mostrar el DataFrame
print(df)

