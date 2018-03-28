print(abs(-5))
a=abs
print(a(-6))

def myabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad type ')
    if x>0:
        return x
    else:
        return - x


print(myabs(-8))


def non(age):
    # empty function
    pass

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/5)
print(x,y)
# when return one more object , they will be a tuple
res=move(100,100,60,math.pi/5)
print(res)


def sumAll(arrayNum):
    result = 0
    for num in arrayNum:
        result+=num
    return result
print(sumAll([1,3,5]))

def sumAll2(*tuple):
    result=0
    for num in tuple:
        result+=num
    return result

print(sumAll2(1,2,4,5))