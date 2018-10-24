#Description: Create 2 types of accounts: Currents and Savings.
#Both will inherit from the Account Parent Class.
#- Each Account can deposit and withdraw money and print statements
#- Each account will have different minimim limits: Current will have
#overdraft of $1000. Savings won't have any overdraft.

#1)Create Abstract Parent Class. Will need a constructor.
#Will take name of account holder, balance, and minimum balance of account

#Constructor General Accounts method:
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #Deposit Method
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    #Withdraw Method
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Sorry. not enough funds!")
            
    #Statement Method:
    def statement(self):
        print("Account Balance: ${}".format(self.balance))


#Create Current account Class
class Current(Account): #class "Current" and inherits from "Account".
    def __init__(self, name, balance): #Contructor. These are parameters someone must enter to create acct
        #we need to pass this data (self, name, balance) up to "Account".
        super().__init__(name, balance, min_balance = - 1000)
        #super method and init function.

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)


        
#Create Savings account class
class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account: Balance ${}".format(self.name, self.balance)
