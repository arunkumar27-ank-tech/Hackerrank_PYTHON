import re

s = re.search(r'([a-zA-Z0-9])\1', input())
print(s.group(1) if s else -1)
#s = re.search(r'(?P<one>\w+),(?P=one)',input())
#print(s.group('one') if s else -1)