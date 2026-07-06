''' An electricity provider offers a 10% discount on the total bill amount if the customer's
 bill is ₹5,000 or more. Otherwise, no discount is applied. '''
#----------------------------------------------------------------
'''Sample Input 1 
Enter the electricity bill amount: 6200 
Sample Output 1 Discount Applied! 
Final Bill Amount: ₹5580.0 
#------------------------------------------------
Sample Input 2 Enter the electricity bill amount: 4200 
Sample Output 2 No Discount Applied! 
Final Bill Amount: ₹4200 '''
#----------------------------------------------------------------
#----------- Coding ---------------------------------------------
#----------------------------------------------------------------
amount = float(input("Enter the electricity bill amount(in Rs) : "))
if(amount < 0):
    exit("amount must be greater than 0")
if(amount >= 5000 ):
    print("Discount Applied!")
    final_amount = amount - (amount * 10/100)

else:
    print("No Discount Applied!")
    final_amount = amount
print("Final Bill Amount : Rs",final_amount)  

#----------------------------------------------------------------
#----------output------------------
'''Enter the electricity bill amount(in Rs) : 6200
Discount Applied!
Final Bill Amount : Rs 5580.0'''
