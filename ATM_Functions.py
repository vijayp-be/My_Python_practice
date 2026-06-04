balance =0

def display_menu():
    print("\n ATM Menu")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

def get_choice():
    return input("Enter your choice (1-4): ")

def credit():
    global balance
    amount = float(input("enter the amount to credit: "))
    if amount <= 0:
        print("please enter positive amount")
    else:
        balance += amount
        print(f"${amount} credited to your account")

def debit():
    global balance
    amount = float(input("enter the amount to debit: "))
    if amount <= 0:
        print("please enter positive numbers..")
    elif amount > balance:
        print("insufficient balance..")
    else:
        balance -= amount
        print(f"${amount} debited from you account")
def show_balance():
    print(f"your current balance is : ${balance}")
    
def main():
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            show_balance()
        elif choice =='4':
            print("thank you for using ATM.. Goodbye!")
            break
        else:
            print("Invalid choice, please try again")
            
main()
