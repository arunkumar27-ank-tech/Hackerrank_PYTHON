import re
consonants = '[qwrtypsdfghjklzxcvbnm]'
a=re.findall(r'(?<='+consonants+')([aeiou]{2,})'+consonants,input(),re.I)
print('\n'.join((a or ['-1'])))
#print(re.findall(r'[a,e,i,o,u,A,E,I,O,U]',string))
#in this problem, we applied lookbehind method(?<=) and re.I flag(re.I)