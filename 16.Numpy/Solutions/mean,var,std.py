import numpy as np
m,n = list(map(int,input().split()))
a=[]
for _ in range(m):
    a.append(list(map(int,input().split())))
my_array = np.array(a)
print(np.mean(my_array,axis=1))
print(np.var(my_array,axis=0))
stds=np.std(my_array,axis=None)
print(np.around(stds,11))



