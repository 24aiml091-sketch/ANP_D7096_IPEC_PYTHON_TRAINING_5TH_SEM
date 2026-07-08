'''Write a function check_password(password) that checks whether a password is strong.
 A password is considered Strong if: 
 • It contains at least 8 characters. 
  • It contains at least one uppercase letter.  
  • It contains at least one lowercase letter.  
  • It contains at least one digit.  
  The function should return: 
  • "Strong Password" 
  or 
   • "Weak Password"  
The main program should accept a password from the user and display the result.'''
#-----------------coding----------------------
#---------------------------------------------
def check_password(password):
    if len(password) <= 8:
        return "Weak Password"
    #condition-----
    has_upper = False
    has_lower = False
    has_digit = False
    #checking upper,lower,digits-----
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
            
    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"
#-----------------------------------------------------
# Main program
if __name__ == "__main__":
    user_password = input("Enter the password: ")
    result = check_password(user_password)
    print(result)
#----------------output------------------
'''Enter the password: SAnjatsahu3848@
Strong Password'''