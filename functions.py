'''Task 1: Add Function
Write a Python function named add that takes two arguments a and 
b and returns their sum.
'''
# def add(a, b):
#     return a + b

# obj = add(10, 20)
# print(obj)

'''Square of a Function
Write a Python function named square that takes a number x as input and returns its square.'''

# def square(x):
#     x = x ** 2
#     return x

# num = int(input("Enter a number: "))
# print(square(num))

'''
Write a Python function named 'factorial' that takes a positive integer n as input and 
returns its factorial'''

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result
# num = int(input("Enter a number: "))
# print(factorial(num))

'''Task 4: Maximum Function
Write a Python function named maximum that takes a list of numbers as input and 
returns the maximum value in the list.'''

# def maximum(numbers):
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(maximum([1,2,25,4,5]))
      
'''Task 5: Reverse Function
Write a Python function named reverse that takes a string s as input and 
returns its reverse'''

# def reverse(x):
#     return x[::-1]
# print(reverse("vijay"))

# def reverse(s):
#     reverse_string = ""
#     for char in s:
#         reverse_string = char + reverse_string
#     return reverse_string
# print(reverse("vijay"))

'''Check Prime Function
Write a Python function named is_prime that takes a positive integer n as input 
and returns True if n is prime, otherwise False'''

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))

# if is_prime(num) == True:
#     print(num, "is a prime no")
# else:
#     print(num, "is not a prime no")
   
''' Fibonacci Function
Write a Python function named fibonacci that takes a positive integer 
n as input and returns the nth Fibonacci number'''

'''palindrome'''

# def is_palindrome(s):
#     palin_text = ""
#     for char in s:
#         palin_text = char + palin_text
        
#     if s == palin_text:
#         return True
#     else:
#         return False

# word = input("enter a word: ")
# if is_palindrome(word) == True:
#     print(word, "is a palindrome")
# else: 
#     print(word, "is not a palindrome")
    
'''Sum of Squares Function
Write a Python function named sum_of_squares that takes a list of numbers as 
input and returns the sum of the squares of those numbers.'''

# def sum_of_squares(x):
#     sum =0
#     for i in x:
#         square = i ** 2
#         sum += square
#     return sum
# print(sum_of_squares([1,2,3,4,5]))

'''
Write a Python function named averave that takes a list of numbers as input and 
returns the average value. '''

# def average(x):
#     sum =0
#     for i in x:
#         sum += i
#     average = sum/len(x)
#     return average
# print(average([1,2,3,4,5]))

