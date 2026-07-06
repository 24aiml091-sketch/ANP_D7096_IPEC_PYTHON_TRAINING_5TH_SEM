'''Area of circle'''
#input from user
radius = float(input("Enter the radius (in Meter) : "))
if radius < 0 :
  exit("Radius is not in negative")
pi = 3.1412
#-----------------------------------
print("Radius:",radius,"In Meter")
#--------------------------------
Area =(pi*radius*radius)
#----------------
print("Area of circle:",Area,"In Meter")