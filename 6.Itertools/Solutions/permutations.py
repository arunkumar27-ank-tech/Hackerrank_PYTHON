from itertools import permutations
stdin,k=input().split()
a=list(permutations(stdin,int(k)))
a.sort()
for i in a:
    print(''.join(i)) #join_Function_willbreak_the_list_into_strings