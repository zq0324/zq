#coding=utf-8
from sympy import *

x=Symbol("x")
y=Symbol("y")

res = solve([4*x*x+2*y-4000, x+3*y-2304],[x, y])
print(res)
