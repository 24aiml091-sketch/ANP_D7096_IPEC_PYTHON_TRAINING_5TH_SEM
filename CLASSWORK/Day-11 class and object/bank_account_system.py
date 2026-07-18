'''Problem Statement Create a simple Bank Account class that allows users to deposit and withdraw money. 
Requirements
 1. Create a class BankAccount.
  2. Define the following instance variables:
    o account_number 
    o customer_name  
    o balance
  3. Create the following methods: 
    o accept_details() – Accept account details from the user.  
    o deposit(amount) – Add the amount to the balance.  
    o withdraw(amount) – Deduct the amount if sufficient balance is available; 
    otherwise display "Insufficient Balance".  
    o display_balance() – Display account details and current balance.  
    4. Create an object of the class.
  5. Accept a deposit amount and a withdrawal amount from the user and perform both operations. '''
#---------------------------------------------------------------------
#class
class BankAccount:
    def __init(self):
        self.account_number =0
        self.customer_name = ""
        self.balance = 0.0
#accepting details of user       
    def accept_details(self):
        self.account_number =int(input("Enter account number :"))
        self.custome_name = input("Enter customer name : ")
        self.balance = float(input("Enter balance : "))
        print("\nAccount details accepted successfully")
    
    #deposit details    
    def deposit(self,amount):
        if amount >0:
            self.balance=self.balance + amount
            print("deposited successfully")
        else:
            print("deposit amount must be greater than 0")
    #withdraw details      
    def withdraw(self,amount):
        if amount>0:
          if self.balance>=amount:
             self.balance=self.balance-amount
             print("withdraw succesfully")
          else:
            print("insufficient balance")
        else:
            print("withdraw amount must be greater than 0")
     #display details       
    def display_details(self):
        print("------------------------------------")
        print("Account details are as follows")
        print("Account number:",self.account_number)
        print("Customer name:",self.custome_name)
        print("balance:",self.balance)
        print("------------------------------------")
#---------------------------------------------------------------------
#main program
#creating object of class
bank_account=BankAccount()
bank_account.accept_details()

print("----Enter deposit amount----")
deposit_amount=float(input("Enter deposit amount :"))
bank_account.deposit(deposit_amount)

print("----Enter withdraw amount----")
withdraw_amount=float(input("Enter withdraw amount :"))
bank_account.withdraw(withdraw_amount)

print("\nAccount details")
bank_account.display_details()
#---------------------------------------------------------------------
#-----output----------------------------
'''Enter account number :44646464343543543434
Enter customer name : sanjay
Enter balance : 4500

Account details accepted successfully
----Enter deposit amount----
Enter deposit amount :300
deposited successfully
----Enter withdraw amount----
Enter withdraw amount :400
withdraw succesfully

Account details
------------------------------------

Account details are as follows
Account number: 44646464343543543434
Customer name: sanjay
balance: 4400.0
------------------------------------'''
    
            
    
    