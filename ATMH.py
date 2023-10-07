class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: +{amount}')
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: -{amount}')
            return True
        else:
            return False

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance and recipient.user_id != self.user_id:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer to {recipient.user_id}: -{amount}')
            recipient.transaction_history.append(f'Transfer from {self.user_id}: +{amount}')
            return True
        else:
            return False

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self, accounts):
        self.accounts = accounts
        self.current_user = None

    def authenticate_user(self):
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")

        for account in self.accounts:
            if account.user_id == user_id and account.pin == pin:
                self.current_user = account
                return True

        return False

    def display_menu(self):
        while True:
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_transaction_history()
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                if self.current_user.withdraw(amount):
                    print(f"Withdrawal successful. Current balance: {self.current_user.balance}")
                else:
                    print("Withdrawal failed. Insufficient funds or invalid amount.")
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                if self.current_user.deposit(amount):
                    print(f"Deposit successful. Current balance: {self.current_user.balance}")
                else:
                    print("Deposit failed. Invalid amount.")
            elif choice == "4":
                recipient_id = input("Enter recipient's User ID: ")
                recipient = self.find_account_by_user_id(recipient_id)
                if recipient:
                    amount = float(input("Enter transfer amount: "))
                    if self.current_user.transfer(recipient, amount):
                        print(f"Transfer successful. Current balance: {self.current_user.balance}")
                    else:
                        print("Transfer failed. Invalid recipient, insufficient funds, or invalid amount.")
                else:
                    print("Recipient not found.")
            elif choice == "5":
                print("Thank you for using the ATM. Have a nice day!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.current_user.get_transaction_history():
            print(transaction)

    def find_account_by_user_id(self, user_id):
        for account in self.accounts:
            if account.user_id == user_id:
                return account
        return False


if __name__ == "__main__":
    # Create sample accounts
    accounts = [Account("12345", "1234", 1000), Account("54321", "4321", 500)]

    atm = ATM(accounts)

    while not atm.authenticate_user():
        print("Authentication failed. Please try again.")

    atm.display_menu()
