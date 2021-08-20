n = int(input())
sets = set(map(int,input().split()))
for _ in range(int(input())):
    operation = input().split()[0]
    b = set(input().split())
    eval(f'sets.{operation}({b})')
print(sum(list(map(int,sets))))