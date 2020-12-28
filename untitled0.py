# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:58:29 2020

一阶欧拉法


@author: lenovo
"""

import numpy as np
from matplotlib import pyplot as plt

tau=1
dt=0.0284*tau
t=10*tau
lt=int(t/dt)
y=np.zeros(lt)
yy=np.zeros(lt)
y[0]=1
error=0
for i in range(0,lt-1):
    y[i+1]=(1-dt/tau)*y[i]
    yy[i]=y[0]*np.exp(-i*dt/tau)
    error+=(y[i]-yy[i])**2
error=error/np.dot(yy,yy)
error=error**0.5
plt.plot(dt*np.arange(0,lt),y[:])
plt.plot(dt*np.arange(0,lt),yy[:])