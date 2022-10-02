from sympy import*
from sympy.abc import*
from sympy.stats import*
init_printing(use_latex="mathjax")
from numpy import*
from scipy.integrate import*

def integrand(t, LL, k):
    return ((LL**k*t**(k-1)*exp(-LL*t))/(math.factorial(k-1)))

LL_min = 1.07238
LL_max = 2.06666
LL = 1.56952
j = 0
i = 0
Antes = 0

print("***DISTRIBUCIÓN DE ERLANG***\nLambda: ", LL)
P_CRIT = float(input("Indique la probabilidad con la que desea la predicción (0-100):\n"))/100
rango = int(input("Indique el número máximo de éxitos\n")) + 1

for k in range(1 , rango):
    II = 0
    II_min = 0
    II_max = 0
    i = 0
    i_min = 0
    i_max = 0
    while II < P_CRIT:
        i += 1
        I = quad(integrand, 0, i/100, args=(LL,k))
        II = I[0]
        float(II)
    while II_min < P_CRIT:
        i_min += 1
        I_min = quad(integrand, 0, i_min/100, args=(LL_min,k))
        II_min = I_min[0]
        float(II_min)
    while II_max < P_CRIT:
        i_max += 1
        I_max = quad(integrand, 0, i_max/100, args=(LL_max,k))
        II_max = I_max[0]
        float(II_max)
    print("P =%2.3f" % (II), " t=",i_max/100,"/", i/100,"/" ,i_min/100," k=", k)
