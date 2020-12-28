# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:27:38 2020

@author: lenovo
"""

import numpy as np
f=lambda x:np.cos(x)
def trapzoid(f,a,b,n):
    if a>b:
        a,b=b,a
    h=(b-a)/n
    s=h/2*(f(a)+f(b))
    for k in range(1,n-1):
        s+=h*f(a+k*h)
    return s
a=trapzoid(f,0,np.pi/2,10000)
print(a)

