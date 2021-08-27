import re
integer_range = r'[1-9][0-9]{5}'
repititive_integer = r'(\d)(?=.\1)'
for _ in range(int(input())):
    postalcode = input()
    print(bool(re.match(integer_range,postalcode)) and len(re.findall(repititive_integer,postalcode))<2)