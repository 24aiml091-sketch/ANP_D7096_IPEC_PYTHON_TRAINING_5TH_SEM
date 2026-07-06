'''An ATM allows a user to enter the correct PIN. The correct PIN is 4589.
 The user can keep entering the PIN until it matches the correct one.'''
'''An ATM allows a user to enter the correct PIN. 
 The correct PIN is 4589. 
 The user can keep entering the PIN until it matches the correct one.'''
#-------------------------------------------------------------
#-------------coding---------------------
#input from the user: 
pin = int(input("Enter the PIN : "))
 #validation
if(pin < 0):
    exit()
if(pin >= 10000):
    exit()
 #Checking the PIN
while(pin != 4589):
    pin = int(input("Enter the PIN : "))
    #validation
    if(pin < 0):
        exit()
    if(pin >= 10000):
        exit()
print("PIN is correct")
 #--------------------------output-----------------------