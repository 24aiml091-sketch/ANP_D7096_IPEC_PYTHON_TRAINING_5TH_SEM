'''To verify the number is natural number or not'''
#--------------------------------------
#--------------------------------------
#----------- Coding -------------------
#--------------------------------------
number = int(input("Enter the number : "))
if(number <= 0):
    exit("Number must be positive")
if(number > 0):
    print("Number is natural")
else:
    print("Number is not natural")
#--------------------------------------
#----------- Output -------------------
#--------------------------------------
'''Enter the number : 5
Number is natural
'''