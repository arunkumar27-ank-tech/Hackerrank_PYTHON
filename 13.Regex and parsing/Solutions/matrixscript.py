import re
n,m = list(map(int,input().split()))
matrix = []
res = ''
for i in range(n):
    script = input()
    matrix.append(script)
print(matrix)
for item in zip(*matrix):
    res += ''.join(item)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", res))