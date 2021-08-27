import re
for _ in range(int(input())):
    print(bool(re.match('[789]\d{9}',input())))