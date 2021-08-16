import operator
n , m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
#k = int(input())
arr.sort(key=operator.itemgetter(1))
for i in arr:
    print(*i)