import re
import email.utils
for _ in range(int(input())):
    name,email = input().split(' ')
    s= re.match('<[a-zA-Z][\w|\.|_|-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>',email)
    if s:
        print(name,email)