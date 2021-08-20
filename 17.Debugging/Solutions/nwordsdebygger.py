class Evenstream(object):#8
    def __init__(self):
        self.current = 0 #evenfunctionprintshouldstartfrom0, so 0 is given
    def get_next(self):
        return_value = self.current
        self.current += 2
        return return_value


class Oddstream(object): #8a
    def __init__(self):
        self.current =1  #oddfunctionprintshouldstartfrom0, so 1 is given
    def get_next(self):
        return_value = self.current
        self.current += 2
        return return_value


def print_from_stream(n,stream=Evenstream()):#7 #7b now_streamvalueisOddstreambecause the argument is given
    stream.__init__()#9

    for _ in range(n):#10
        print(stream.get_next())


queries = int(input()) #1
for i in range(queries): #2
    command, n = input().split() #3
    n = int(n)#4
    if command == "even":#5
        print_from_stream(n)#6
    else:#5b
        print_from_stream(n,Oddstream())#6b