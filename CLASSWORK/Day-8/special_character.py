'''find the special characters in strings 
'''
#-----------------------------------------
#-----------coding-----------------------
#input the sentence :
sentence = input("Enter the sentence : ")
#initialize count as 0:
special_characters = 0
#iterate through the sentence:
for x in sentence:
    if(x.isalnum() == False  and x.isspace()== False  and x.isdigit() == False and x.isalpha() == False):
        special_characters += 1
print("No. of special characters : ", special_characters)
#------------------------------------------------
#----------------output---------------------------
