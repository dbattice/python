# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:26:04 2017

@author: Devin
"""
import matplotlib,numpy,scipy
from math import pi, tan,exp,log,cos,sin
from time import clock
'Get order/number of equations in system'
n=int(input('Enter number of differential equations '))
'First order ODE'
if n==1:
    'Set initial conditions'
    tstart=clock()
    t0,tf=0,500.0
    t=t0
    y0=100
    yn=y0
    dt=.01
    yv=[y0]
    tv=[t0]
    'Define ODE to solve'
    def yprime(t,y):
        z=y
        return z
    'Solve ODE'
    while t<tf:
        j1=yprime(t,yn)
        j2=yprime(t+.5*dt,yn+.5*j1*dt)
        j3=yprime(t+.5*dt,yn+.5*j2*dt)
        j4=yprime(t+dt,yn+j3*dt)
        yn=yn+dt/6*(j1+2*j2+2*j3+j4)
        yv.append(yn)
        tv.append(t)
        t=t+dt
    'Plot solution'
    matplotlib.pyplot.plot(tv,yv)
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Displacement (m)')
    tend=clock()
    print(tend-tstart)

elif(n==2):
    '2nd order ODE or system of 2 ODEs'
    'Define initial conditions'
    tstart=clock()
    t0,tf=0,6.43
    t=t0
    x0,y0=0,1.0
    xn,yn=x0,y0
    dt=.001
    xv=[x0]
    yv=[y0]
    tv=[t0]
    cvtmaxt=3.4
    'Define ODEs'
    def xprime(t,x,y):
        z=y
        return z
    def yprime(t,x,y):
        z=(-y*y)
        return z

    'Solve equations'
    while t<=tf:
        j1=xprime(t,xn,yn)*dt
        k1=yprime(t,xn,yn)*dt
        j2=xprime(t+.5*dt,xn+.5*j1,yn+.5*k1)*dt
        k2=yprime(t+.5*dt,xn+.5*j1,yn+.5*k1)*dt
        j3=xprime(t+.5*dt,xn+.5*j2,yn+.5*k2)*dt
        k3=yprime(t+.5*dt,xn+.5*j2,yn+.5*k2)*dt
        j4=xprime(t+dt,xn+j3,yn+k3)*dt
        k4=yprime(t+dt,xn+j3,yn+k3)*dt
        yn=yn+(k1+2*k2+2*k3+k4)/6
        xn=xn+(j1+2*j2+2*j3+j4)/6
        xv.append(xn)
        yv.append(yn)
        tv.append(t)
        t=t+dt
    'Plot solution'
    matplotlib.pyplot.figure(1)
    matplotlib.pyplot.plot(tv,xv)
    matplotlib.pyplot.title('Position vs. Time')
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Displacement (m)')
    matplotlib.pyplot.figure(2)
    matplotlib.pyplot.plot(tv,yv)
    matplotlib.pyplot.title('Velocity vs. Time')
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Velocityt (m/s)')
    tend=clock()
    print(xn,yn)
    print(tend-tstart)

elif(n==3):
    'Third degree ODE or system of 3 ODEs'
    'Define ICs'
    tstart=clock()
    t0,tf=0,10
    t=t0
    x0,y0,z0=6,5,1
    xn,yn,zn=x0,y0,z0
    dt=.0001
    xv=[x0]
    yv=[y0]
    tv=[t0]
    zv=[z0]
    'Define ODEs'
    def xprime(t,x,y,z):
        a=z-x
        return a
    def yprime(t,x,y,z):
        a=x-y
        return a
    def zprime(t,x,y,z):
        a=y-z
        return a
    'Solve ODEs'
    while t<tf:
        j1=xprime(t,xn,yn,zn)*dt
        k1=yprime(t,xn,yn,zn)*dt
        l1=zprime(t,xn,yn,zn)*dt
        j2=xprime(t+.5*dt,xn+.5*j1,yn+.5*k1,zn+.5*l1)*dt
        k2=yprime(t+.5*dt,xn+.5*j1,yn+.5*k1,zn+.5*l1)*dt
        l2=zprime(t+.5*dt,xn+.5*j1,yn+.5*k1,zn+.5*l1)*dt
        j3=xprime(t+.5*dt,xn+.5*j2,yn+.5*k2,zn+.5*l2)*dt
        k3=yprime(t+.5*dt,xn+.5*j2,yn+.5*k2,zn+.5*l2)*dt
        l3=zprime(t+.5*dt,xn+.5*j2,yn+.5*k2,zn+.5*l2)*dt
        j4=xprime(t+dt,xn+j3,yn+k3,zn+l3)*dt
        k4=yprime(t+dt,xn+j3,yn+k3,zn+l3)*dt
        l4=zprime(t+dt,xn+j1,yn+k1,zn+l3)*dt
        zn=zn+(l1+2*l2+2*l3+l4)/6
        yn=yn+(k1+2*k2+2*k3+k4)/6
        xn=xn+(j1+2*j2+2*j3+j4)/6
        xv.append(xn)
        yv.append(yn)
        zv.append(zn)
        tv.append(t)
        t=t+dt
        'Plot solution'
    matplotlib.pyplot.subplot(311)
    matplotlib.pyplot.plot(tv,xv)
    matplotlib.pyplot.title('Position vs. Time')
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Displacement (m)')
    matplotlib.pyplot.subplot(312)
    matplotlib.pyplot.plot(tv,yv)
    matplotlib.pyplot.title('Velocity vs. Time')
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Velocityt (m/s)')
    matplotlib.pyplot.subplot(313)
    matplotlib.pyplot.plot(tv,zv)
    matplotlib.pyplot.title('Accleration vs. Time')
    matplotlib.pyplot.xlabel('Time (s)')
    matplotlib.pyplot.ylabel('Acceleration (m/s^2)')
    tend=clock()
    print(tend-tstart)

else:
    'Error'
    print('Not valid')