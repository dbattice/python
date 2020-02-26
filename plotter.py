# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:40:22 2017

@author: Devin
"""
"print(dir(matplotlib),dir(numpy),dir(scipy))"
import matplotlib
from math import sin,cos,pi,log,exp
from csv import reader, writer,QUOTE_NONNUMERIC
x1=[]
fy1=[]
x2=[]
fy2=[]
x3=[]
fy3=[]
x4=[]
fy4=[]
x5=[]
fy5=[]
dx=1/100
def y1(j):
    z=exp(-j*j*j*j*j*j*j*j)
    x1.append(j)
    fy1.append(z)
    return 0
def y5(j):
    z=exp(-j*j*j*j*j*j*j*j*j*j)
    x5.append(j)
    fy5.append(z)
    return 0
def y2(j):
    z=exp(-j*j*j*j*j*j)
    x2.append(j)
    fy2.append(z)
    return 0
def y3(j):
    z=exp(-j*j*j*j*j*j)
    x3.append(j)
    fy3.append(z)
    return 0
def y4(j):
    z=exp(-j*j*j*j*j*j*j*j)
    x4.append(j)
    fy4.append(z)
    return 0
i=-2
while i<=(2):
    y1(i)
    y2(i)
    y3(i)
    y4(i)
    y5(i)
    i=i+dx
matplotlib.pyplot.figure()
matplotlib.pyplot.plot(x1,fy1)
matplotlib.pyplot.plot(x2,fy2)
matplotlib.pyplot.plot(x3,fy3)
matplotlib.pyplot.plot(x4,fy4)
matplotlib.pyplot.plot(x5,fy5)
matplotlib.pyplot.xlabel('Time (s)')
matplotlib.pyplot.ylabel('Displacement (m)')
with open('datatest.csv', newline=None)as csv:
    data=reader(csv,delimiter=',',quoting=QUOTE_NONNUMERIC)
    a=[]
    b=[]
    for row in data:
        a.append(row[0])
        b.append(log(row[1]))
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(a,b)
    