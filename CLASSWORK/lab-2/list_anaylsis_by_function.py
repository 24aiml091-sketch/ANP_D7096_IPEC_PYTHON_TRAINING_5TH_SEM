'''Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list.'''
#-----------------------------------------------------
#------------------coding----------------------------

#creating an empty list:
list = []

# Input from the user: 
print("Please enter 10 integers:")
n=0
for i in range(1, 11):
    val = int(input("Enter the number %d: " %(n+1)))
    list.append(val)
    n=n+1

# Display the results
print("\n--- List Analysis Results ---")
print("Numbers list:", list)
print("Maximum value =", max(list))
print("Minimum value =", min(list))
print("Average value =", sum(list)/len(list))
#-----------------------------------------------------
'''Please enter 10 integers:
Enter the number 1 : 10
Enter the number 2 : 20
Enter the number 3 : 10
Enter the number 4 : 20
Enter the number 5 : 30
Enter the number 6 : 50
Enter the number 7 : 10
Enter the number 8 : 20
Enter the number 9 : 30
Enter the number 10 : 10

--- List Analysis Results ---
Numbers list: [10, 20, 10, 20, 30, 50, 10, 20, 30, 10]
Maximum value = 50
Minimum value = 10
Average value = 21.0'''
