from abc import ABC, abstractmethod
import re

class PaymentProcessor(ABC):

    @abstractmethod
    def validate():
        pass
    @abstractmethod
    def process_payment(amount):
        pass
    
    @abstractmethod
    def refund(transaction_id):
        pass
    
    def log_transaction(self,details):
        print(details)
    
class CreditCardProcessor(PaymentProcessor):

    def __init__(self,creditcard_number):
        self.creditcard_number=creditcard_number
        
    def validate(self):
        if len(str(self.creditcard_number))==16:
            print("valid card number")
        else:
            print("invalid")
    
    def process_payment(self,amount):
        self.log_transaction(f"transaction done of amount {amount} for {self.creditcard_number} by creditcard")

    def refund(self,transaction_id):
        print(f"failed transaction payment refunt to {transaction_id} in creditcard processor")

    
        
class PayPalProcessor(PaymentProcessor):
    

    def __init__(self,email):
        self.email=email
        
    def validate(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(pattern,self.email):
            print("correct email")
        else:
            print("incorrect email format")
    
    def process_payment(self,amount):
       self.log_transaction(f"transaction done of amount {amount} for {self.email} by paypalprocessor")

    def refund(self,transaction_id):
        print(f"failed transaction payment refund to {transaction_id} in  paypalprocessor")
    
class CryptoProcessor(PaymentProcessor):
    def __init__(self,wallet_id):
        self.wallet_id=wallet_id
        
    def validate(self):
        if len(str(self.wallet_id))<42 and len(str(self.wallet_id))>24:
            print(" wallet length valid")
        else:
            print("invalid")
    
    def process_payment(self,amount):
        self.log_transaction(f"transaction done of amount {amount} for {self.wallet_id} by cryptoprocessor")

    def refund(self,transaction_id):
        print(f"failed transaction payment refunt to {transaction_id} in crypto wallet")



x=CreditCardProcessor(1234567890111112)
y=PayPalProcessor("aanal@gmail.com")
z=CryptoProcessor(12345678903456457568698612345678901234)

group=[x,y,z]
for p in group:
    p.validate()
    p.process_payment(2000)
    p.refund(1)

