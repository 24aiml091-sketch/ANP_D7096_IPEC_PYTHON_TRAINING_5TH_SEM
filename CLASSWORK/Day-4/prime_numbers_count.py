'''Accept two integers representing the starting and ending values of a range.
Display all prime numbers within the range and finally display the total number of prime numbers found. '''

#--------------------------------------
#coding----------------

#input from the user:
num = int(input("Enter the number(starting range): "))
num1 = int(input("Enter the number(ending range): "))
counter = 0
#printing prime numbers
for i in range(num,num1+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        print(i)
        counter += 1
print("Total number of prime numbers found: ",counter)
