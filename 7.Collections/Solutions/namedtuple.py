from collections import namedtuple
from typing import TextIO
no_student = int(input())
col = input()
Student = namedtuple('Student',col)
Total =0
for _ in range(no_student):
    student = Student(*input().split())
    Total += int(student.MARKS)
print(Total/no_student)
