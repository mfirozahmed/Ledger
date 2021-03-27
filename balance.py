from Database.commands import *


class Balance:

    def __init__(self, database):
        result = getBalanceSQL(database)
        self.balance = result[3]



    def getBalance(self):
        return self.balance
    


    def addBalance(self, value, database):
        self.balance += value
        addBalanceSQL(self.balance, value, database)



    def reduceBalance(self, value, database):
        self.balance -= value
        reduceBalanceSQL(self.balance, -value, database)
    


    def showBalance(self):
        balance = self.getBalance()
        print("Current Balance: {}".format(balance))