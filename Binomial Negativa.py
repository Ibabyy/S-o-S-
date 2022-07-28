from sympy import*
from sympy.abc import*
from sympy.stats import*
from numpy import*
from scipy.integrate import*
from math import*



print("***DISTRIBUCIÓN BINOMIAL NEGATIVA***\nProbabilidad del suceso: ", p)
P_CRIT = float(input("Indique la probabilidad con la que desea la predicción (0-100):\n"))/100
rango = int(input("Indique el número máximo de éxitos\n")) + 1


for r in range (1,rango):
    p = 0.23613
    i = 0
    S = sum([comb((x-1),(r-1))*p**r*(1-p)**(x-r) for x in range(r,r+i)])
    while S < P_CRIT:
        i += 1
        S = sum([comb((x-1),(r-1))*p**r*(1-p)**(x-r) for x in range(r,r+i)])

    print("P=%2.8f" % (S), " Intentos mínimos:", r+i, "Éxitos:", r)
input()
