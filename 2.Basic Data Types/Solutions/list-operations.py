n = int(input())
a=[]
for _ in range(n):
    func = input().split()
    if (func[0]=='insert'):
        pos = int(func[1])
        ele = int(func[2])
        a.insert(pos,ele)
    elif (func[0]=='append'):
        a.append(int(func[1]))
    elif (func[0]=='remove'):
        a.remove(int(func[1]))
    elif (func[0]=="print"):
           print(a)
    elif (func[0]=="sort"):
            a.sort()
    elif (func[0]=="pop"):
            a.pop()
    elif (func[0]=="reverse"):
            a.reverse()