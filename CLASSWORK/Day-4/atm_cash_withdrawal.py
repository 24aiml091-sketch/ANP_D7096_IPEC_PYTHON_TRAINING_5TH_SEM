'''A customer can withdraw money only if the requested amount does not exceed the available balance. '''
#------------------------------------------------
'''Accept the account balance and withdrawal amount. 
• If withdrawal amount is less than or equal to balance, 
display: Transaction Successful 
• Otherwise display: '''
'''Sample
 Input 
 5000 
 4500 
 Sample 
 Output 
 Transaction Successful'''
 #---------------------------------------
 #-------------coding--------------------
 
#input from the user :
balance = float(input("Enter the account balance(Rs): "))
withdrawal = float(input("Enter the withdrawal amount(Rs): "))
#Validation
if(balance < 0):
    exit()
if(withdrawal < 0):
    exit()
if(withdrawal > balance):
    print("Insufficient Balance")
else:
    print("Transaction Successful")



#----------------------------------------
#-------------output---------------------
'''Enter the account balance(Rs): 5000
Enter the withdrawal amount(Rs): 4500
Transaction Successful'''


 