n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
print('second_maximum',sorted(set(a),reverse=True)[1])
#print('second_maximum',sorted(set(a))[-2])