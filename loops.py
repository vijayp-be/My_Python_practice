'''
Exercise 1 Sum of Squares
Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a 
for loop.'''

# number = [1,2,3,4,5]
# sum = 0
# for i in number:
#     squre_number = i ** 2
#     print(f'the square of a number {i} is {squre_number}')
#     sum += squre_number
    
# print(f'the sum of squares of a numbers is {sum}')

'''Exercise 2 Countdown
Write a Python program that uses a 
while loop to print a countdown from 5 to 1'''

# num = 5
# while num >= 1:
#     print(num)
#     num -= 1
 
'''Exercise 3 Multiplication Table with Nested For Loop
Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop.'''

# table = int(input('enter the table: '))
# for i in range(1,11):
#     print(f'{table} * {i} = {table * i}')

# for i in table:
#     for j in range(1,11):
#         print(f'{i} * {j} = {i * j}')

'''Exercise 4 
Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive)'''

# sum = 0
# for i  in range(0,11,2):
#     sum += i
# print(f'sum of all even numbers for 1 to 10 is {sum}')
    
'''Exercise 5
Calculate the sum of all numbers from 1 to a given number
'''
# number = int(input('enter the number: '))
# sum = 0
# for i in range(1,number):
#     sum += i
# print('sum =', sum)

'''Exercise 6
Display numbers from a list using loop'''

# list1 = [1,2,3,4,5,6]

# for i in list1:
#     print(i)

'''Exercise 7
Display numbers from 10 to 1 using for loop
'''
# for i in range(-10,0):
#     print(i)
    
'''Exercise 8 
Write a program to display all prime numbers within a range'''

prime_list = []
num = int(input('enter the number: '))

for i in range(2, num+1):
    for j in range(2, num+1):
        if i % j == 0:
            break
    if i == j:
        prime_list.append(i)

print(f'prime numbers between 1 and {num} are: {prime_list}')
        

        

        







    

        