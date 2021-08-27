n = int(input())
students = {}
for _ in range(n):
    name, *line = input().split()
    score = list(map(float,line))
    students[name]=score
#print(students)
query_name = input()
sum = 0
for i in students[query_name]:
    sum+=i
    #print(sum)
print(sum/len(students[query_name]))