'''A website requires users to create a password having at least 8 characters.
Keep asking the user to enter a password until the entered password
satisfies the minimum length requirement. '''

'''Sample 
Output 
Enter Password: hello Password too short.  
Enter Password: python@123 
Password Accepted. '''
#-----------------------------------------------------
#-------------coding----------------------------------
#user input:
password = input("Enter Password: ")

#checking
while len(password) < 8:
    print("Password too short.")
    password = input("Enter Password: ")

print("Password Accepted.")
#------------------output------------------
'''Enter Password: python
Password too short.'''