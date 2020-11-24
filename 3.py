from math import cos
from math import factorial
epsilon = float(input("задана точність:"))
n = float(input("значення n"))
x = float(input("значення x:"))
cosinus = cos(x)
dodanok = 1
s = 0
i = 0
while dodanok > epsilon:
    dodanok1 = dodanok
    s += dodanok1
    dodanok = (-1) ** i * ((x ** (2*i)) / factorial( 2*i ))
    i += 1
if cosinus == s:
    print("вірна справедливість")
else:
    print("спріведливість не є вірною")