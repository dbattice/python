# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:44:55 2019

@author: Devin
"""
from math import pi
from time import clock
from matplotlib import pyplot
tstart=clock()
t0,tf=0,10
t=t0
x0,y0=0.0,0.0
xn,yn=x0,y0
dt=.001
xv=[x0]
yv=[y0]
tv=[t0]
cvtv=[3.38]
rpmv=[1850]
cvtmaxt=3
cvtengaget=.05
gr=10
cd=.98
area=12.0
rhoair=.0765/32.2
mtotal=650/32.2
tiredm=23/12
ff=18.0
vmaxrl=tiredm*pi/60*3820/(gr*.54)
print('The ratio limited top speed is '+str(vmaxrl))
vmaxpl=(9*550/(cd*.5*area*rhoair))**(1/3)
print('The ratio limited top speed is '+str(vmaxpl))
eta=.72
def xprime(t,x,y):
    z=y
    return z
def yprime(t,x,y):
    z=(eta*torque(t)*gr*cvt(t)/(tiredm/2)-ff-y*y*.5*cd*area*rhoair)/(mtotal)
    return z
def cvt(t):
    if t<=cvtengaget:
        cvt=3.38
    elif t>=cvtmaxt:
        cvt=.54
    else:
        cvt=(3.38-2.84/(cvtmaxt-cvtengaget)*(t-cvtengaget))
    return cvt
def rpm(t):
    cvtmaxrpm=cvtmaxt*(382-185)/(375-185)
    if t<cvtmaxrpm:
        rpm=t/cvtmaxrpm*(3820-1850)+1850
    else:
        rpm=3820
    return rpm
def torque(t):
    cvtmaxrpm=cvtmaxt*(382-185)/(375-185)
    if t<cvtmaxrpm:
        rpm=t/cvtmaxrpm*(3820-1850)+1850
    else:
        rpm=3820
    teng=14-1/(810000)*(rpm-2700)*(rpm-2700)
    return teng
torquev=[torque(0)]
while (t<tf):
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
    rpmv.append(rpm(t))
    cvtv.append(cvt(t))
    torquev.append(torque(t))
    t=t+dt
    tend=clock()
pyplot.figure()
pyplot.plot(tv,xv)
pyplot.figure()
pyplot.plot(tv,yv)
pyplot.figure()
pyplot.plot(tv,rpmv)
pyplot.figure()
pyplot.plot(tv,cvtv)
pyplot.figure()
pyplot.plot(tv,torquev)
pyplot.figure()
pyplot.plot(rpmv,cvtv)