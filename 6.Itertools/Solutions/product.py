#as in the name itertools, this concepts will be useful in iterating process
#product function is equivalent nested for loop function, this function will reduce the lines of code
from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*product(a,b))