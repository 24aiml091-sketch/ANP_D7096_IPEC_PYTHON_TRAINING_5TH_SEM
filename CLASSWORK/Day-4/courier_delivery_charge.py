'''A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180
-----------------------------------------------------------
Sample Input
 4 
 Sample Output 
 Delivery Charge = ₹100 
 ---------------------------------------------------------

'''
#-------------------------------coding-------------------------
weight = float(input("Enter the weight of the package(in kg) : "))
if(weight <= 2):
    charge = 50
elif(weight <= 5):
    charge = 100
else:
    charge = 180
print("Delivery Charge = ", charge,"Rs")
