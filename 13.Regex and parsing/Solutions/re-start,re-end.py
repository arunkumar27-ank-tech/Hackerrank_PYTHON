import re
string = input()
pattern = input()
m = list(re.finditer('(?=(%s))'%pattern,string))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))