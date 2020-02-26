# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:16:00 2018

@author: Devin
"""

'Algebra'
from math import sin,cos,atan,asin,acos,pi,sqrt
origin=input('enter vector for vectors, tri for triangle solver, quad for quadratic formula ')
if origin=='vector':
    in1=int(input('enter number of dimensions'))
    in2=input('enter comp to solve for components or ma for magnitude and direction')
    if in1==2 and in2=='comp':
        mag=float(int(input('magnitude')))
        angle=float(int(input('angle in degrees')))
        x=mag*cos(angle*pi/180)
        y=mag*sin(angle*pi/180)
        print('<'+x+', '+y+'>')
    elif in1==2 and in2=='ma':
        x=float(int(input('enter x component')))
        y=float(int(input('enter y component')))
        mag=sqrt(x*x+y*y)
        angle=atan(y/x)
        print(str('r='),mag,str(', theta='),angle)
    elif in1==3 and in2=='comp':
        mag=float(int(input('magnitude')))
        theta=float(int(input('theta in degrees')))
        phi=float(int(input('phi in degrees')))
        x=mag*cos(theta*pi/180)*sin(phi*pi/180)
        y=mag*sin(theta*pi/180)*sin(phi*pi/180)
        z=mag*cos(phi*pi/180)
        print('<',x,', ',y,', ',z,'>')
    elif in1==3 and in2=='ma':
        x=float(int(input('enter x component')))
        y=float(int(input('enter y component')))
        z=float(int(input('enter z component')))
        mag=sqrt(x*x+y*y+z*z)
        phi=acos(z/mag)
        theta=acos(x/(sin(phi)*mag))
        print('r='+str(mag)+', theta='+str(theta)+', phi='+str(phi))
elif origin=='quad':
    a=float(int(input('enter a ')))
    b=float(int(input('enter b ')))
    c=float(int(input('enter c ')))
    discriminant=b*b-4*a*c
    if discriminant>=0:
        r1=(-b+sqrt(discriminant))/(2*a)
        r2=(-b-sqrt(discriminant))/(2*a)
        print(r1, r2)
    else:
        print('no real roots')
elif origin=='tri':
    knowns=input('enter sss, sas, asa, ssa, aas ')
    if knowns=='sss':
        a=float(int(input('a ')))
        b=float(int(input('b ')))
        c=float(int(input('c ')))
        alpha=acos((a*a-b*b-c*c)/(-2*b*c))*180/pi
        beta=acos((-a*a+b*b-c*c)/(-2*a*c))*180/pi
        gamma=acos((-a*a-b*b+c*c)/(-2*b*a))*180/pi
        print(alpha, beta, gamma)
    elif knowns=='ssa':
        a=float(int(input('a ')))
        b=float(int(input('b ')))
        alpha=float(int(input('alpha ')))
        beta=asin(b/a*sin(alpha*pi/180))*180/pi
        gamma=180-beta-alpha
        c=a/sin(pi/180*alpha)*sin(gamma*pi/180)
        print(c, beta, gamma)
    elif knowns=='sas':
        a=float(int(input('a ')))
        b=float(int(input('b ')))
        gamma=float(int(input('gamma ')))
        c=sqrt(b*b+a*a-2*a*b*cos(pi/180*gamma))
        alpha=acos((a*a-b*b-c*c)/(-2*b*c))*180/pi
        beta=acos((-a*a+b*b-c*c)/(-2*a*c))*180/pi
        print(alpha, beta, c)
    elif knowns=='asa':
        alpha=float(int(input('enter a ')))
        beta=float(int(input('enter beta')))
        gamma=180-alpha-beta
        c=float(int(input('c ')))
        b=c/sin(gamma*pi/180)*sin(beta*pi/180)
        a=c/sin(gamma*pi/180)*sin(alpha*pi/180)
        print(a, b, gamma)
    elif knowns=='aas':
        alpha=float(int(input('enter a ')))
        beta=float(int(input('enter beta')))
        gamma=180-alpha-beta
        c=float(int(input('c ')))
        b=c/sin(gamma*pi/180)*sin(beta*pi/180)
        a=c/sin(gamma*pi/180)*sin(alpha*pi/180)
        print(a, b, gamma)