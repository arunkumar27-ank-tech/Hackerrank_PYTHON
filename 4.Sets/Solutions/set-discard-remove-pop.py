n = int(input())
sets = set(map(int, input().split()))
for _ in range(int(input())):
    eval('sets.{0}({1})'.format(*input().split()+[""]))
print(sum(sets))