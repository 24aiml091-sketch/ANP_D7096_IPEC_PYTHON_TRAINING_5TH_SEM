'''Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0–100) as a parameter. 
 • Return the grade according to the following
  criteria:  
  o 90 and above → A+ 
    o 75–89 → A  
    o 60–74 → B  o 40–59 → C  
    o Below 40 → Fail 
     The main program should:
      • Accept marks of 5 students.

  • Call the function for each student.
    • Display the marks and corresponding grade.'''
def calculate_grade(marks):
    if(marks >=90):
        return("A+")
    elif(marks >=75):
        return("A")
    elif(marks >=60):
        return("B")
    elif(marks >=40):
        return("C")
    else:
        return("Fail")
#main program :
students = []
#input from user
num_students = int(input("Enter the number of students:"))
if(num_students<=0):
    print("Number of students must be positive")
    exit()
n=1
for i in range(num_students):
    marks = float(input("Enter the marks of student %d :"%n))
    if(marks<0 or marks>100):
        print("Marks must be between 0 and 100")
        continue
    students.append(marks)
print("Mark : Grade")
print("----------------")
for i in students:
    print(i , ":", calculate_grade(i))
    
