
#lambda arguments:expression
#filter(function,iterables)
#map(function, iterable, ...)
'''filter list of even numbers in the given list'''

# list1 = [1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x%2 == 0
# obj = filter(even,list1)
# print(list(obj))

#using filter function functions..

# list1 = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda i:i%2==0, list1)
# print(list(result))

#more less code

# result =filter(lambda i:i%2==0, [1,2,3,4,5,6,7,8,9,10])
# print(list(result))

'''print squares of list of elements'''

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [11,12,13,14,15,16,17,18,19,20]
# def squres(x):
#     return x**2
# result = map(squres, list1)
# print(list(result))

                        # or

# result = map(lambda i:i**2, list1)
# print(list(result))

                        # or

# result = map(lambda i:i**2, [1,2,3,4,5,6,7,8,9,10])
# print(list(result))

                    #multiple iterables
# result = map(lambda i,j:(i**2,j**2), list1, list2)
# print(list(result))


                    #reduce function

# from functools import reduce

# result = reduce(lambda a,b:a+b, [1,2,3,4,5])
# print(result)

                    # generator function
                    
# def sample():
#     yield 1
#     yield 2
#     yield 3
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

'''
Write a Python function 
square_all(numbers) that takes a list of numbers as 
input and returns a new list containing the square of each number in the 
input list. Use the map() function with a lambda function to implement this'''

# list1 = [1,2,3,4,5]

# def squre_all(i):
#     return map(lambda i:i**2, list1)
# print(list(squre_all(list1)))

                # other approach
# result = map(lambda i:i**2, [1,2,3,4,5])
# print(list(result))
                

'''
Write a Python function filter_positive(numbers) that takes a list of numbers 
as input and returns a new list containing only the positive numbers from the input list. Use the
fliter() function with a lambda function to implement this'''

# numbers = [1,2,-1,-3,4,5,-7,-8]

# def filter_positive(numbers):
#     return filter(lambda i:i>0, numbers)
# print(list(filter_positive(numbers)))

'''Write a Python function calculate_factorial(n) that calculates the factorial of 
a given number n. Use the reduce() function with an appropriate lambda 
function to implement this.'''


                        #  regular method to calculate factorial 
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
# print(cal_fact(5))

                            # with reduce function
# from functools import reduce

# def calculate_factorial(n):
#     return reduce(lambda x,y:x*y, range(1,n+1))
# print(calculate_factorial(5))

'''
Write a Python function count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the 
reduce() function with an appropriate lambda function to implement this'''

from functools import reduce
def count_vowels(name):
    vowels = 'aeiouAEIOU'
    return reduce(lambda count, char: count + (1 if char in vowels else 0), )
