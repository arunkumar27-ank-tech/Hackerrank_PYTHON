import re
from typing import Pattern

def fun(s):
    pattern = re.compile('^([a-zA-Z0-9-_])+@([a-zA-Z0-9])+\.([a-zA-Z]){,3}$')
    return re.match(pattern,s)

def filter_email(email):
    return list(filter(fun,email))

email = []
for _ in range(int(input())):
    email.append(input())

filtered_emails = filter_email(email)
filtered_emails.sort()
print(filtered_emails)