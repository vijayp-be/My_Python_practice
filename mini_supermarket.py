'''Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items
Sample Input:
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]

'''

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]

Total = float(0)
print("items\t\t price")
print("_"*25)

for iteam,price in items:
    print(iteam, "\t\t", float(price))
    Total += price
print("_"*25)
print("Total", "\t\t", Total)

        
