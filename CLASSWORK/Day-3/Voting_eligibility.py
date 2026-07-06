'''check the voting criteria of a person 
(age must be >18)'''
#--------------------------------
#---------------------------------
#----------Coding-----------------
#---------------------------------
nationality = input("Enter the nationality(in letters): ")
if(nationality != "indian"):
    exit("You are not eligible to vote")
age = int(input("Enter age(in year) : "))
if(age <= 0):
    exit("Age must be positive")
if(age >= 18 ):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# ----------------------------------------------------------------
# ----------output------------------
'''Enter age(in year) : 23
You are eligible to vote
'''

