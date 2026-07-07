''' Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where: 
 o Key = Roll Number  
 o Value = Student Name 
  • Search for the given roll number. 
   • Return the student name if found;
    otherwise return "Student Not Found".  
    
    The main program should: 
    • Create a dictionary of at least 5 students.  
• Accept a roll number from the user. 
 • Display the search result.  '''
 #----------------------------------------------------------
def search_student(student_dict, roll_no):
    roll_no = int(roll_no)
    if roll_no in student_dict:
        return student_dict[roll_no]
    return "Student Not Found "  
#------------------------------------------------------------------------------------------
#main program:
student_dict = {}
roll_no = 1
#input how many students :
n=int(input("Enter the number of students:"))
#initialize :
if n <=0:
    exit("student must be positive")
for x in range(1, n+1):
    #taking input no. and name:
    name = input("Enter the student %d name: "%roll_no)
    student_dict[roll_no] = name
    roll_no = roll_no + 1 
print("----------------------------------------")
print("List of students:",student_dict)
print("----------------------------------------")
#input from user:
roll_no = input("Enter the roll number of the student :")
print("Student name = ",search_student(student_dict, roll_no)) 
#---------------------------------------------------------------------------
'''enter the number of students:5
Enter the student 1 name: sanjay
Enter the student 2 name: ankit
Enter the student 3 name: udit
Enter the student 4 name: sagar
Enter the student 5 name: varun
List of students: {1: 'sanjay', 2: 'ankit', 3: 'udit', 4: 'sagar', 5: 'varun'}
Enter the roll number of the student :3
Student name =  udit'''