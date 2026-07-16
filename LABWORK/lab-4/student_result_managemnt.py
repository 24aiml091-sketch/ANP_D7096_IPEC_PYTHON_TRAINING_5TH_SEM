'''Problem 7: Student Result Management--
 Create a dictionary
 where Roll No → Marks Store details of 10 students.
 Perform:
 • Find topper 
 • Find average marks  
• Display students scoring above average
  • Count failed students (Marks < 35) 
 • Display grade using'''
#-------------------------------------
#creating the dict:
students = {}
#asking the roll no:
for i in range(10):
    roll = input("Roll No: ")
    marks = int(input("Marks: "))
    students[roll] = marks
#find the topper:
topper = max(students, key=students.get)

print("Topper:", topper, students[topper])
#find the average:
avg = sum(students.values()) / len(students)

print("Average:", avg)

print("Above Average:")

for r,m in students.items():
    if m > avg:
        print(r,m)

fail = 0

for m in students.values():
    if m < 35:
        fail += 1

print("Failed Students:", fail)

for r,m in students.items():
#grading:
    if m>=90:
        grade="A"
    elif m>=75:
        grade="B"
    elif m>=60:
        grade="C"
    elif m>=35:
        grade="D"
    else:
        grade="Fail"
#printing the marks:
    print(r,m,grade)