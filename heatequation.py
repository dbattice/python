# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:03:44 2019

@author: Devin
"""
from math import exp,tan,cos,pi,sin,log,sqrt,erf
from scipy.special import j0,j1
type=input('Enter type of problem ')

'cylindrical, 1d, SS, no heat gen'
print('1/r*d(r*dT/dr)/dr=0, sol=k1*ln(r)+k2')
'cylindrical, 1d, SS, heat gen'
print('1/r*d(r*dT/dr)/dr=-egen, sol=-egen/4*r^2+k1*ln(r)+k2')
'spherical, 1d, SS, no heat gen'
print('1/r^2*d(r^2*dT/dr)/dr=0, sol=k1/r+k2)')
'spherical, 1d, SS, heat gen'
print('1/r*d(r*dT/dr)/dr=-egen, sol=-egen/6*r^2+k1/x+k2')


'Wall no heat gen'
if str(type)==('car1dssnhg'):
    T0=50
    Tl=20
    l=3
    qdot=3000
    'BC: 2 temperatures'
    k2=T0
    k1=(Tl-k2)/l
    print('T(x)='+str('k1')+'*x+'+str('k2'))
    'BC: 1 Temp and 1 Rate'
    k1=qdot
    k2=T0
    k2=Tl-k1*l
    print('T(x)='+str('k1')+'*x+'+str('k2'))

'Wall heat gen'
if str(type)==('car1dssnhg'):
    T0=50
    Tl=20
    l=3
    qdot=3000
    edot=-2000
    'BC: 2 temperatures'
    k3=T0
    '(Tl-k3-edot/2*l*l)/l'
    print('T(x)='+str('k1')+'*x+'+str('k2'))
    'BC: 1 Temp and 1 Rate'
    k3=T0
    k2=qdot-edot*l
    'if rate is given at x=0'
    k2=qdot
    print('T(x)='+str('k1')+'*x+'+str('k2'))
    
'Semi-infinite Solids'
if str(type)==('semiinfsolid'):
    t=3
    x=0
    alpha=2.3e-5
    eta=x/sqrt(4*alpha*t)
    Tm=20
    T0=5
    T=(Tm-T0)*erf(eta)+T0
    print('Temperature at time t '+str(T))
'Lumped system'
if str(type)=='lumpedsys':
    t=30
    lc=5
    h=40
    k=.6
    rho=5400
    a=5
    cp=400
    vol=5
    b=h*a/(rho*cp*vol)
    Theta=exp(-b*t)
    T=100
    Tinf=20
    Ti=150
    t=log((T-Tinf)/(Ti-Tinf))/(-b)
'sswall'
k=.4
a=1
Ti=10
To=20
L=.1
area=40
qdot=k*a*(To-Ti)/L
'sscyl'
r1=.1
r2=1.1
Rcyl=log(r2/r1)/(2*pi*k*L)
qdot=(To-Ti)/Rcyl
'sssphere'
Rsph=(r2-r1)/(2*pi*k*r1*r2)
qdot=(To-Ti)/Rsph

'Transient constants'
n=0
xnow=.1
Bi=.3
alpha=5.6e-6
t=64000
m,y=0.0,0
xnext=0
r0=.5
r=.1
'Transient heat conduction'
if str(type)=='transientwall':
    thetawall=0
    n=0
    xnow=.1
    Bi=.3
    alpha=5.6e-6
    t=64000
    m,y=0.0,0
    xnext=0
    tauwall=alpha*t/(y*y)
    'd=distance from center of wall, L=half of wall thickness'
    d=.05
    L=.5
    xnow=.1
    for n in range(11):
        xnext=xnow-(xnow*tan(xnow)-Bi)/(tan(xnow)+xnow/(cos(xnow)*cos(xnow)))
        thetawall=4*sin(xnext)/(2*xnext+sin(2*xnext))*exp(-xnext*xnext*tauwall)*cos(xnext*d/L)
    for lambdan in range(1,21):
        xnow=lambdan*pi
        for n in range(11):
            xnext=xnow-(xnow*tan(xnow)-Bi)/(tan(xnow)+xnow/(cos(xnow)*cos(xnow)))
            xnow=xnext
        thetawall=thetawall+4*sin(xnext)/(2*xnext+sin(2*xnext))*exp(-xnext*xnext*tauwall)*cos(xnext*d/L)
    print("theta wall = "+str(thetawall))

'Transient cylinders'
if str(type)=='transientcyl':
    xnow=.01
    taucyl=1
    for n in range(11):
        xnext=xnow-(xnow*j0(xnow)*j1(xnow)-Bi*j0(xnow)*j0(xnow))/(j0(xnow)*j0(xnow)*xnow+j1(xnow)*j1(xnow)*xnow)
        xnow=xnext
        thetacyl=0
        xnow=.1
    thetacyl=thetacyl+2/xnext*j1(xnext)/(j0(xnext)*j0(xnext)+j1(xnext)*j1(xnext))*exp(-xnext*xnext*taucyl)*j0(xnext*r/r0)
    for lamc in range(1,21):
        xnow=lamc*pi
        for n in range(11):
            xnext=xnow-(xnow*j0(xnow)*j1(xnow)-Bi*j0(xnow)*j0(xnow))/(j0(xnow)*j0(xnow)*xnow+j1(xnow)*j1(xnow)*xnow)
            xnow=xnext
        thetacyl=thetacyl+2/xnext*j1(xnext)/(j0(xnext)*j0(xnext)+j1(xnext)*j1(xnext))*exp(-xnext*xnext*taucyl)*j0(xnext*r/r0)
    print("theta cylinder = "+str(thetacyl))

'Transient Spheres'
if str(type)=='transientsphere':
    thetasph=0
    tausph=alpha*t/(r0*r0)
    xnext=0
    xnow=.1
    for n in range(11):
        xnext=xnow-(1-xnow/tan(xnow)-Bi)/(-1/tan(xnow)+xnow/(sin(xnow)*sin(xnow)))
        xnow=xnext
    thetasph=thetasph+4*(sin(xnext)-xnext*cos(xnext))/(2*xnext-sin(2*xnext))*exp(-xnext*xnext*tausph)*sin(xnext*r/r0)/(xnext*r/r0)
    xnow=.1
    for lamc in range(1,21):
        xnow=lamc*pi
        for n in range(11):
            xnext=xnow-(1-xnow/tan(xnow)-Bi)/(-1/tan(xnow)+xnow/(sin(xnow)*sin(xnow)))
            xnow=xnext
        thetasph=thetasph+4*(sin(xnext)-xnext*cos(xnext))/(2*xnext-sin(2*xnext))*exp(-xnext*xnext*tausph)*sin(xnext*r/r0)/(xnext*r/r0)
    print("theta sphere = "+str(thetasph))
