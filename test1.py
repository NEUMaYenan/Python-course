def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else: return -x

from math import cos,sin
import math
def move(x,y,step,angle=0):
    nx=x+step*cos(angle)
    ny=y-step*sin(angle)
    return nx, ny

def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(int,float)):
            raise TypeError('bad operand type')
    if a==0:
        print('错误，a=0'),
    else:
        d=b**2-4*a*c
        if d<0:
            print('方程无实数解')
        elif d==0:
            print('方程有两个相等的解,x1=x2=',-b/(2*a))
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            print('方程有两个不相等的解:','x1=',x1,'x2=',x2)

def findMinAndMax(L):
    if L==[]:
        return(None,None)
    elif L!=[]:
        Min=L[0]
        Max=L[0]
        for i in L:
            if i<Min:
                Min=i
            if i>Max:
                Max=i
        return(Min,Max)
