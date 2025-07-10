class Bank:
    def __init__(self,account_holder,balance,pin):
        self.account_holder=account_holder
        self.__balance=balance
        self.__pin=pin
    def get_balance(self,pin):
        if self.__pin==pin:
            print("Balance available is::",self.__balance)
        else:
            print("Invalid pin")
    def deposite(self,amount,pin):
        if self.__pin==pin and amount>0:
            self.__balance+=amount
            print("Sucess")
            print("Balance available is::",self.__balance)
        else:
            print("Invalid Pin or Amount")
    def withdraw(self,amount,pin):
        if self.__pin==pin and amount>0:
            self.__balance-=amount
            print("Sucess to withdraw")
            print("Balance available is::",self.__balance)
        else:
            print("Invalid Pin or Amount")
    def change_pin(self,old_pin,new_pin):
        if self.__pin==old_pin:
            self.__pin=new_pin
            print("Pin set is sucess")
        else:
            print("Invalid old pin is wrong")
b=Bank("veeranna",1000,1001)
b.get_balance(1001)
b.withdraw(120,1001)            
b.deposite(1200,1001)
b.change_pin(1001,1009)
b.withdraw(1000,1009)
b.get_balance(1009)            
            
