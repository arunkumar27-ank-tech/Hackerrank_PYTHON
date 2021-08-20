from collections import Counter
n = int(input())
shoesizes = Counter(map(int,input().split()))
print(shoesizes)
customer = int(input())
total_revenue = 0
for _ in range(customer):
    shoesize, price = map(int, input().split())
    if shoesizes[shoesize]:
        total_revenue+=price
        shoesizes[shoesize]-=1
print(total_revenue)