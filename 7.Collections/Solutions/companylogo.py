from collections import Counter
n = Counter(input())
for letter, value in n.most_common(3):
    print(letter, value)