import re
for _ in range(int(input())):
    string = input()
    m = re.match('^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$',string)
    if m:
        print("Valid")
    else:
        print("InValid")