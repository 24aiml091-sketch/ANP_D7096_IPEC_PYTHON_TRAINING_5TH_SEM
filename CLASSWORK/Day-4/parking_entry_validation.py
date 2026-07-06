'''Only vehicles having a valid parking pass are allowed to enter a private parking area. '''
#-----------------------------------------------------
'''Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, 
display: Entry Allowed 
• Otherwise display: Entry Denied'''
vehicle_pass = int(input("Enter the pass(1/0) :"))
if(vehicle_pass == 1):
    print("Entry Allowed")
else:
    print("Entry Denied")
