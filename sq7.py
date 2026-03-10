from abc import ABC, abstractmethod

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
    
    def log_transaction(details):
        pass
    
class CreditCardProcessor(PaymentProcessor):
    pass
class PayPalProcessor(PaymentProcessor):
    pass
class CryptoProcessor(PaymentProcessor):
    pass 