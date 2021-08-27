import numpy as np
m,n = list(map(int, input().split()))
a=[]
for _ in range(m):
    a.append(list(map(int, input().split())))
#print(a)
myarray = np.array(a)
print(np.prod(myarray))