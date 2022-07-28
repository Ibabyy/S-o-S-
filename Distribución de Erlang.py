from sympy import*
from sympy.abc import*
from sympy.stats import*
init_printing(use_latex="mathjax")
from numpy import*
from scipy.integrate import*


def integrand(t, LL, k):
    return ((LL**k*t**(k-1)*exp(-LL*t))/(math.factorial(k-1)))


LL = 1.56952
j = 0
i = 0
Antes = 0

print("***DISTRIBUCIÓN DE ERLANG***\nLambda: ", LL)
P_CRIT = float(input("Indique la probabilidad con la que desea la predicción (0-100):\n"))/100
rango = int(input("Indique el número máximo de éxitos\n")) + 1



for k in range(1 , rango):
    II = 0
    i = 0# COMENTAR ESTA LÍNEA PARA MÁS VELOCIDAD. NO FUNCIONA PARA RANGOS GRANDES
    while II < P_CRIT:
        i += 1
        I = quad(integrand, 0, i/100, args=(LL,k))
        II = I[0]
        float(II)
    print("P =%2.8f" % (II), " t=", i/100, " k=", k)

input()
