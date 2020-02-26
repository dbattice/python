# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:22:24 2019

@author: Devin
"""
from numpy import poly1d,polymul
from numpy import polynomial as poly
from math import sin,cos,exp,log,pi,sqrt,atan,tan,atan2
from numpy import array
"Controls Root Locus"
"num and dem start with constant term then increase by degree"
num=poly1d([1,2])
den=poly1d([1,6,11,6])
'''
Root locus requires a close loop transfer function with unity feedback

When drawing root locus, lines leave poles and go to zeros
lines go from left to right but only if there are an odd number 
of poles and zeros to the right
For optimal responses the actual poles/zeros should be below the 50deg line
'''
'Requires system to be in k/(s*s+a*s+b)'
def sysanalysis(a,b):
    freq=sqrt(b)
    zeta=a/(freq*2)
    overshoot=exp(-zeta*pi/sqrt(1-zeta*zeta))
    tau=1/(zeta*freq)
    peaktime=pi/(freq*sqrt(1-zeta*zeta))
    print("Frequency "+str(freq))
    print("Damping ratio/zeta "+str(zeta))
    print("overshoot "+str(overshoot))
    print("Time constant "+str(tau))
    print("Peak time "+str(peaktime))
    
def designUDsys(overshoot, settime):
    tau=settime/4
    zeta=-log(overshoot)/sqrt(pi*pi+log(overshoot)*log(overshoot))
    freq=4/(settime*zeta)
    peaktime=pi/(freq*sqrt(1-zeta*zeta))
    print("Time constant "+str(tau))
    print("Damping ratio/zeta "+str(zeta))
    print("Frequency "+str(freq))
    print("Peak time "+str(peaktime))
    
def rootlocus(numerator,denominator):
    numroots=poly.polynomial.polyroots(numerator)
    denroots=poly.polynomial.polyroots(denominator)
    rootlocuspoly=poly.polynomial.polymul(numerator,denominator)
    prodnum,prodden=1,1
    poleintercepts,zerointercepts=0.0,0.0
    for i in numroots:
        prodnum=prodnum*abs(i)
        zerointercepts=zerointercepts+i.real
        print(zerointercepts)
    for i in denroots:
        prodden=prodden*abs(i)
        poleintercepts=poleintercepts+i.real
    kgain=prodden/prodnum
    sigmap=poleintercepts-zerointercepts/(len(denroots)-len(numroots))
    print("SS gain "+str(kgain))
    thetadenom=(len(denroots)-len(numroots))
    print(rootlocuspoly)
    print("Poles: "+str(denroots))
    print("Zeroes: "+str(numroots))
    print("Intercept: "+str(sigmap))
    print("theta=(2k+1)/"+str(thetadenom)+'*pi')


'''
Compensators/controllers
Adding zeroes decreases rise time and peak time but increases overshoot
Adding poles decrease overshoot, slow down response time,
RHP make the system unstable
Adding 1/s redcues steady state error
Transient response can be improved by adding a differentiating controller (s)
'''



's=a+bi'

def findgain(numerator,denominator):
    numroots=poly.polynomial.polyroots(numerator)
    denroots=poly.polynomial.polyroots(denominator)
    prodnum,prodden=1,1
    for i in numroots:
        prodnum=prodnum*abs(i)
    for i in denroots:
        prodden=prodden*abs(i)
    kgain=prodden/prodnum
    print(kgain)
def findpole(targa):
    newpolea=-10*targa.imag+targa.real
    return newpolea
def findzero(os,tau,numerator,denominator):
    a=log(os)
    zeta=sqrt(a*a/(pi*pi+a*a))
    freq=4/(tau*zeta)
    point=complex(-zeta*freq,sqrt(1-zeta*zeta))
    print('found point '+str(point))
    numroots=poly.polynomial.polyroots(numerator)
    denroots=poly.polynomial.polyroots(denominator)
    angles=0
    for i in numroots:
        angles=angles-atan((point.imag-i.imag)/(point.real-i.real))
    for i in denroots:
        angles=angles+atan((point.imag-i.imag)/(point.real-i.real))
    angle=180+angles*180/pi
    print('angle '+str(angle))
    zc=freq/tan(angle*pi/180)*(zeta*tan(angle)+sqrt(1-zeta*zeta))
    return zc
pole=-3+2j

overshoot=.1
tau=.5


newpole=poly1d([1,findpole(pole)])
print('new pole '+str(newpole))

newzero=poly1d([1,findzero(overshoot,tau,num,den)])
print(newzero)
'lag/lead'
findgain(polymul(num,newzero),polymul(den,newzero))
rootlocus(polymul(num,newzero),polymul(den,newzero))

'''Frequency Response Bode Plots


M=abs(G)=abs(G(omega*j))
phio=arctan(1/(omega*j+1))
yaxis in db: 20log(M)/log(10)
slope of db/decade changes based on poles
also y axis is phase angle
xaxis on both is log10 scale of frequency
Crossover frequency- frequency in which M=0
omegac
phase margin =180+omegac
gain margin  gain to 0dB when phase =-180

bodeplot


'''
freq=array([-5.0,-4.5,-4.0,-3.5,3.0,-2.5,2.0,-1.5,-1.0,-.5,0.0,.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0])
tens=array([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
x=pow(tens,freq)
print(x)
def G(s):
    y=(s+5)
    return y
ygain=[20*log(abs(G(10**(-5.0))))]
yphase=atan2(G(10**(-5)).real,G(10**(-5)).imag)


'''Nyquist criterion
draw a closed loop which is the set of inputs/encloses inputs
if the zero is outside the look, the loop maps to a shift by the value of the zero from the origin
if a pole is outside the loop, the loop maps onto a reflection over the x axis and a shifts 


equal # of poles and zeroes won't encircle origin but will reverse direction
z>p encircle origin in same direction
z<p encircle origin reverse direction

CL poles=zeroes of GH
poles of GH= poles of CL transfer function

draw loop around all poles/zeros in RHP
1+GH=(DgDh+NgNh)/(DgdDh)
clockwise encirclements of -1=z-p
we know open loop poles and encirclements'''

