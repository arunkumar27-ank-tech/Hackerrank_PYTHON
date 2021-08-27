for _ in range(int(input())):
    n,lst =int(input()), list(map(int,input().split()))
    if (sorted(lst)[-1]==lst[0]) or (sorted(lst)[-1]==lst[-1]):
        print("Yes")
    else:
        print("No")
    
       

#lst1 = [2,3,4,5]
##lst2=[4,5,2,3]
#if (lst1==sorted(lst2)):
 #   print("yes")
#else:
 #   print("No")