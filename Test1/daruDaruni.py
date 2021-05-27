class User:
    username = []
    password = []
    balance = []
    transaction = []

    def validate(self, username, password):
        login = False
        for i in range(len(self.username)):
            if self.username[i] == username and self.password[i] == password:
                login = True
                break
            else:
                login = False

        if login:
            return "Login Success"
        else:
            return "Login Error"

    def register(self, username, password):
        self.username.append(username)
        self.password.append(password)
        self.balance.append(0)
        self.transaction.append([])

    def printUserTransaction(self, username):
        for i in range(len(self.transaction)):
            if self.username[i] == username:
                if len(self.transaction[i]) > 0:
                    no = 1
                    print("List of Transaction : ")
                    for trans in self.transaction[i]:
                        print("{}. {}".format(no, trans))
                        no += 1
                else:
                    print("There is no transaction")

    def printUserBalance(self, parameter):
        if len(self.username) > 0:
            print("List of User :")
            no = 1
            if parameter == 0:
                for i in range(len(self.username)):
                    print("{}. {}, Balance = {}".format(no, self.username[i], self.balance[i]))
                    no += 1
            else:
                for i in range(len(self.username)):
                    print("{}. {}".format(no, self.username[i]))
                    no += 1
        else:
            print("There is no registered user")


class ATM(User):

    def deposit(self, deposit, username, parameter):
        for i in range(len(self.username)):
            if self.username[i] == username:
                self.balance[i] += deposit
                self.transaction[i].append("Deposit = {}".format(deposit))
                if parameter == 0:
                    print("Your current balance is {}".format(self.balance[i]))

    def withdraw(self, withdraw, username, parameter):
        for i in range(len(self.username)):
            if self.username[i] == username:
                if self.balance[i] - withdraw < 0:
                    print("Your balance is insufficient ")
                else:
                    self.balance[i] -= withdraw
                    if parameter == 1:
                        self.transaction[i].append("Transfer = {}".format(withdraw))
                    else:
                        self.transaction[i].append("Withdraw = {}".format(withdraw))
                    print("Your current balance is {}".format(self.balance[i]))

    def checkBalance(self, username):
        for i in range(len(self.username)):
            if self.username[i] == username:
                print("Your current balance is {}".format(self.balance[i]))

    def fundTransfer(self, username, recipient, transferredMoney, parameter):
        find = False
        for i in range(len(self.username)):
            if recipient == self.username[i]:
                find = True
                break
            else:
                find = False
        if find:
            for i in range(len(self.username)):
                if self.username[i] == username:
                    if self.balance[i] - transferredMoney < 0:
                        print("Your balance is insufficient ")
                    else:
                        self.withdraw(transferredMoney, username, parameter)
                        self.deposit(transferredMoney, recipient, parameter)
        else:
            print("There is no username name as {}".format(recipient))


user = User()
account = ATM()
username = ""
password = ""
while True:
    choose = int(input("1. Register\n2. Login\n3. All User and Balance\n4. Exit\nChoose : "))
    if choose != 3 and choose != 4:
        username = input("Enter your Username : ")
        password = input("Enter your Password : ")
    if choose == 1:
        user.register(username, password)
    elif choose == 2:
        callback = user.validate(username, password)
        if callback == "Login Success":
            print("\n{}. Welcome {}".format(callback, username))
            while True:
                choose2 = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Fund Transfer\n5. All "
                                    "Transaction\n6. Exit\nChoose : "))
                if choose2 == 1:
                    deposit = float(input("Enter your deposit amount: "))
                    account.deposit(deposit, username, 0)
                elif choose2 == 2:
                    withdraw = float(input("Enter your withdraw amount: "))
                    account.withdraw(withdraw, username, 0)
                elif choose2 == 3:
                    account.checkBalance(username)
                elif choose2 == 4:
                    account.printUserBalance(1)
                    recipient = input("Enter Recepient Username: ")
                    transferredMoney = float(input("Enter the money amount: "))
                    account.fundTransfer(username, recipient, transferredMoney, 1)
                    pass
                elif choose2 == 5:
                    account.printUserTransaction(username)
                elif choose2 == 6:
                    break

                again = input("\nAnother transaction? ")

                if again == "n":
                    break
                else:
                    print("")
        else:
            print("{}. Please Try Again".format(callback))
    elif choose == 3:
        account.printUserBalance(0)
    elif choose == 4:
        print("Thank You!")
        break
    print("")
