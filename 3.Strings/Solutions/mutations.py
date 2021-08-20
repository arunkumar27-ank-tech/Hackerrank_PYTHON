#stringsareimmutableobjecy, we cannot modify string values. so, modify a string , 1st we convert the string into list
#thus, list are mutable, we add the changes and converting the list into normal string by usnig join function
string = "abcdefghij"
print(string)
lst = list(string)
lst[5]='m'
string = ''.join(lst)
print(string)
#string[5]='m'
#print(string)
