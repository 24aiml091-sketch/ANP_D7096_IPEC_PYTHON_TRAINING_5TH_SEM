'''Create another Python file named operations.py that imports the twodfigures module and performs
 the following tasks: 
 1. Display a menu for selecting one of the following figures:
  o Square 
  o Circle 
  o Triangle 
  o Rectangle 

  2. Based on the user's choice, ask for the required dimensions of the selected figure.
   o Example: 
   ▪ Circle → Radius 
   ▪ Square → Side 
   ▪ Rectangle → Length and Breadth 
   ▪ Triangle → Three sides (for perimeter) and Base & Height (for area) 

   3. Display a second menu to choose the required operation:
    o Area 
    o Perimeter 

    4. Call the appropriate function from the twodfigures module based on the user's selections.

     5. Display the calculated result in a user-friendly format.

     6. Allow the user to perform multiple calculations until they choose to exit the application. 

'''
#importing module :
import twodfigures

choice = 0
while choice != 5:
    #Display a menu for selecting one of the following figures:
    print("\n 1. Square" )
    print("\n 2. Circle" )
    print("\n 3. Triangle" )
    print("\n 4. Rectangle" )
    print("\n 5. Exit" )
    
    #choice input :
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("\nExiting the application. Goodbye!")
        break

    elif choice == 1:
        print("\n 1. Area" )
        print("\n 2. Perimeter" )
        try:
            operation = int(input("\nEnter your operation: "))
        except ValueError:
            print("Invalid input!")
            continue
            
        #operation on square:
        if operation == 1:
            side = float(input("\nEnter the side of the square: "))
            print("\n Area of square is : ", twodfigures.calculate_square_area(side))
        elif operation == 2:
            side = float(input("\nEnter the side of the square: "))
            print("\n Perimeter of square is : ", twodfigures.calculate_square_perimeter(side))
        else:
            print("Invalid operation selection.")

    elif choice == 2:
        print("\n 1. Area" )
        print("\n 2. Circumference" )
        try:
            operation = int(input("\nEnter your operation: "))
        except ValueError:
            print("Invalid input!")
            continue
            
        #operation on circle:
        if operation == 1:
            radius = float(input("\nEnter the radius of the circle: "))
            print("\n Area of circle is : ", twodfigures.calculate_circle_area(radius))
        elif operation == 2:
            radius = float(input("\nEnter the radius of the circle: "))
            print("\n Circumference of circle is : ", twodfigures.calculate_circle_circumference(radius))
        else:
            print("Invalid operation selection.")

    elif choice == 3:
        print("\n 1. Area" )
        print("\n 2. Perimeter" )
        try:
            operation = int(input("\nEnter your operation: "))
        except ValueError:
            print("Invalid input!")
            continue
            
        #operation on triangle:
        if operation == 1:
            base = float(input("\nEnter the base of the triangle: "))
            height = float(input("\nEnter the height of the triangle: "))
            print("\n Area of triangle is : ", twodfigures.calculate_triangle_area(height, base))
        elif operation == 2:
            side1 = float(input("\nEnter the side1 of the triangle: "))
            side2 = float(input("\nEnter the side2 of the triangle: "))
            side3 = float(input("\nEnter the side3 of the triangle: "))
            print("\n Perimeter of triangle is : ", twodfigures.calculate_triangle_perimeter(side1, side2, side3))
        else:
            print("Invalid operation selection.")

    elif choice == 4:
        print("\n 1. Area" )
        print("\n 2. Perimeter" )
        try:
            operation = int(input("\nEnter your operation: "))
        except ValueError:
            print("Invalid input!")
            continue
            
        #operation on rectangle:
        if operation == 1:
            length = float(input("\nEnter the length of the rectangle: "))
            width = float(input("\nEnter the width of the rectangle: "))
            print("\n Area of rectangle is : ", twodfigures.calculate_rectangle_area(length, width))
        elif operation == 2:
            length = float(input("\nEnter the length of the rectangle: "))
            width = float(input("\nEnter the width of the rectangle: "))
            print("\n Perimeter of rectangle is : ", twodfigures.calculate_rectangle_perimeter(length, width))
        else:
            print("Invalid operation selection.")
    else:
        print("Invalid choice. Please choose an option from 1 to 5.")
