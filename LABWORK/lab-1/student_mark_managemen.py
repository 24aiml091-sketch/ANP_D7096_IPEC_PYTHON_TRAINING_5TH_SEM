'''Problem Statement: Create a dictionary to store the marks of 5 students, 
where the key is the student's name and the value is their marks.

 Perform the following operations:
  • Display all student names and marks.  
  • Add a new student with marks.  
  • Update the marks of an existing student.  
  • Delete a student by name. 
 • Display the student who scored the highest marks.  '''
 #------------------coding-------------------------
#creating dictionary :
my_dict = {
    "sanjay" : 99,
    "sanjeev" : 87,
    "santosh" : 93,
    "saurabh" : 89,
    "shubham" : 91
 }
print(my_dict)
#adding new student:
my_dict["kabir"] = 85
print("\nAfter adding new student:")
print(my_dict)
#updating marks:
my_dict["sanjay"] = 100
print("\nAfter updating marks:")
print(my_dict)
#deleting student:
my_dict.pop("shubham")
print("\nAfter deleting student:")
print(my_dict)
#display the student who scored the highest marks:
max(my_dict)
print("\nThe student who scored the highest marks:")
print(my_dict)

#output:
'''{'sanjay': 99, 'sanjeev': 87, 'santosh': 93, 'saurabh': 89, 'shubham': 91}

After adding new student:
{'sanjay': 99, 'sanjeev': 87, 'santosh': 93, 'saurabh': 89, 'shubham': 91, 'kabir': 85}

After updating marks:
{'sanjay': 100, 'sanjeev': 87, 'santosh': 93, 'saurabh': 89, 'shubham': 91, 'kabir': 85}

After deleting student:
{'sanjay': 100, 'sanjeev': 87, 'santosh': 93, 'saurabh': 89, 'kabir': 85}

The student who scored the highest marks:
{'sanjay': 100, 'sanjeev': 87, 'santosh': 93, 'saurabh': 89, 'kabir': 85}'''

