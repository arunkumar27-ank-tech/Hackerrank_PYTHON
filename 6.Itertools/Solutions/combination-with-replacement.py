from itertools import combinations_with_replacement
word , n = input().split()
for j in combinations_with_replacement(sorted(word),int(n)):
    print(''.join(j))
