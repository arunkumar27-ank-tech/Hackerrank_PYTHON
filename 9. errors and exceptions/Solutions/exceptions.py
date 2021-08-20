for _ in range(int(input())):
    
    try:
        a,b =int(input()), int(input())
        print(a//b)
    except ZeroDivisionError as e:
        print("ERRORCODE", e)
    except ValueError as v:
        print("ERRORCODE", v)