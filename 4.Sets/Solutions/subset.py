for _ in range(int(input())):
    x,a,y,b = int(input()),set(map(int,input().split())),int(input()),set(map(int,input().split()))
    print(a.issubset(b))