'''Write a program to calculate area and perimeter of rectangle and validate it'''
#--------------------------
length = float(input("Enter the length (in meter)"))
if length < 0 :
  exit("length not in negative")
width = float(input("Enter the width (in meter)"))
if width < 0 :
 exit("width not in negative")
 #--------------------------
 print("Length :",length)
 print("Width :",width)
 #---------------------------
 area = length*width
 perimeter = 2(length + width)
 print("Area of circle is :",area)
 print("perimter of rectangle is :",perimeter)

