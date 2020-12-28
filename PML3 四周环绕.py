# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:43:54 2020
PML在四周都有吸收的情况

@author: lenovo
"""
import numpy as np
from matplotlib import pyplot as plt

lt=250 #时间长度
lx=140 
ly=140  #空间大小
lyy=24 #PML层
lxx=24
lx+=lxx
ly+=lyy

dx=0.1
dy=0.1  #空间步长
dt=0.1  #时间步长
wl=40
mu=1
ep=2
sigma=4
sigmam=sigma*mu/ep

g1=(ep/dt-sigma/2)/(ep/dt+sigma/2)
g2=1/(ep/dt+sigma/2)
gm1=(mu/dt-sigmam/2)/(mu/dt+sigmam/2)
gm2=1/(mu/dt+sigmam/2)

Hx1=np.zeros((lx,ly))
Hx2=np.zeros((lx,ly))
Hy1=np.zeros((lx,ly))
Hy2=np.zeros((lx,ly))
Ez1=np.zeros((lx,ly))
Ez2=np.zeros((lx,ly))
x=np.arange(0,lx*dx,dx)
y=np.arange(0,(ly)*dy,dy)
X, Y = np.meshgrid(y, x)
xx=int(lx/4)        #源点
yy=int(ly/4)
for i in range(0,lt-1):


    for j in range(0,lx-1):
        for k in range(0,ly-1):         #Hx与Hy的更新
            if (lyy/2<k<ly-lyy/2)and(lxx/2<j<lx-lxx/2):
                Hx2[j,k]=Hx1[j,k]-dt/(dy*mue)*(Ez1[j,k]-Ez1[j,k-1])
                Hy2[j,k]=Hy1[j,k]+dt/(dx*mu)*(Ez1[j,k]-Ez1[j-1,k])
            else:           #pml层的更新
                Hx2[j,k]=gm1*Hx1[j,k]-gm2/(dy)*(Ez1[j,k]-Ez1[j,k-1])
                Hy2[j,k]=gm1*Hy1[j,k]+gm2/(dx)*(Ez1[j,k]-Ez1[j-1,k])

    for j in range(0,lx-1):
        for k in range(0,ly-1):    #Ez的更新
            if (lyy/2<k<ly-lyy/2)and(lxx/2<j<lx-lxx/2):
                if (j!=xx)or(k!=yy):
                    Ez2[j,k]=Ez1[j,k]+dt/ep*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
            else:           #pml层的更新
                Ez2[j,k]=g1*Ez1[j,k]+g2*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
                
    Ez2[xx,yy]=np.sin(np.pi*2*i/wl)  #源点不参与更新               
    Ez1[:,:]=Ez2[:,:]
    Hx1[:,:]=Hx2[:,:]
    Hy1[:,:]=Hy2[:,:]
    

    if i==lt-2:
        """
        fig = plt.figure()  #定义新的三维坐标轴
        ax = plt.axes(projection='3d')
        ax.plot_surface(X,Y,Ez2,cmap='rainbow')
        """
        plt.imshow(np.log(Ez2**2).T,cmap='gray_r',vmin=-15, vmax=0)
        plt.colorbar()
        
