# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:43:54 2020
PML在四周都有吸收的情况

@author: lenovo
"""
import numpy as np
from matplotlib import pyplot as plt

lt=100 #时间长度
lx=100 
ly=100  #空间大小
lyy=36 #PML层
lxx=36
lx+=lxx
ly+=lyy

dx=0.1
dy=0.1  #空间步长
dt=0.1  #时间步长
wl=40
mu=np.zeros((lx,ly))
ep=np.zeros((lx,ly))
sigma=np.zeros((lx,ly))
sigmam=np.zeros((lx,ly))
mu0=1
ep0=2
sigma0=0
sigmam0=0
sigma1=2        #PML内σ
sigmam1=sigma1*mu0/ep0
"""
mu=1
ep=2
sigma=4
sigmam=sigma*mu/ep
"""

#赋值pml层内的sigma
for i in range(0,lx-1):
    for j in range(0,ly-1):
        if (lxx/2<i<lx-lxx/2)and(lyy/2<j<ly-lyy/2):
            mu[i,j]=mu0
            ep[i,j]=ep0
            sigma[i,j]=sigma0
            sigmam[i,j]=sigmam0
            
        else:
            mu[i,j]=mu0
            ep[i,j]=ep0
            sigma[i,j]=sigma1
            sigmam[i,j]=sigmam1


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

            gm1=(mu[j,k]/dt-sigmam[j,k]/2)/(mu[j,k]/dt+sigmam[j,k]/2)
            gm2=1/(mu[j,k]/dt+sigmam[j,k]/2)
            Hx2[j,k]=gm1*Hx1[j,k]-gm2/(dy)*(Ez1[j,k]-Ez1[j,k-1])
            Hy2[j,k]=gm1*Hy1[j,k]+gm2/(dx)*(Ez1[j,k]-Ez1[j-1,k])

    for j in range(0,lx-1):
        for k in range(0,ly-1):    #Ez的更新
            g1=(ep[j,k]/dt-sigma[j,k]/2)/(ep[j,k]/dt+sigma[j,k]/2)
            g2=1/(ep[j,k]/dt+sigma[j,k]/2)

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
        plt.imshow(np.log(Ez2**2).T,cmap='gray_r',vmin=-12, vmax=0)
        plt.colorbar()
        
"""
            if (lyy/2<k<ly-lyy/2)and(lxx/2<j<lx-lxx/2):
                if (j!=xx)or(k!=yy):
                    Ez2[j,k]=Ez1[j,k]+dt/ep*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
            else:           #pml层的更新
"""