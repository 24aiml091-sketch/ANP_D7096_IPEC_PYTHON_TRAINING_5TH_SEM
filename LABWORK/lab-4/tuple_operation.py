'''Problem 6: Tuple Operations Create a tuple containing names of 15 students.
 Perform the following: 
• Count total students 
 • Display first five students  
• Display last five students 
 • Search a student name 
• Count occurrences of a given name 
 • Convert tuple into list and sort alphabetically '''
#-------------------------------------------------------------
#creating the tuple:
students = (
"Aman","Rahul","Riya","Kiran","Neha",
"Priya","Sanjay","Rohit","Ankit","Pooja",
"Rahul","Simran","Ajay","Meena","Kajal"
)
#total students:
print("Total Students:", len(students))

print("First Five:", students[:5])

print("Last Five:", students[-5:])

#input the searching the name:
name = input("Enter name to search: ")
#--------------------------------------------------
if name in students:
    print("Student Found")
else:
    print("Not Found")
#occurance:
print("Occurrences:", students.count(name))

student_list = list(students)
student_list.sort()
#print the list
print(student_list)