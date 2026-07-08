'''accept a string and convert into upper case ,lower case and capitalize each word 
'''

#---------------------------------
#------coding---------------------
sentence = str(input("Enter the sentence : "))
#initalizing
lower_case = 0
upper_case = 0
#looping through the sentence
for x in sentence:
    if(x.islower()):
        lower_case += 1
    if(x.isupper()):
        upper_case += 1

#display the results
print("Lower case : ", lower_case)
print("Upper case : ", upper_case)
print("Capitalize : ", sentence.capitalize())
#--------------------------
#--------------------------
'''output:
Hello My Name Is Sanjay.
Lower case :  26
Upper case :  5
Capitalize :  Hello my name is sanjay.'''