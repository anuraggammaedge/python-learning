# Create a class BankAccount with methods for deposit, withdrawal, balance check, and transaction history.
import datetime 

class InsufficientFundsError(Exception):
    def __init__(self):
        print(f'Insufficient Balance')


class BankAccount:
    _amount = 0
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions = []

    def __init__(self, acc_holder_name):
        self.acc_holder_name = acc_holder_name
        print(f"Welcome Back {acc_holder_name}!")
        print(self.transactions)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._amount += amount
        self.transactions.append({'deposit': amount, 'datetime': self.current_time, 'total_amount': self._amount})
        return print(f'{amount} Deposit Successfully. Total amount: {self._amount}')
    
    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal Amount cannot be negative")
        
        if amount > self._amount:
            # print(f'Insufficient Balance. Available: {self._amount}')
            # return 
            raise InsufficientFundsError()

        self._amount -= amount
        self.transactions.append({'withdrawal': amount, 'datetime': self.current_time, 'total_amount': self._amount})
        return print(f'{amount} withdrawal Successfully. Total amount: {self._amount}')
        

    def balance_check(self) -> int:
        return self._amount
    
    def transaction_history(self):
        for data in self.transactions[::-1]:
            deposit = data.get('deposit')
            withdrawal = data.get('withdrawal')
            if deposit:
                print(f'Deposite {data['deposit']} at {data['datetime']}. Available: {data['total_amount']}')
            
            if withdrawal:
                print(f'withdrawal {data['withdrawal']} at {data['datetime']}. Available: {data['total_amount']}')
    

anurag_acc = BankAccount("Aurag Dubey")

print("Account balance" , anurag_acc.balance_check())

anurag_acc.deposit(1000)

anurag_acc.withdrawal(500)
anurag_acc.withdrawal(500)
anurag_acc.withdrawal(500)

anurag_acc.deposit(300)
print("Account balance" , anurag_acc.balance_check())
anurag_acc.transaction_history()