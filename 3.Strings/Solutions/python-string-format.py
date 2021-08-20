n = int(input())
x=len(bin(n)[2:])
for i in range(1,n+1):
    #print(str(i),bin(i)[2:],oct(i)[2:],hex(i)[2:].upper())
    print(str(i).rjust(x,' '),bin(i)[2:].rjust(x,' '), oct(i)[2:].rjust(x,' '), hex(i)[2:].upper().rjust(x,' '))
