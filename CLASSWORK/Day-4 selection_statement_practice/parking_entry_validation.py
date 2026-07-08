'''Only vehicles having a valid parking pass are allowed to enter a private parking area. '''
#-----------------------------------------------------
'''Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, 
display: Entry Allowed 
• Otherwise display: Entry Denied'''
#-----------------coding-------------------------------
#input from the user:
vehicle_pass = int(input("Enter the pass(1/0) :"))
#validation
if(vehicle_pass < 0):
    exit()
if(vehicle_pass > 1):
    exit()

if(vehicle_pass == 1):
    print("Entry Allowed")
else:
    print("Entry Denied")

#-----------------------------------------------------------
#----------OUTPUT-------------------------------------
'''Enter the pass(1/0) :0
Entry Denied'''
