# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:55:40 2019

@author: Naufal Basyah
"""

from sympy import *
import numpy as np

x= Symbol("x")   

#def diff(stringEq):
#    x= Symbol("x")                                                       #method to turn an equation string into a lambda derrivative equation
#    y=stringEq
#    yprime=y.diff(x)
#    y=sp.lambdify(x,yprime)
#    return y

                                                            
def rootNewton(f,xpoint):

    count=0
    
    x = Symbol("x")
    y = eval(f)
    f = lambdify(x,y)
    fprim = diff(y)
    fprime = lambdify(x,fprim)
    xt = xpoint
  
    while (True):
        count += 1
        xt = xt - (f(xt)/fprime(xt))
        if (abs(f(xt) <= 1.0E-6)):
            print("The closest approximation for the root using Newton-Rhapson Mehtod is :", xt,"\nAnd it went through",count,"number of iteration(s)")
            return xt
        elif count>1000:
            return -99999,count
    
#    while (True):
#        x1=x0-(f(xpoint)/fprime(xpoint))
#        count+=1
#        if f(x1)-f(x0)< 1.0E-6:
#            print("The closest approximation for the root using Newton-Rhapson Mehtod is :", x1,"\nAnd it went through",count,"number of iteration(s)")
#            return x1,count
#
#        else:
#            x0=x1
                                                                                        #methods to approximate the root(s) of a polynomial equation
def bisectionRoot(f1,a,b):
    
    f= lambda x : eval(f1)
    N=1000
    if f(a)*f(b) >= 0:
        print("Bisection method fails1.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            print(m_n)
            return m_n
        else:
            print("Bisection method fails2.")
            return None
    return (a_n + b_n)/2

def centralDiffApp(f1,xpoint,a,b):
    
    f =lambda x: eval(f1)
   
    x=xpoint
    h=[]
    for i in range(a*100,b*100):
        if i==b*100-1:
            h.append(b)
        else:
            h.append(i/100)
    fwd= []
    bwd= []
    approx=[]
    fwd2=[]
    bwd2=[]                                                         #method to approximate a derivative of a polynomial equation at a ceertain point
    for i in range(0,len(h)):
        fw1=f(x+h[i])
        fwd.append(fw1)
        bw1=f(x-h[i])
        bwd.append(bw1)
        fw2=f(x+2*h[i])
        fwd2.append(fw2)
        bw2=f(x-2*h[i])
        bwd2.append(bw2)
        
    for i in range(0,len(fwd)):
#        print("%f ===== %f"%(bwd[i],f(x-h[i])),"\n")
        res= (fwd[i]-bwd[i])/(2*h[i])
        approx.append(res)
    print("The approximates for f'(%d) are:")
    total=0
    for g in approx:
        total+=g
    print (total/len(approx))
    return total/len(approx)

# x= sp.Symbol("x")
# f= x**2+(4*x)-12
# xApprox,count=rootNewton(f,4)
# centralDiffApp(f,2,3,5)
# bisectionRoot(f,-5,10)
    



