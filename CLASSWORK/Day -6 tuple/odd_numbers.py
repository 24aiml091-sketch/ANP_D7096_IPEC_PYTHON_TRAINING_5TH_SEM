'''Find the odd numbers from 15 numbers in tuple'''
#-----------------------------------------
#----coding-------------------------------
#creating a blank list :
list_numbers = []
print("Enter the 15 numbers :")
for x in range(15):
    #input from user:
    num = int(input())
    #insert elements into list
    list_numbers.append(num)
#----------------------
#convert list to tuple
numbers = tuple(list_numbers)
print("tuple of 15 numbers :")
print(numbers)
#----------------------
#find odd numbers using tuple:
print("odd numbers : ")
for elements in numbers:
    if(elements%2) !=0:
        print(elements,end=" ")
#-----------------------
#------------output--------------------
'''tuple of 15 numbers :
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
odd numbers :
1 3 5 7 9 11 13 15'''
