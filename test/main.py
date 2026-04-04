class BankAccount:
   def __init__(self, balance=0):
       self.balance = balance

   def deposit(self, amount):
       self.balance += amount

   def withdraw(self, amount):
       if amount > self.balance:
           raise ValueError("Ты нищий")
       self.balance -= amount

   def transfer(self, other, amount):
       if self.balance < amount:
           raise ValueError("Ты нищий")
       self.balance -= amount
       other.balance += amount
