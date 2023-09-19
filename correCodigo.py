import sympy as sp
from MetodosNuméricos import raicesEcuaciones as rE
import pandas as pd


x=sp.symbols('x')
f=x**2-5
tol=10**(-100)
iterMax=1000


pancho=rE(f,tol,iterMax)
[errBis,aproxBis]=pancho.halley(1.5)

#crear un DataFrame
data={"Aproximación":aproxBis, "Error":errBis}
df=pd.DataFrame(data)
pancho.grafErrorIter(errBis,"Halley")
pancho.grafAproxIter(aproxBis, "Halley")

#Mostrar el DataFrame
print(df)

