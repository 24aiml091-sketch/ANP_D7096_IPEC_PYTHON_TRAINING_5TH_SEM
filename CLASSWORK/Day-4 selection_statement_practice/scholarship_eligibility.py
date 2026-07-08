'''A university provides a scholarship only to students who score 90 or above.
 Write a Python program to accept a student's percentage and determine whether the student is eligible.
  • If percentage is 90 or above, display: Scholarship Approved 
  • Otherwise display: Scholarship Not Approved
  ------------------------------------------------------------------
  Sample Input
   92 
   Sample Output 
   Scholarship Approved
  
  '''
  #-------------------------coding-------------------------
  
percentage = float(input("Enter the percentage of the student(%) : "))
#validation
if(percentage < 0):
    exit()
if(percentage > 100):
    exit()

    
if(percentage >= 90 ):
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")

#---------------------------------------------
#-------------------------Output--------------------------
'''Enter the percentage of the student(%) : 86
Scholarship Not Approved'''