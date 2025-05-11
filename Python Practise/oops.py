class Account:
  def __init__(self,Balance,AccNo):
    self.Balance=Balance
    self.AccNo=AccNo
    
  def debit(self,amount):
    current_bal = self.Balance - amount
      
    print ("Total Balance :",self.Balance,"Now Balance is :",current_bal)
  def credit(self,amount):
    current_bal = self.Balance + amount
    print ("Total Balance :",self.Balance,"Now Balance is :",current_bal)
  def get_balance(self):
    print ("Current Balance is:",self.Balance)   

  
s1=Account(5000,500134)
s1.debit(200)
s1.credit(400)
s1.get_balance()