
'''An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
• Total units consumed  
• Average units consumed  
• Highest consumption  
• Lowest consumption'''
#-------------------------------------------------
#----------coding---------------------------------
#input from user:
units = float(input("Enter the monthly unit consumed: "))
#validation
if(units < 0):
    exit("units must be positive")

