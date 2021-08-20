#a = set(map(int, input().split()))
#b=set()
#for _ in range(int(input())):
 #   b.update(set(map(int, input().split())))
#print(a.issuperset(b))
a = set(input().split())
print(all(a> set(input().split()) for _ in range(int(input()))))