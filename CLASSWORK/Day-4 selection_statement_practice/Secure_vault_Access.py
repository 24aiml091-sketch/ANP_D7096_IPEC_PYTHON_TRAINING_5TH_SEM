'''Write a Python program that accepts the entered security code. 
If the entered code is 7890, display: "Access Granted to the Vault." '''
#----------------------------------------------
''''Sample Input 7890 
Sample Output 
Access Granted to the Vault.'''
#------------------------coding---------------------------- 
#input from the user :
password = int(input("Enter the password : "))
#validation
if(password < 0):
    exit()
if(password >= 10000):
    exit()

    
if( password == 7890):
    print("Access Granted to the vault.")

else:
    exit()

#-------------------------output---------------------------
#Enter the password : 6742