'''Problem 1: Electricity Bill Calculator
 Write a Python program that calculates the electricity bill based on the following conditions: 
Units Rate per Unit First 100 Next 100 ₹5 ₹7 Above 200 ₹10 Additional Charges: 
• If the bill exceeds ₹2000, 
apply a 5% surcharge.
  • If the total bill is below ₹500, 
the minimum bill should be ₹500.  
Display: 
• Total Units 
 • Bill Amount 
 • Final Payable Amount

#------------------------------------------------------------
#input bill from user:
units = int(input("Enter units consumed: "))
bill = 0
#Rate of charges on unit:
if units <=100:
   bill = units*5
elif unit <=200:
   bill =(100*5)+((unit - 100)*7)
else:
   bill =(100*5)+(100*7)+((units-200)*10)

#--------------------------------------------------------
#addtional charges on > 2000:
if bill > 2000:
   bill +=bill*0.05

if bill < 500:
   bill = 500

print("Total units:",units)
print9"Bill amount:",bill)
print("final Payable Amount:",bill)

 