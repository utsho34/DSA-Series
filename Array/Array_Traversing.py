#create an array
#array size dynamic
#user input

###regular method
size = int(input('Enter the size of the array: '))
array = []
for i in range(size):
    l=input()
    array.append(l)
print(array)

###using builtin functions
elements= int(input("Enter the number of the elements of the array: "))
arr = list(map(int,input('Enter the elements: ').strip().split()))
print(arr)

###strip() - this method work like a space cleaner both in start and end part.
###split() - this method work for converting a string to a list/array

#question-1: Find duplicate elements in a list and remove it from the list and print the list of distinct elements and removed elements
q1_array= [5,3,665,67,44,88,77,66,88,4,5,6,7,8,9,8,7,6,5,43,3,4677,56,66,4677,9,9,9,9,9,9]
duplicate_array = []
distinct_array = []
for i in q1_array:
    if i in q1_array:
        distinct_array.append(i)
    elif i not in q1_array:
        duplicate_array.append(i)
print('Duplicate Elements Array',duplicate_array)
print('Distinct Array',distinct_array)
#complexity- O(n^2)
###optimize approach
distinct_array_op = []
duplicate_array_op = []

seen = set()
for i in q1_array:
    if i not in seen:
        distinct_array_op.append(i)
        seen.add(i)
    else:
        duplicate_array_op.append(i)
#complexity after using set is O(n)




