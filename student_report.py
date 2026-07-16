def calculate_total_and_percentage(marks_list):
    """
    Calculates the total and percentage of marks.
    Assumes each subject is out of 100 marks.
    """
    total = sum(marks_list)
    percentage = (total / (len(marks_list) * 100)) * 100
    return total, percentage

def get_grade(percentage):
    """
    Determines the grade based on percentage using selection statements.
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def main():
    # Accept the student's name
    name = input("Enter Name: ")
    
    # Accept marks of 5 subjects
    while True:
        try:
            marks_input = input("Enter Marks: ")
            # Split by whitespace and convert to numbers (int if possible, otherwise float)
            marks = []
            for item in marks_input.split():
                val = float(item)
                # Convert to integer if it has no decimal part to match output style
                if val.is_integer():
                    marks.append(int(val))
                else:
                    marks.append(val)
            
            if len(marks) != 5:
                print("Please enter exactly 5 marks.")
                continue
            
            # Check if any marks are outside the valid 0-100 range
            if any(m < 0 or m > 100 for m in marks):
                print("Marks should be between 0 and 100. Please try again.")
                continue
                
            break
        except ValueError:
            print("Invalid input. Please enter 5 numeric values separated by spaces.")
            
    # Calculate the total and percentage using a user-defined function
    total, percentage = calculate_total_and_percentage(marks)
    
    # Get grade using selection statements
    grade = get_grade(percentage)
    
    # Display all entered marks along with total, percentage, and grade
    print(f"Student Name : {name}")
    print(f"Marks : {marks}")
    print(f"Total : {total}")
    # Display percentage with one decimal place if it has one, or format cleanly
    if percentage.is_integer():
        print(f"Percentage : {int(percentage)}")
    else:
        print(f"Percentage : {round(percentage, 2)}")
    print(f"Grade : {grade}")

if __name__ == "__main__":
    main()
