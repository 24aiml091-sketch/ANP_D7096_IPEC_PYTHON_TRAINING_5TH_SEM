'''find the no.of vowel in strings '''
#------------------------------------------
#input the sentence
string = input("Enter the sentence : ")
#----------------
#initialize count as 0:
vowels = 0
#----------------
for x in string:
    if(x == 'A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u'):
        vowels += 1
print("Total number of vowels : ", vowels)
#-------------------------------------
#---------coding-------------------------
'''Enter the sentence : Hello my name is sanjay. I'm a b.tech student.
Total number of vowels :  12'''

    