n, m = int(input()), list(map(int, input().split()))
print(all([True if x>0 else False for x in m]) and any([str(x)==str(x)[::-1] for x in m]))