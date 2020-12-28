# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:04:10 2020

一维FDTD考虑任意有动力的位置
@author: lenovo
"""

import numpy as np
from matplotlib import pyplot as plt
lt=400 #
lx=500 #距离=dx*lx
dx=0.1
dt=0.1
wl=20 #波长lambda
H1=np.zeros(lx-1)
H2=np.zeros(lx-1)
E1=np.zeros(lx)
E2=np.zeros(lx)
xx=int(250)
"""
E[:,xx]=np.array(list(map(lambda x: np.sin(np.pi*2*dx*x/wl),range(lt))))   #0点以cosx震动，map need this:np.array(list(map(...)))
"""


for i in range(0,lt-2):  #时间有lt-1个时刻

    if i<=int(0.5*wl/dx): #只有一个周期的运动
        E1[xx]=np.sin(np.pi*2*dx*i/wl)
    
    for j in range(0,lx-2):
        H2[j]=H1[j]+1.2*(dx/dt)*(E1[j+1]-E1[j])
    for j in range(1,lx-1):   #E有lx-1个位置
        if (j!=xx)or(i<=int(0.5*wl/dx)):
            E2[j]=E1[j]+0.8*(dx/dt)*(H2[j]-H2[j-1])


    if i==lt-3:  
        plt.plot(dx*np.arange(0,lx),E2[:])
        #plt.plot(dx*np.arange(0,lx-1),H2[:])
    E1[:]=E2[:]
    E2[:]=0
    H1[:]=H2[:]
    H2[:]=0
    
    
    H1[0]=0
    H1[lx-2]=0
    #E2[lx-1]=E1[lx-2]
    