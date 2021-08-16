def find_leap(year):
    a = "Leap Year"
    b = "Not a Leap Year"
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(a)
            else:
                print(b)
        else:
            print(a)
    else:
        print(b)


year = int(input())
find_leap(year)
print(find_leap)