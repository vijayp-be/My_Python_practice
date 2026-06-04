
'''Vowel Checker:
Write a Python program that takes a character as input and checks whether 
it is a vowel or not. Use the 
if-else statement.'''

# vowel_check = input('enter the character to check: ')

# if vowel_check in "aeiouAEIOU":
#     print(f"the character '{vowel_check}' is vowels")
# else:
#     print(f"the character '{vowel_check}' is not a vowel")
    

'''Age Group Classification
Write a program that takes an age as input and classifies the person into 
one of the following age groups:
1. Child: 0-12 years
2. Teenager: 13-17 years
3. Adult: 18-64 years
4. Senior: 65 years and older'''

# age = int(input("enter age of a person: "))

# if age > 0 and age <= 12:
#     print(" the perso is a child")
# elif age >= 13 and age <= 17:
#     print('the person is Teenager')
# elif age >= 18 and age <= 64:
#     print('the person is an Adult')
# elif age >= 65:
#     print('the preson is senior')
# else:
#     print('enter a valid age')

''' Leap Year Checker:
Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400.
'''
# check_leap = int(input('enter year to check: '))

# if (check_leap % 4) == 0 :
#     if (check_leap % 100) != 0:
#         print(f"the year {check_leap} is a leap year")
#     elif (check_leap % 400 == 0):
#         print(f"the year {check_leap} is a leap year")
#     else:
#         print(f"the year {check_leap} is not a leap year")
# else:
#     print(f"the year {check_leap} is not a leap year")
    
''' second approch'''

# check_leap = int(input('enter year to check: '))

# if (check_leap % 4 == 0 and check_leap % 100 != 0 ) or (check_leap % 400 == 0):
#     print(f"the year {check_leap} is a leap year")
# else:
#     print(f"the year {check_leap} is not a leap year")

'''Calculator:
Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation.'''

# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))
# operator = input('enter the operator (+, -, *, /): ')

# if operator == "+":
#     print(f"the addition of {num1} and {num2} is {num1 + num2} ")
# elif operator == '-':
#     print(f"the subraction of {num1} and {num2} is {num1 - num2} ")
# elif operator == '*':
#     print(f"the multiple of {num1} and {num2} is {num1 * num2} ")
# elif operator == '/':
#     print(f"the division of {num1} and {num2} is {num1 / num2} ")
    
# else:
#     print('please check the numbers and the operators and try again')
    

'''
Rewrite the following code using the short-hand 
if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
'''
# x = int(input('enter the number: '))

# print("the number is even" if x%2 == 0 else "the number is odd")

'''Discount Calculator:
Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input.'''

# original_price = int(input('enter the price: '))
# discount = int(input("enter the discount percentage"))

# discount_price = original_price * (discount/100)
# final_price = original_price - discount_price
# ##original_price -= discount_price

# print(f"the orighinal price is {original_price} and the discount if {discount}% is applied and final price after discount is {final_price}")

''' BMI Calculator:
Write a program that calculates the Body Mass Index BMI using the 
formula: BMI  weight (kg) / (height (m))^2. The program should take 
weight and height as input.'''

weight = float(input('enter the weight: '))
height = float(input('enter the height: '))

BMI = weight / (height)**2

print(f'the BMI for the weight {weight} and height {height} is {BMI}')
