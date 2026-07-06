'''A school assigns grades based on the marks obtained by students according to the following criteria:

* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F
'''
#----------------------------------------------------
#----------Coding--------------------------
#------------------------------------------
grade = float(input("Enter the marks : "))
if(grade < 0 or grade >100):
    exit("Marks must be between 0 and 100")
if(grade >= 90):
    print("Grade A")
elif(grade >=75 and grade <=89):
    print("Grade B")
elif(grade >=50 and grade <=74):
    print("Grade C")
else:
    print("Grade F")
#--------------------------------------
#----------- Output -------------------
#--------------------------------------
'''Enter the marks : 50
Grade C
'''
#--------------------------------------
#----------- Output -------------------
#--------------------------------------
'''Enter the marks : 78
Grade B
'''
#--------------------------------------
#----------- Output -------------------
#--------------------------------------
'''Enter the marks : 98
Grade A
'''