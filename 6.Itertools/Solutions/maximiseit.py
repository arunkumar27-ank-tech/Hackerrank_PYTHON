import itertools
n, modu = map(int,input().split())
alist=[]
for i in range (n):
    alist.append(list(set([(j**2) for j in list(map(int, input().split()))[1:]])))
#print([(i) for i in itertools.product(*alist)])
#print([sum(i)%modu for i in itertools.product(*alist)])
print(max([sum(i)%modu for i in itertools.product(*alist)]))