import numpy as np
from numpy.core.fromnumeric import prod
n, m = list(map(int,input().split()))
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
myarr = np.array(a)
myarr=np.min(myarr,axis=1)
print(np.max(myarr))