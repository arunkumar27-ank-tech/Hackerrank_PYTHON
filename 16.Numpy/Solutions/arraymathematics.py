import numpy as np
m,n = list(map(int,input().split()))
arr1 = np.array([input().split() for _ in range(m)],int)
arr2 = np.array([input().split() for _ in range(m)],int)
for operator in '+ - * // % **'.split():
    print(eval(f'arr1{operator}arr2'))