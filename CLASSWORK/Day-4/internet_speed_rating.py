'''An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25–99 Mbps → Good  
• 100 Mbps or above → Excellent '''
#-----------------------------coding-----------------------------
speed = float(input("Enter the download speed(in Mbps) : "))
#validation
if(speed < 0):
    exit()
#Internet Speed :
elif(speed < 25):
    print("Slow")
elif(speed < 100):
    print("Good")
else:
    print("Excellent")

#----------------------output--------------------------
'''Enter the download speed(in Mbps) : 56
Good'''