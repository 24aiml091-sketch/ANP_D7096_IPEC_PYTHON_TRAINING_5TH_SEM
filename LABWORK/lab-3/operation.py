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
#Display a menu for selecting one of the following figures:
print("\n 1. Square" )
print("\n 2. Circle" )
print("\n 3. Triangle" )
print("\n 4. Rectangle" )
print("\n 5. Exit" )
#choice input :
choice = int(input("\nEnter your choice: "))
if choice ==1:
    print("\n 1. Area" )
    print("\n 2. Perimeter" )
    operation = int(input("\nEnter your operation: "))
    #operation on sqaure:
    if(operation == 1):
      side = float(input("\nEnter the side of the square(in Meters): "))
      print("\n Area of square is(in Meter^2) : ",twodfigures.calculate_square_area(side))
    elif(operation == 2):
      side = float(input("\nEnter the side of the square(in Meters): "))
      print("\n Perimeter of square is(in Meter) : ",twodfigures.calculate_square_perimeter(side))
      exit()
      #-----------------------------------------------------------------
      #operation on circle:
if choice ==2:
      print("\n 1. Area" )
      print("\n 2. Circumference" )
      operation = int(input("\nEnter your operation: "))
      if(operation == 1):
        radius = float(input("\nEnter the radius of the circle(in Meters): "))
        print("\n Area of circle is(in Meter^2) : ",twodfigures.calculate_circle_area(radius))
      elif(operation == 2):
        radius = float(input("\nEnter the radius of the circle(in Meters): "))
        print("\n Circumference of circle is (in Meter): ",twodfigures.calculate_circle_circumference(radius))
        exit()
        #----------------------------------------
        #operation on triangle:
if choice ==3:
        print("\n 1. Area" )
        print("\n 2. Perimeter" )
        operation = int(input("\nEnter your operation: "))
        if(operation == 1):
          base = float(input("\nEnter the base of the triangle(in Meters): "))
          height = float(input("\nEnter the height of the triangle(in Meters): "))
          print("\n Area of triangle is(in Meters): ",twodfigures.calculate_triangle_area(base,height))
        elif(operation == 2):
          side1 = float(input("\nEnter the side1 of the triangle(in Meters): "))
          side2 = float(input("\nEnter the side2 of the triangle(in Meters): "))
          side3 = float(input("\nEnter the side3 of the triangle: "))
          print("\n Perimeter of triangle is(in Meters) : ",twodfigures.calculate_triangle_perimeter(side1,side2,side3))
          exit()
          #---------------------------------------------------------------
          #operation on rectangle : 
if choice ==4:
          print("\n 1. Area" )
          print("\n 2. Perimeter" )
          operation = int(input("\nEnter your operation: "))
          if(operation == 1):
            length = float(input("\nEnter the length of the rectangle(in Meters): "))
            width = float(input("\nEnter the width of the rectangle(in Meters): "))
            print("\n Area of rectangle is(in Meters) : ",twodfigures.calculate_rectangle_area(length,width))
          elif(operation == 2):
            length = float(input("\nEnter the length of the rectangle(in Meters): "))
            width = float(input("\nEnter the width of the rectangle(in Meters): "))
            print("\n Perimeter of rectangle is(in Meter) : ",twodfigures.calculate_rectangle_perimeter(length,width))
            exit()
#-----------------------------------------------------------------------------
else:
    exit()
