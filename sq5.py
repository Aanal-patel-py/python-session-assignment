class Account:
    a_balance=0
    def __init__(self,account_no,balance,owner):
        self.account_no=account_no
        self.balance=balance
        self.owner=owner
        Account.a_balance+=balance
    
    def deposit(self,amt):
        self.balance+=amt
        Account.a_balance+=amt

    def withdraw(self,amt):
        if amt>self.balance:
            raise InsufficientFundsError(self.balance,amt)
        self.balance-=amt
        Account.a_balance-=amt

    def transfer(self,amt,another_account):
        self.withdraw(amt)
        another_account.deposit(amt)

    @classmethod
    def total_money(cls):
        return cls.a_balance

# def logging(func)

class SavingsAccount(Account):

    def __init__(self,account_no,balance,owner,interest_rate,minimum_balance):
        super().__init__(account_no,balance,owner)
        self.interest_rate=interest_rate
        self.minimum_balance=minimum_balance

class ChekingAccount(Account):

    def __init__(self,account_no,balance,owner,overdraft_limit):
        super().__init__(account_no,balance,owner)
        self.overdraft_limit=overdraft_limit

class InsufficientFundsError(Exception):

    def __init__(self,balance,amt_withdraw):
        self.balance=balance
        self.amt_withdraw=amt_withdraw
        message=f"cannot withdraw. balance is {balance}"
        super().__init__(message)

x=SavingsAccount(1,1000,"abc",3,400)
y=SavingsAccount(2,5000,"xyz",3,400)
x.transfer(200,y)
print(x.balance)
print(y.balance)

x.deposit(400)
print(x.balance)

try:
    x.withdraw(5000)
except InsufficientFundsError as e:
    print(e)
total_balance=Account.total_money()
print(total_balance)