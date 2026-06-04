'''Reverse List:
Write Python code to reverse the order of elements in the given list 
Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]'''

# my_list = [10,20,30,40,50,11]
# my_list.reverse()
# print(my_list)

# print(my_list[::-1])

'''Common Elements:
Given two lists 
them.
list1 and 
list2 , find and print the common elements between 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]'''

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common = []

# for i in list1:
#     for j in list2:
#         if i == j:
#             common.append(i)
# print(common)

#           or

# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)


'''Unique Elements:
Create a new list 
unique_list containing only the unique elements from the 
given list 
original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]'''

# original_list = [1, 2, 2, 3, 4, 4, 5]
# empty_list = []

# for i in original_list:
#     if i not in empty_list:
#         empty_list.append(i)
# print(empty_list)

'''Remove Duplicates:
Remove duplicate elements from the given list 
without duplicates while preserving the order.
duplicated_list and print the list '''

duplicated_list = [1, 2, 2, 3, 4, 4, 5]

# set_convert = set(duplicated_list)
# remove_dup = list(set_convert)
# print(remove_dup)
#               or
# remove_dup = []
# for i in duplicated_list:
#     if i not in remove_dup:
#         remove_dup.append(i)
# print(remove_dup)


'''Exercise 1 List Concatenation
Write a Python script that concatenates two lists and prints the result.
'''

# list1 = [1, 2, 3, 4, 5]
# list2 = [ 6, 7, 8]

# print(list1 + list2)

'''Exercise 2 List Repetition
Write a Python script that repeats a list three times and prints the result.
'''
# list1 = [1, 2, 3, 4, 5]

# print(list1 * 3)

'''Exercise 3 List Removal
Write a Python script that removes the elements at even indices from a list.
'''

# list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in list1:
#     if  i%2 == 0:
#         list1.remove(i)
# print(list1)



        