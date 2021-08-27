def wrapper(func):
    def fun(l):
        func(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_ph(l):
    print(*sorted(l),sep='\n')

l = [input() for _ in range(int(input()))]
sort_ph(l)
print(sort_ph.__name__)