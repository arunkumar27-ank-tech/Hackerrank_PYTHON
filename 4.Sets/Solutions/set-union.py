n = int(input())
set_eng = set(map(int, input().split()))
m = int(input())
set_fren = set(map(int,input().split()))
print(len(set_eng.union(set_fren)))