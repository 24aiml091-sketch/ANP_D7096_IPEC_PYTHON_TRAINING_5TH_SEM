'''Problem 5: List Processing Accept 20 integers from the user into a list.
 Perform the following:
 a) Print largest number  
b) Print second largest number 
 c) Print smallest number  
d) Remove duplicate elements  
e) Print only even numbers  
f) Print numbers divisible by both 3 and 5  
g) Reverse the list without using reverse()  '''
#-----------------------------------------------------
#creating the blank list:
mylist = []

#input the 20 integers
print("Enter 20 integers:")

for i in range(20):
    mylist.append(int(input()))
#largest number:
print("Largest:", max(mylist))

unique = list(set(mylist))
unique.sort(reverse=True)

print("Second Largest:", unique[1])
print("Smallest:", min(mylist))

print("Without Duplicates:", unique)
#printing the even numbers:
print("Even Numbers:")
for i in mylist:
    if i % 2 == 0:
        print(i, end=" ")

print("\nDivisible by 3 and 5:")

for i in mylist:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

print("\nReverse List:")

for i in range(len(mylist)-1,-1,-1):
    print(mylist[i], end=" ")