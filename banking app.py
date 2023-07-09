class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def withdraw(self, w_amount):
        if self.amount >= w_amount:
            self.amount -= w_amount
        else:
            print("Insufficient balance. Transaction failed.")

    def deposit(self, d_amount):
        self.amount += d_amount


def create_account():
    name = input("Enter your full name: ")
    number = int(input("Enter a valid mobile number: "))
    address = input("Enter the address: ")
    account_type = input("Enter the type of account you require [e.g., Savings(SA), Current(CA), Fixed(FA)]: ")
    amount = float(input("Enter the initial amount that you want to deposit: "))
    return name, number, address, BankAccount(account_type, amount)


def login():
    accounts = {}  # to store name of account
    while True:
        choice = int(input("Press 1 for Login\nPress 2 for Creating a new account\n"))
        if choice == 1:
            user_name = input("Enter your User Name: ")
            if user_name in accounts:
                number, address, account = accounts[user_name]
                print(f"Welcome, {user_name}!")
                while True:
                    c = int(input("1. Balance\n2. Withdraw\n3. Deposit\n4. Account Details\n5. Logout\n"))
                    if c == 1:
                        print("Your Account Balance Is:", account.amount)
                    elif c == 2:
                        h = float(input("Enter the amount to be withdrawn: "))
                        account.withdraw(h)
                        print("Transaction completed. Your Current Balance Is:", account.amount)
                    elif c == 3:
                        e = float(input("Enter the amount to be deposited: "))
                        account.deposit(e)
                        print("Transaction completed. Your Current Balance Is:", account.amount)
                    elif c == 4:
                        print("Account Details:")
                        print(f"Name: {user_name}")
                        print(f"Account Type: {account.account_type}")
                        print(f"Amount: {account.amount}")
                    elif c == 5:
                        break
                    else:
                        print("Invalid Input")
            else:
                print("Account Not Found")
        elif choice == 2:
            name, number, address, q = create_account()
            accounts[name] = (number, address, q)
            print("Your Account Is Created Successfully")
        else:
            print("Invalid option")


login()
