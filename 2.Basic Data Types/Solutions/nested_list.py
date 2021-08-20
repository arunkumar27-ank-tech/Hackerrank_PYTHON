n = int(input())
lst = []
for _ in range(n):
    name = str(input())
    mark = int(input())
    lst.append([name,mark])
dct =dict(lst)
arange = list(sorted(set(dct.values())))
#arange1 = list(sorted(set(dct.items())))
#print(arange)
#print(arange1)
second = arange[1]
names=[]
for name,mark in dct.items():
    if mark==second:
       names.append(name)
names.sort()
for i in names:
    print(i)
#print(arange)
#print(second)
#for items in dct.values():
 #   print(items)
#print(lst)
#print(dct)