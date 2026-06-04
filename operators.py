'''arithematic operations'''
# a = 10
# b = 3

# addition = a + b
# sub = a - b
# multiple = a * b
# division = a / b
# exponential = a ** b #(a power b)
# modules = a % b #(remainder)
# floor_devision = a // b 

# print (addition, sub, multiple, division, exponential, modules, floor_devision)


'''Compound Assignment operations'''
# num_1 = 10
# num_1 += 5  #num_1 = num_1 + 5
# print(num_1)

# num_1 *= 2
# print(num_1)


'''Comparision operators''' #(returns boolean)

# product_cost = 10
# product_cost2 = 20

# print(product_cost == product_cost2)
# print(product_cost > product_cost2)
# print(product_cost < product_cost2)
# print(product_cost >= product_cost2)
# print(product_cost >= product_cost2)
# print(product_cost != product_cost2)


'''Logical Operators'''

# user = 'vijay'
# password = 1234
# otp = 12345

# print(user == 'vijay' and password == 1234 and otp == 12345)
# print(user == 'vijay' or password == 1234 or otp == 12345)

# sample = True
# print(not(sample))


'''Identity operators''' #checks if memory is same

# list1 = [1,2,3]
# a = list1
# list2 = [1,2,3]

# print(list1 is a)
# print(list1 is a)
# print(list1 is not list2)
# print(list1 is list2)

'''Membership Operators'''  

# fruits = ['apple', 'banana', 'orange']
# print('orange' in fruits)
# print('orange' not in fruits)


# product_cost = 1000
# discount = 5
# result = product_cost * (discount / 100)
# product_cost -= result
# print(f"discount giver {discount}% and final discount {result} and total cost after discount is {product_cost}")


'''write a program to calculate simple interest in years'''

principle_amt = int(input('enter the principle amount: '))
rate = int(input('enter the rate: '))
time = int(input('enter the time in years: '))

simple_interest = (principle_amt * time * rate) / 100

print(f'the simple interest for principle amount {principle_amt} with rate of interest {rate} for {time} years is {simple_interest}')



100         >    2
1000        >    20
10000       >    200
100000      >    20000
400000      >    80000

1 year = 96000
3 years = 288000

96000 