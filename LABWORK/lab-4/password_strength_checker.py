'''Problem 8: Password Strength Checker--
 Accept a password and check whether it satisfies: 
• Minimum 8 characters  
• At least one uppercase letter
  • At least one lowercase letter  
• At least one digit 
 • At least one special character  '''
#---------------------------------
#taking the passwrod from the user:
password = input("Enter the password:")

upper = lower = digit = special = False

for ch in password:

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

    else:
        special = True

strong = True
#checking password length:
if len(password) < 8:
    print("Minimum 8 characters required")
    strong=False

if not upper:
    print("Missing Uppercase")
    strong=False

if not lower:
    print("Missing Lowercase")
    strong=False

if not digit:
    print("Missing Digit")
    strong=False

if not special:
    print("Missing Special Character")
    strong=False
#-----------------------------------
if strong:
    print("Strong Password")
else:
    print("Weak Password")