'''Problem Statement Create a class named Student to store and display a student's details. 
Requirements
 1. Create a class Student. 
2. Define the following instance variables: 
 o student_id 
 o name 
 o course 
 o marks  
3. Create a method accept_data() to take input from the user. 
4. Create a method display_data() to display all student details. 
5. Create another method check_result() that: 
 o Displays "Pass" if marks are 35 or above 
 o Displays "Fail" otherwise. 
6. Create an object of the class and call all the methods.  '''
#--------------------------------------------------------------
#class
class Student:
    #intialise instance variables
    def __init__(self):
        self.student_id = 0
        self.name = ""
        self.course = ""
        self.marks = 0.0
    #method to accept details
    def accept_data(self):
        self.student_id =int(input("Enter student ID : "))
        self.name = input("Enter student name : ")
        self.course = input("Enter course name : ")
        self.marks = float(input("Enter marks : "))
        print("\n Student details accepted successfully")
    
    #display details
    def display_data(self):
        print("------------------------------------")
        print("Student details are as follows")
        print("Student ID :",self.student_id)
        print("Name :",self.name)
        print("Course :",self.course)
        print("Marks :",self.marks)
        print("------------------------------------")
    #check result
    def check_result(self):
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")
    #main program
print("----Enter student details----")
student = Student()
student.accept_data()
student.display_data()
student.check_result()
#---------------------------------------------------------------------
#--------------------output-------------------------------------------
'''----Enter student details----
Enter student ID : 5413045
Enter student name : sanjay sahu
Enter course name : B.Tech
Enter marks : 99

 Student details accepted successfully
------------------------------------
Student details are as follows
Student ID : 5413045
Name : sanjay sahu
Course : B.Tech
Marks : 99.0
------------------------------------
Pass'''       
