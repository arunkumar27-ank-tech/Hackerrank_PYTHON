#print (set(set(['H','a','c','k','e','r','r','a','n','k'])))
n=int(input())
heights = list(map(int, input().split()))
avg = set(heights)
res = sum(avg)/len(avg)
print(res)