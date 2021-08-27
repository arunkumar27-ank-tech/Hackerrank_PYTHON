#hereweusesortedfunctionkeyattribute,tosaysortingshouldbedoneonwhichbasis
import operator

def decoratorfunc(f):
    def inner(people):
        return (map(f,sorted(people,key=lambda x: int(x[2]))))
    return inner


@decoratorfunc
def nameformat(person):
    return("Mr. " if person[3]=="M" else "Ms. ") + person[0]+ " " + person[1]


people = [input().split()for _ in range(int(input()))]
print(*nameformat(people),sep='\n')