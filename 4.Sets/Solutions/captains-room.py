from collections import Counter
group = int(input())
rooms = list(map(int,input().split()))
d = Counter(rooms)
for key,value in d.items():
    if value == 1:
        print(key)
