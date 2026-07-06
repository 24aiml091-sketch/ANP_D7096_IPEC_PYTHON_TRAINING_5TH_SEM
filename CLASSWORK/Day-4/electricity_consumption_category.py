'''An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption 
 • 101–300 units → Moderate Consumption  
 • Above 300 units → High Consumption '''
 #-----------------------------coding-----------------------------
 #input from the user : 
units = int(input("Enter the units of electricity consumed : "))
#validation
if(units <= 0):
    exit("Invalid input! Number of units must be positive.")

#Electricity consumption category
if(units <=100):
    print("Low Consumption")
elif(units <=300):
    print("Moderate Consumption")
else:
    print("High Consumption")
#---------------------------
#-----------output----------
