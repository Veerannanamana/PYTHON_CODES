class bank:
    def __init__(self,balance,aco_name):
        self.__balance=balance
        self.aco_name=aco_name
    def gets(self):
        print(self.__balance)
    def withdraw(self,amount):
        if self.__balance>=amount:
            x=self.__balance-amount
            print("withdraw sucess",x)
        else:
            print("Insufficient amount")
    def deposite(self,amount):
        if self.__balance>=0:
            x=self.__balance+amount
            print("Deposite is sucess",amount)
            print("Final total is",x)
b=bank(1232,"veera")
b.gets()
b.withdraw(10000)
b.deposite(100)
