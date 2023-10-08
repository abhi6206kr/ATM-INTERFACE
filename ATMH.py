class Bank():
    def __init__(self, id, pin):
        self.id = id
        self.pin = pin
        self.balance = 0
        self.history = {}
        self.i = 1
        self.j = 1

    def Deposit(self, amount):
        self.balance += amount
        self.history["Deposit{}".format(self.j)] = amount
        self.j += 1

    def Withdraw(self, amount, pin):
        if pin == self.pin:
            if self.balance < amount:
                print("Your Available Balance Is", self.balance, "\nIs Less Than", amount)
            else:
                self.balance -= amount
                print("Withdraw Amount", amount, "\nRemaining amount is", self.balance)
                self.history["Withdraw{}".format(self.i)] = amount
                self.i += 1
        else:
            print("Enter Correct Pin")

    def his(self):
        print(self.history)

    def Check(self, pin):
        if pin == self.pin:
            print(self.balance)
        else:
            print("Enter Correct Pin")

id = input("Enter id:")
pin = int(input("Password:"))
b = Bank(id, pin)

while True:
    choice = int(input("Select:\n1 History\n2 Withdraw\n3 Deposit\n4 Check Balance\n0 to quit\nEnter Choice:"))
    if choice == 1:
        b.his()
    elif choice == 2:
        amount = int(input("Enter Amount to be Withdrawn:"))
        entered_pin = int(input("Enter Pin:"))
        b.Withdraw(amount, entered_pin)
    elif choice == 3:
        amount = int(input("Enter Amount to be Deposited:"))
        b.Deposit(amount)
    elif choice == 4:
        entered_pin = int(input("Enter Pin:"))
        b.Check(entered_pin)
    elif choice == 0:
        break
    else:
        print("Enter Valid Input (1, 2, 3, 4)")
