import numpy as np


# basic param
a=np.arange(15).reshape(3,5)

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))


# Array Creation
b1=np.array([6,7,8])
print(b1)
print(type(b1))

b2=np.array([(1,2,3),(4,5,6)])
print(b2)

c=np.array([1,2,3],dtype=complex)
print(c)

# zeros

print(np.zeros((3,4)))

print(np.ones((3,4,5),dtype=np.int16))

print(np.empty((2,3)))

print(np.arange( 10, 30, 5 ))

print(np.linspace(0,2,9))