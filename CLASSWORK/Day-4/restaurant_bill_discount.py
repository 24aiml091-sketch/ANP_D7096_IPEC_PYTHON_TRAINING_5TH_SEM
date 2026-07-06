'''A restaurant offers discounts based on the total bill amount. 
• Bill below ₹1000 → No Discount  
• ₹1000–₹2999 → 10% Discount 
 • ₹3000 or more → 20% Discount'''
 #-----------------coding----------------
 #input from the user :
total_bill = float(input("Enter the total bill amount(in Rs) : "))
if(total_bill < 0):
    exit()
if(total_bill < 1000):
    print("No Discount")
    print("Total Bill = ", total_bill)
elif(total_bill < 3000):
    discount = total_bill * 0.10
    print("Discount = ", discount)
    print("Total Bill = ", total_bill)
else:
    discount = total_bill * 0.20
    print("Discount = ", discount)
    print("Total Bill = ", total_bill)    
#---------------------------------------
#-----------output---------------------

    