#hash() function only work in tuples in otherwords, which are immutable
#hash() function works only on immutable objects, hash(function doesnt work in list
#n=int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))