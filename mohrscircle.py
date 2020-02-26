# -*- coding: utf-8 -*-
"""
Devin Battice

This is a temporary script file.
"""
from math import sin,cos,atan,sqrt,pi
sigx=8
sigy=0
tau=6
thetar=0
siga=.5*(sigx+sigy)
sigxp=siga+(sigx-sigy)*.5*cos(2*thetar)+tau*sin(2*thetar)
sigyp=siga-(sigx-sigy)*.5*cos(2*thetar)-tau*sin(2*thetar)
taup=-(sigx-sigy)*.5*sin(2*thetar)+tau*cos(2*thetar)
thetap=atan(2*tau/(sigx-sigy))*90/pi
thetas=atan((sigy-sigx)/2*tau)*90/pi
sigmax=siga+sqrt((sigx-sigy)**2/4+tau*tau)
sigmin=siga-sqrt((sigx-sigy)**2/4+tau*tau)
taumax=sqrt((sigx-sigy)**2/4+tau**2)
print("sigmin,sigmax,taumax,sigxp,sigyp,taup,thetap,thetas,")
print(sigmin,sigmax,taumax,sigxp,sigyp,taup,thetap,thetas,)

"Values to find stress/factor of safety"
ms=60
n=1.3
s1=15
s2=10
taumax=10
"MSS"
msn=n*(s1-s2)
nn=ms/(s1-s2)
print('MSS Factors of safety')
print(nn,msn)
mst=n*2*taumax
nt=ms/(2*taumax)
print(nt,mst)
"von Mises Stress"
vmms=n*sqrt(s1*s1-s1*s2+s2*s2+3*taumax*taumax)
vmn=ms/sqrt(s1*s1-s1*s2+s2*s2+3*taumax*taumax)
print('von Mises stress')
print('von Mises stress = '+str(vmms))
print('von Mises shear stress = '+str(mst))
print('von Mises safety factor = '+str(vmn))
"Shaft design diameter and factor of safety"
sut,sy,se=64,42,32
Kf,Kfs=1.0,1.0
Mavg=0
Malt=50
Tavg=24
Talt=0
a=sqrt(4*Kf*Kf*Malt*Malt+3*Kfs*Kfs*Talt*Talt)
b=sqrt(4*Kf*Kf*Mavg*Mavg+3*Kfs*Kfs*Tavg*Tavg)
d=1.5
n=1
'Marin Factors'
ka=1*sut**(.87)
kb=.9*d**(-.107)
kc=.59
'temperature'
kd=1
ke=1-.08*.01
kf=1
se=ka*kb*kc*kd*ke*kf*se
if d==0.0:
    print('diamters')
    "DE-Gerber"
    dger=(8*n*a/(pi*se)*(1+sqrt(1+4*b*b*se*se/(a*a*sut*sut))))**(1/3)
    "DE-Goodman"
    dgood=(16*n/pi*(a/se+b/sut))**(1/3)
    "ASME Elliptical"
    dasme=(16*n/pi*sqrt(a*a/(se*se)+b*b/(sut*sut)))**(1/3)
    "DE-Soderberg"
    dsod=(16*n/pi*(a/se+b/sy))**(1/3)
    print("Gerber "+str(dger))
    print("Goodman "+str(dgood))
    print("ASME "+str(dasme))
    print("Soderberg "+str(dsod))
else: 
    print("Factors of safety")
    "DE-Gerber"
    nger=pi*d*d*d*se/(8*a*(1+sqrt(1+4*b*b*se*se/(a*a*sut*sut))))
    "DE Goodman"
    ngood=pi*d*d*d/(16*a/se+16*b/sut)
    "ASME Elliptical"
    nasme=pi*d*d*d/(16*sqrt(a*a/(se*se)+b*b/(sut*sut)))
    "DE-Soderberg"
    nsod=pi*d*d*d/(16*a/se+16*b/sy)
    print("Gerber "+str(nger))
    print("Goodman "+str(ngood))
    print("ASME "+str(nasme))
    print("Soderberg "+str(nsod))
