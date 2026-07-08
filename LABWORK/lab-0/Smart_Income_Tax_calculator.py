'''A government tax portal calculates tax based on the following conditions:
• Income up to ₹5,00,000 → No tax
• ₹5,00,001 to ₹10,00,000 → 10%
• ₹10,00,001 to ₹20,00,000 → 20%
• Above ₹20,00,000 → 30%
Additional Benefits:
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.
• Women taxpayers receive an additional 2% rebate on tax. '''
#--------------------------------------------------
'''Sample Input
Enter Annual Income: 1200000
Enter Age: 65
Enter Gender (M/F): F
Sample Output
Tax before rebate: ₹240000.0
Senior Citizen Rebate: ₹12000.0
Women Rebate: ₹4800.0
Final Tax Payable: ₹223200.0'''
#--------------------------------------------------------------------
income = float(input("Enter the income(in Rs) : "))
age = int(input("Enter the age(in years) : "))
gender = input("Enter the gender(M/F) : ")
if(income <= 500000):
    tax = 0
elif(income <= 1000000):
    tax = income * 0.10
elif(income <= 2000000):
    tax = income * 0.20
else:
    tax = income * 0.30
if(age >= 60):
    tax = tax * 0.95
if(gender == "F"):
    tax = tax * 0.98
print("-------------------------")
print("Tax before rebate: ", tax)
print("Senior Citizen Rebate: ", tax * 0.05)
print("Women Rebate: ", tax * 0.02)
print("Final Tax Payable: ", tax)
#-------------------------------------
#------------------Output------------
'''Enter the income(in Rs) : 1200000
Enter the age(in years) : 65
Enter the gender(M/F) : M
---------------------------------------
Tax before rebate:  228000.0
Senior Citizen Rebate:  11400.0      
Women Rebate:  4560.0
Final Tax Payable:  228000.0'''
#-------------------------------------------
'''Enter the income(in Rs) : 3000000
Enter the age(in years) : 45
Enter the gender(M/F) : F
-------------------------------------------
Tax before rebate:  882000.0
Senior Citizen Rebate:  44100.0
Women Rebate:  17640.0
Final Tax Payable:  882000.0'''