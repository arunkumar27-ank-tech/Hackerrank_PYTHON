import numpy

def arrays(arr):
    a=numpy.array(arr[::-1])
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)