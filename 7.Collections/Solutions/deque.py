from collections import deque
d =deque()
for _ in range(int(input())):
    k = input().split()
    eval(f"d.{k[0]}({k[1]})") if len(k)==2 else eval(f"d.{k[0]}()")
print(*d)