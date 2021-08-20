from collections import defaultdict
d = defaultdict(list)
list1 = []
n, m = map(int,input().split())


for i in range (n):
    k = input()
    d[k].append(i+1)
for j in range(m):
    l=input()
    list1.append(l)
for k in list1:
    if (k in d):
        print(" ".join(map(str,d[k])))
    else:
        print(-1)
    
    
        
    
