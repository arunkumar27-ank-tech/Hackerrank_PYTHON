import re
for _ in range(int(input())):
    print(bool(re.search('^[-+.]?[0-9]+\.?[0-9]+$',input())))