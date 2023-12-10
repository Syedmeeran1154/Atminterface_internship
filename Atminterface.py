class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid amount for withdrawal or insufficient funds."

def main():
    atm = ATM()
    
    while True:
        print("\nATM Interface")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            balance = atm.check_balance()
            print(f"Your balance is ${balance}")
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: $"))
            message = atm.deposit(amount)
            print(message)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: $"))
            message = atm.withdraw(amount)
            print(message)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
