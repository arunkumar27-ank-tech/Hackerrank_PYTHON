#in this problem, we will learn how to use centre function and join function

from string import ascii_lowercase as chars
n= int(input())
heap = [(('-'.join(chars[i:n])[::-1])+
        ('-'.join(chars[i:n])[1:])).center(4*n-3,'-')
        for i in range(n)]
#print(*heap[::-1],sep='\n')
print(*(heap[::-1])+heap[1:], sep='\n')