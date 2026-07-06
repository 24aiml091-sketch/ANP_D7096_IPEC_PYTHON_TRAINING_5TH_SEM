'''Create a nested dictionary to store marks of students in three subjects.
 Example: 
 { 
 'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
 'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
 'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
 }
  Write a program to: • Calculate the total marks of each student. 
   • Calculate the average marks of each student. 
    • Display the topper based on total marks.  
    • Display the subject-wise highest marks along with the student's name.  
 • Display students whose average is greater than or equal to 85.'''

#------------------coding-------------------------
students = { 
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
    'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
}

# 1 & 2. Calculate the total and average marks of each student
print("--- Total and Average Marks of Each Student ---")
totals = {}
averages = {}
for student, subjects in students.items():
    total = sum(subjects.values())
    avg = total / len(subjects)
    totals[student] = total
    averages[student] = avg
    print(f"Student: {student} | Total Marks: {total} | Average Marks: {avg:.2f}")

# 3. Display the topper based on total marks
print("\n--- Topper ---")
topper = max(totals, key=totals.get)
print(f"Topper: {topper} with {totals[topper]} total marks")

# 4. Display the subject-wise highest marks along with the student's name
print("\n--- Subject-wise Highest Marks ---")
# Get list of unique subjects while preserving order of appearance
subjects_list = []
for marks in students.values():
    for subject in marks.keys():
        if subject not in subjects_list:
            subjects_list.append(subject)

for subject in subjects_list:
    highest_mark = -1
    highest_student = ""
    for student, marks in students.items():
        if subject in marks:
            if marks[subject] > highest_mark:
                highest_mark = marks[subject]
                highest_student = student
    print(f"Highest in {subject}: {highest_mark} (Scored by: {highest_student})")

# 5. Display students whose average is greater than or equal to 85
print("\n--- Students with Average >= 85 ---")
for student, avg in averages.items():
    if avg >= 85:
        print(f"Student: {student} | Average: {avg:.2f}")

#output:
'''
--- Total and Average Marks of Each Student ---
Student: Rahul | Total Marks: 263 | Average Marks: 87.67
Student: Priya | Total Marks: 255 | Average Marks: 85.00
Student: Ankit | Total Marks: 274 | Average Marks: 91.33

--- Topper ---
Topper: Ankit with 274 total marks

--- Subject-wise Highest Marks ---
Highest in Math: 91 (Scored by: Ankit)
Highest in Science: 95 (Scored by: Priya)
Highest in English: 94 (Scored by: Ankit)

--- Students with Average >= 85 ---
Student: Rahul | Average: 87.67
Student: Priya | Average: 85.00
Student: Ankit | Average: 91.33
'''