''' Problem Statement: 
Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing: 
 o Name  
 o Department  
 o Salary  
 Perform the following operations: 
 • Display all employee details.  
 • Search for an employee using Employee ID.  
 • Increase the salary of all employees by 10%. 
 • Display employees belonging to a specific department entered by the user.  '''

# Initialize the employee dictionary with some sample data
employees = {
    "E101": {"Name": "Sanjay", "Department": "IT", "Salary": 80000.0},
    "E102": {"Name": "Amit", "Department": "HR", "Salary": 50000.0},
    "E103": {"Name": "Rohan", "Department": "IT", "Salary": 75000.0},
    "E104": {"Name": "Kirti", "Department": "Marketing", "Salary": 60000.0}
}

# 1. Display all employee details
print("--- Displaying All Employee Details ---")
for emp_id, info in employees.items():
    print(f"ID: {emp_id} | Name: {info['Name']} | Department: {info['Department']} | Salary: {info['Salary']}")

# 2. Search for an employee using Employee ID
print("\n--- Search Employee by ID ---")
search_id = input("Enter Employee ID to search: ").strip()
if search_id in employees:
    info = employees[search_id]
    print(f"Found: ID: {search_id} | Name: {info['Name']} | Department: {info['Department']} | Salary: {info['Salary']}")
else:
    print("Employee ID not found.")

# 3. Increase the salary of all employees by 10%
print("\n--- Increasing salaries by 10% ---")
for emp_id in employees:
    employees[emp_id]['Salary'] = round(employees[emp_id]['Salary'] * 1.10, 2)
print("Salaries updated.")

# 4. Display employees belonging to a specific department entered by the user
print("\n--- Display Employees by Department ---")
target_dept = input("Enter Department: ").strip()
found = False
for emp_id, info in employees.items():
    if info['Department'].lower() == target_dept.lower():
        print(f"ID: {emp_id} | Name: {info['Name']} | Department: {info['Department']} | Salary: {info['Salary']}")
        found = True
if not found:
    print(f"No employees found in the '{target_dept}' department.")
