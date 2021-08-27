n,x = list(map(int,input().split()))
mark = []
for i in range (x):
    mark.append(tuple(map(float,input().split()))) #tuple is immutable y marks are converted into tuple
#print(mark)
zipped = list(zip(*mark))
#print(zipped)
for value in zipped:
    print(sum(value)/len(value))