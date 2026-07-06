'''Deletion pf element from list'''
#-----------------------------
#------------coding-----------------
#List creating:
subject_list = ['python','java','c++','dsa','cpp','docker','OOPS','c','Data structure','OS']

#input from user :    
index = int(input("Enter the index of element to delete(0/9) : "))
#validation :
if(index < 0):
    exit("Index out of range")
if(index >= len(subject_list)):
    exit("Index out of range")
#Deletion element by index:
subject_list.pop(index)
print("Updated List:",subject_list)
#-----------------------------------------
#------------output----------------------
'''Enter the index of element to delete(0/9) : 8
['python', 'java', 'c++', 'cpp','Data structure']'''