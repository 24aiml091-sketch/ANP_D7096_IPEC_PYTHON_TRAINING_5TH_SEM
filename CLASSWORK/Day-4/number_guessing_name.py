'''A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered
. Display whether the entered number is too high, too low, or correct.'''
#-----------------------
#--------------coding------------------
number = int(input("Enter the correct number :"))
#validation 
if(number < 0):
    exit()
if(number > 100):
    exit()

#Displaying whether the entered number is too high, too low, or correct.

if(number < 37):
    print("too low")
elif(number > 37):
    print("too high")
        
    number = int(input("Enter the correct number :"))
    #validation 
    if(number < 0):
        exit()
    if(number > 100):
        exit()

print("Correct")