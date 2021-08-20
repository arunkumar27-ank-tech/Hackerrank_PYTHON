for _ in range(int(input())):
    n,nos =int(input()), list(map(int,input().split()))
    if (sorted(nos)[-1]==sorted(nos[0])) or (sorted(nos[-1]==[-1])):
        print("Yes")
    else:
        print("No")
    
       

#lst1 = [2,3,4,5]
##lst2=[4,5,2,3]
#if (lst1==sorted(lst2)):
 #   print("yes")
#else:
 #   print("No")