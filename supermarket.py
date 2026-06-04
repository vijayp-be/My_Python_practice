name = input("enter your Name: ")

lists = '''
Rice    Rs 10/kg
Sugar   Rs 8/kg
Oil     Rs 30/ltr
Salt    Rs 25/kg
Paneer  Rs 40/kg
Maggie  Rs 12/kg
Boost   Rs 200/bottle'''

#Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

#rate for each item

items = {'rice': 10, 'sugar': 8, 'oil': 30, 'salt':25, 'paneer': 40, 'maggie': 12, 'boost': 200}

while True:
    option = input("press 1 for lists or 2 to exit: ")
    if option == '2':
        print("thank you for shopping..")
        break
    elif option == '1':
        print(lists)
        
        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("thank you for shopping..")
                break
            elif inp1 =='1':
                item = input("choose your item: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():    #check if input is a digit
                        quantity = int(quantity_input)
                        break
                    else:
                        print("please enter the valid quantity..")
                
                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("selected item is not available. sorry for the inconvenience..")
                    
        if totalprice > 0:
            tax = (totalprice * 12)/100
            finalamount = tax + totalprice
            
            print(25 * "=", "supermarket", 25 * "=")
            print(28 * " ", "Bangalore")
            print("Name: ", name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'item', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
                                        
            
        