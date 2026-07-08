'''Students are allowed to enter the examination hall only if they are carrying their admit card. 
Accept input as:
 • 1 → Admit Card Available  
• 0 → Admit Card Not Available '''
#----------------------------------------
#-----------coding-----------------------
#input from the user:
admit_card = int(input("Enter the admit card(1/0) : "))
#validation
if(admit_card < 0):
    exit()
    
if(admit_card > 1):
    exit()


#Checking the admit card
if(admit_card ==1 ):
    print("Admit card is available")
else:
    print("Admit card is not available")
#----------------------------------
#---------------output---------------
'''Enter the admit card(1/0) : 2'''
#--------------------------------
'''Enter the admit card(1/0) :1
Admit card is available'''

