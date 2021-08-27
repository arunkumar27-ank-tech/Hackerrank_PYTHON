cube = lambda x: x**3   
def fibonacci(n):
    if n>2:
        l = []
        l.append(0)
        l.append(1)
        for _ in range(n-2):
            l.append(l[-2]+l[-1])
        return l
    else:
        l =[]
        for i in range(n):
            l.append(i)
        return l

n = int(input())
print(list(map(cube,fibonacci(n))))