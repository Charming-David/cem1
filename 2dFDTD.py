# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:20:27 2020
2d FDTD 
@author: lenovo
"""
import numpy as np
from matplotlib import pyplot as plt

lt=40 #时间长度
lx=60 
ly=60  #空间大小
dx=0.1
dy=0.1  #空间步长
dt=0.1  #时间步长
wl=20
mu=1
ep=2
Hx1=np.zeros((lx,ly))
Hx2=np.zeros((lx,ly))
Hy1=np.zeros((lx,ly))
Hy2=np.zeros((lx,ly))
Ez1=np.zeros((lx,ly))
Ez2=np.zeros((lx,ly))
X=np.arange(0,lx*dx,dx)
Y=np.arange(0,ly*dy,dy)
X, Y = np.meshgrid(X, Y)
xx=int(lx/2)
yy=int(ly/2)
for i in range(0,lt-1):


    for j in range(0,lx-1):
        for k in range(0,ly-1):         #Hx与Hy的更新
            Hx2[j,k]=Hx1[j,k]-1*dt/(dy*mu)*(Ez1[j,k]-Ez1[j,k-1])
            Hy2[j,k]=Hy1[j,k]+1*dt/(dx*mu)*(Ez1[j,k]-Ez1[j-1,k])
    for j in range(0,lx-1):
        for k in range(0,ly-1):    #Ez的更新
            if (j!=xx)or(k!=yy):
                Ez2[j,k]=Ez1[j,k]+1*dt/ep*((Hy2[j+1,k]-Hy2[j,k])/dy-(Hx2[j,k+1]-Hx2[j,k])/dx)
                
    Ez2[xx,yy]=np.sin(np.pi*2*i/wl)  #源点不参与更新               
    Ez1[:,:]=Ez2[:,:]
    Hx1[:,:]=Hx2[:,:]
    Hy1[:,:]=Hy2[:,:]
    
    Ez1[0,:]=0
    Ez1[lx-1,:]=0
    Ez1[:,0]=0
    Ez1[:,ly-1]=0
    if i==lt-2:
        """
        fig = plt.figure()  #定义新的三维坐标轴
        ax = plt.axes(projection='3d')
        ax.plot_surface(X,Y,Ez2,cmap='rainbow')
        """
        fig=plt.imshow(10*np.log(Ez2**2),cmap='gray_r')
        