from collections import Counter
n = int(input())
words = [input().strip() for _ in range(n)]
count = Counter(words)
print(len(count))
print(*count.values())
print(count)