'''Problem 4: Employee Salary Calculator----
Create the following functions:
 calculate_hra(basic) 
calculate_da(basic) 
calculate_tax(gross_salary) 
calculate_net_salary(basic)
 Rules:
 • HRA = 20%  
• DA = 10%  
• Tax = 8% of Gross Salary ''' 
#--------------------------------------------
#creating the function:
def calculate_hra(basic):
    return basic * 0.20

def calculate_da(basic):
    return basic * 0.10

def calculate_tax(gross):
    return gross * 0.08

def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    gross = basic + hra + da
    tax = calculate_tax(gross)
    net = gross - tax
#printing the salary according to calcilation:
    print("Basic Salary:", basic)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross Salary:", gross)
    print("Tax:", tax)
    print("Net Salary:", net)
#salary from user:
basic = float(input("Enter Basic Salary: "))
calculate_net_salary(basic)