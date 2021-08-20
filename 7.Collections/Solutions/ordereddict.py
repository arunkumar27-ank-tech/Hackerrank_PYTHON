from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(maxsplit=1)
    d[item] = d.get(item, 0) + int(price)

for item, price in d.items():
    print(item, price)