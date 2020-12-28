# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:13:55 2020
2d FDTD 加上PML
@author: lenovo
"""
import numpy as np
from matplotlib import pyplot as plt

lt=45 #时间长度
lx=60 
ly=40  #空间大小
lyy=20 #PML层

dx=0.1
dy=0.1  #空间步长
dt=0.1  #时间步长
wl=30
mu=1
ep=2
sigma=2
sigmam=sigma*mu/ep

g1=(ep/dt-sigma/2)/(ep/dt+sigma/2)
g2=1/(ep/dt+sigma/2)
gm1=(mu/dt-sigmam/2)/(mu/dt+sigmam/2)
gm2=1/(mu/dt+sigmam/2)

Hx1=np.zeros((lx,ly+lyy))
Hx2=np.zeros((lx,ly+lyy))
Hy1=np.zeros((lx,ly+lyy))
Hy2=np.zeros((lx,ly+lyy))
Ez1=np.zeros((lx,ly+lyy))
Ez2=np.zeros((lx,ly+lyy))
x=np.arange(0,lx*dx,dx)
y=np.arange(0,(ly+lyy)*dy,dy)
X, Y = np.meshgrid(y, x)
xx=int(lx/2)        #源点
yy=int(ly*3/4)
for i in range(0,lt-1):


    for j in range(0,lx-1):
        for k in range(0,ly+lyy-1):         #Hx与Hy的更新
            if k<=ly-1:
                Hx2[j,k]=Hx1[j,k]-dt/(dy*mu)*(Ez1[j,k]-Ez1[j,k-1])
                Hy2[j,k]=Hy1[j,k]+dt/(dx*mu)*(Ez1[j,k]-Ez1[j-1,k])
            else:           #pml层的更新
                Hx2[j,k]=gm1*Hx1[j,k]-gm2/(dy)*(Ez1[j,k]-Ez1[j,k-1])
                Hy2[j,k]=gm1*Hy1[j,k]+gm2/(dx)*(Ez1[j,k]-Ez1[j-1,k])

    for j in range(0,lx-1):
        for k in range(0,ly+lyy-1):    #Ez的更新
            if k<=ly-1:
                if (j!=xx)or(k!=yy):
                    Ez2[j,k]=Ez1[j,k]+dt/ep*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
            else:           #pml层的更新
                Ez2[j,k]=g1*Ez1[j,k]+g2*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
                
    Ez2[xx,yy]=np.sin(np.pi*2*i/wl)  #源点不参与更新               
    Ez1[:,:]=Ez2[:,:]
    Hx1[:,:]=Hx2[:,:]
    Hy1[:,:]=Hy2[:,:]
    

    if i==lt-2:
        
        fig = plt.figure()  #定义新的三维坐标轴
        ax = plt.axes(projection='3d')
        ax.plot_surface(X,Y,Ez2,cmap='rainbow')
        """
        plt.imshow(Ez2,cmap='gray')
        """