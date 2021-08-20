def merge_the_tool(string,n):
    factor = len(string)//n
    for i in range(factor):
        s = string[i*n:i*n+n]
        st=''
        for j in range(len(s)):
            if s[0:j+1].count(s[j])>1:
                st=st
            else:
                st=st+s[j]
        print(st)


string, n = input(), int(input())
merge_the_tool(string,n)