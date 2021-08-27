import re
for _ in range(int(input())):
    string = str(input())
    print(re.sub('(?<=\s)(&&|\|\|)(?=\s)', lambda i:'and' if i.group(1)=="&&" else "or",string))

#(?<=)->lookbehind_syntax
#\s->matches_white_space
#&&->andsymbol
#1st_pip |-> defines alter or lookfor other
#\|\|-> cancelthe special meaning of pipe, as we know \ is an escape character