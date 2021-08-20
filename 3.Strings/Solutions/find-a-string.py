string = str(input())
substring = str(input())
count = 0
for i in range(len(string)):
    if string[i:].startswith(substring):
        count +=1

print(count)