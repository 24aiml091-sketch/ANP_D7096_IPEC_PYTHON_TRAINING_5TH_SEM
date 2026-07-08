'''A smartphone displays a low battery warning only when the battery percentage falls below 15%. '''
'''If the battery is below 15, 
display: 
Connect Charger Immediately Otherwise,
 display nothing. 
 -----------------------------------------
Sample 
Input 10 
Sample 
Output 
Connect Charger Immediately'''
#---------------------------------------
#--------coding---------------
#input from the user :
battery =int(input("Enter the percentage of battery :"))
#validation
if(battery < 0):
    exit()
if(battery >= 100):
    exit()
#Displaying Mobile battery warning
if(battery <= 15):
    print("Connect chagrer immediately")

#-----------------------------------------------------
# ----------output------------------------------    
'''Enter the percentage of battery :76'''