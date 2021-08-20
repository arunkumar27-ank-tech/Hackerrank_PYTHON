from itertools import *

N = int(input())
element = input().split()
K = int(input())
count = 0
combi = list(combinations(element, K))
#print(combi)
#print(len(combi))
for i in combi:
    if 'a' in i:
        count = count+1
print(count/len(combi))