'''Problem 10: Student Record Management System ------
Create a menu-driven application. 
Each student should have:
 • Roll Number
  • Name  
• Age 
 • Course  
• Marks  
Store records using a list of dictionaries.
 Menu: 
1. Add Student 
2. Display All Students 
3. Search Student by Roll Number 
4. Update Marks 
5. Delete Student 
6. Display Topper 
7. Display Average Marks
 8. Display Students Above Average 
9. Exit '''
#----------------------------------------------
#creating the empty list
students = []

def add_student():
    roll = input("Roll Number: ")

    for s in students:
        if s["Roll"] == roll:
            print("Duplicate Roll Number")
            return

    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    marks = int(input("Marks: "))

    students.append({
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    })

def display():
    for s in students:
        print(s)

def search():
    roll = input("Enter Roll: ")

    for s in students:
        if s["Roll"] == roll:
            print(s)
            return

    print("Not Found")

def update():
    roll = input("Roll: ")

    for s in students:
        if s["Roll"] == roll:
            s["Marks"] = int(input("New Marks: "))
            return

    print("Student Not Found")

def delete():
    roll = input("Roll: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Deleted")
            return

def topper():
    top = max(students,key=lambda x:x["Marks"])
    print(top)

def average():
    avg = sum(s["Marks"] for s in students)/len(students)
    print("Average:",avg)

def above_average():
    avg = sum(s["Marks"] for s in students)/len(students)

    for s in students:
        if s["Marks"]>avg:
            print(s)

while True:

    print("\n1.Add Student")
    print("2.Display")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("6.Topper")
    print("7.Average")
    print("8.Above Average")
    print("9.Exit")

    choice = int(input("Enter Choice: "))

    if choice==1:
        add_student()

    elif choice==2:
        display()

    elif choice==3:
        search()

    elif choice==4:
        update()

    elif choice==5:
        delete()

    elif choice==6:
        topper()

    elif choice==7:
        average()

    elif choice==8:
        above_average()

    elif choice==9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")