from itertools import combinations
word , n = input().split()
for i in range (1,int(n)+1):
    for j in (sorted(combinations(word,i))):
        print(''.join(j))
