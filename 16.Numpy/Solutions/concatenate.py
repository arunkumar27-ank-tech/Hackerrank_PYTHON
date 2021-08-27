import numpy as np
m,n,p = input().split()
l1 =[]
l2 =[]
for _ in range(int(m)):
    l1.append(input().split())

for _ in range(int(n)):
    l2.append(input().split())

print(np.concatenate((np.array(l1,int),np.array(l2,int)),axis=0))