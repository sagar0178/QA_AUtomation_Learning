class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Hello, customer you have")
            print(f"Deposited Rs{amount}. Current balance: Rs{self.balance}")
        else:
            print("Hello, customer")
            print("Invalid amount. Please deposit a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Hello, customer you")
                print(f"Withdrew Rs{amount}. Current balance: Rs{self.balance}")
            else:
                print("(Hello, customer you have")
                print("Insufficient funds.")
        else:
            print("(Hello, customer you entered")
            print("Invalid amount. Please withdraw a positive value.")

    def check_balance(self):
        print("Hello, customer your")
        print(f"Current balance is: Rs{self.balance}")


def get_float_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Hello, customer")
            print("Invalid input. Please enter a valid number.")


def authenticate_account():
    while True:
        try:
            print("Please enter your account number to access your bank account.")
            account_number = int(input("Account Number: "))

            if 1 <= account_number <= 99999:
                return str(account_number).zfill(5)
            else:
                print("Invalid account number. Account number must be between 00001 and 99999.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric account number.")


if __name__ == "__main__":
    account_number = authenticate_account()

    if account_number:
        print("Authentication successful. Welcome to your bank account!")
        account = BankAccount(account_number)

        while True:
            print("\nOptions:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Enter the option number: ")

            if choice == "4":
                print("Exiting the bank account program.")
                break

            if choice in ("1", "2", "3"):
                if choice == "1":
                    amount = get_float_input("Enter the amount to deposit: ")
                    account.deposit(amount)
                elif choice == "2":
                    amount = get_float_input("Enter the amount to withdraw: ")
                    account.withdraw(amount)
                elif choice == "3":
                    account.check_balance()
            else:
                print("Invalid choice. Please select a valid option.")
