''' A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or more. 
Otherwise, the customer must pay a parking fee of ₹100. '''
#----------------------------------------------------------------
#--------sample input----------------
'''Sample Input 1
Enter total purchase amount (in ₹): 2500
Parking Fee: Free!

Sample Input 2
Enter total purchase amount (in ₹): 1500
Parking Fee: ₹100'''
#---------------------------------------------------------------
#----------- Coding --------------------------------------------
#---------------------------------------------------------------
purchases = float(input("Enter total purchase amount(in Rs) : "))
if(purchases < 0):
    exit("purchases must be greater than 0")
if(purchases >= 2000):
    print("Parking Fee: Free!")
else:
    print("Parking Fee: ₹100")
#----------------------------------------------------------------
#----------output------------------
'''Enter total purchase amount(in Rs) : 2500
Parking Fee: Free!'''
