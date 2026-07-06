'''A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 
or more. '''

'''Sample Input 1 
Enter your monthly salary: 45000 
Sample Output 1 Congratulations! 
You are eligible to apply for the loan.
#----------------------------------------- 
Sample Input 2 
Enter your monthly salary: 22000 
Sample Output 2 
Sorry! You are not eligible to apply for the loan'''
#--------------------------------------------
#----------- Coding ------------------------
#--------------------------------------------
salary = float(input("Enter the monthly salary(in Rs) : "))
if(salary < 0):
    exit("Salary must be greater than 0")
if(salary >= 30000):
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

# ----------------------------------------------------------------
# ----------output------------------
'''Enter the monthly salary(in Rs) : 45000
Congratulations! You are eligible to apply for the loan.
'''