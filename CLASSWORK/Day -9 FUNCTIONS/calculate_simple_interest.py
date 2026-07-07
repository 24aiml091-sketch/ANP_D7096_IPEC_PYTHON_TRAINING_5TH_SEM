#creating function :
def calculate_simple_interest(principal , rate, time):
    return (principal * rate * time) / 100  
principal = float(input("Enter the principal amount: ")) 
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))   
#print simple interest :
print("The simple interest is: ", calculate_simple_interest(principal, rate, time))
#---------------output--------------
'''Enter the principal amount: 10000
Enter the rate of interest: 5
Enter the time in years: 10
The simple interest is:  5000.0'''