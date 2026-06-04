class ATM():
    def __init__(self):
        self.balance =0
        
    def display_menu(self):
        print("\n ATM Menu")
        print("1. credit")
        print("2. debit")
        print("3. Balance")
        print("4. Exit")
    
    def get_choice(self):
        return input("enter the choice from (1-4): ")
    
    def credit(self):
        amount = float(input("please enter the amount: "))
        if amount <= 0:
            print("Please enter the positive amount")
        else:
            self.balance += amount
            print(f"${amount} credited to your account")
    
    def debit(self):
        amount = float(input("enter the amount: "))
        if amount <= 0:
            print("please enter the positive amount")
        elif self.balance < amount:
            print("insufficient balance, please try again")
        else:
            self.balance -= amount
            print(f"${amount} debited from account")
    
    def show_balance(self):
        print(f"your current balance is: ${self.balance}")
        
    def run(self):
        while True:
            self.display_menu()
            choice = self.get_choice()
            
            if choice == '1':
                self.credit()
            elif choice == '2':
                self.debit()
            elif choice == '3':
                self.show_balance()
            elif choice == '4':
                print("thank you visit again...!")
                break
            else:
                print("Invalid choice. please try again")
                
atm = ATM()
atm.run()
