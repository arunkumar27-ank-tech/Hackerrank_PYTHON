import re

new = list()
for i in range(int(input())):
    code = input()
    pattern = r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=;|,|\))"
    s =re.findall(pattern,code)
    if s:
        new.extend(s)
for i in new:
    print(i)
