'''Problem Statement:
 Geometry Calculator Using Python Module Develop a menu-driven Python application that demonstrates
  the use of User-Defined Modules and Functions.
  
 Requirements You are required to create a Python module named twodfigures.py that contains functions
  to perform the following calculations for different two-dimensional shapes: 
  
  • Triangle 
  o Calculate Area
   o Calculate Perimeter 

   • Circle 
   o Calculate Area
    o Calculate Circumference (Perimeter)

 • Square
  o Calculate Area 
  o Calculate Perimeter

   • Rectangle
    o Calculate Area 
    o Calculate Perimeter'''

#-------------------------------------------
#-----------coding---------------------------

#triangle :
#area of triangle :

def calculate_triangle_area(height , base ):
    return  0.5 * base * height

#perimeter of triangle :
def calculate_triangle_perimeter(side1 , side2 , side3):
     return side1+side2+side3

#--------------------------------------------------

#circle :
#area of circle :
def calculate_circle_area(radius):
    return 3.14 * radius * radius

#circumference of circle:
def calculate_circle_circumference(radius):
    return 2*3.14*radius

#-----------------------------------------------
#square:
#Area of square :
def calculate_square_area(side):
    return side*side

#perimeter of square :
def calculate_square_perimeter(side):
    return 4*side
#-------------------------------------------------
#rectangle :
#area of rectangle :
def calculate_rectangle_area(length , width):
    return length*width
#perimeter of rectangle :
def calculate_rectangle_perimeter(length , width):
    return 2*(length+width)
#-------------------------------------------------
